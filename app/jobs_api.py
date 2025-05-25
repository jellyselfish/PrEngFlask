from flask import Blueprint, jsonify, request
from app.models.jobs import Job
from app.extensions import db

jobs_api = Blueprint('jobs_api', __name__)


@jobs_api.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([job.to_dict() for job in jobs])


@jobs_api.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404
    return jsonify(job.to_dict())


@jobs_api.route('/api/jobs', methods=['POST'])
def create_job():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Empty request'}), 400

    required_fields = ['team_leader', 'job', 'work_size', 'collaborators']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({'error': 'Missing fields', 'missing': missing}), 400

    job = Job(
        team_leader=data['team_leader'],
        job=data['job'],
        work_size=data.get('work_size', 0),
        collaborators=data.get('collaborators', ''),
        is_finished=data.get('is_finished', False)
    )
    db.session.add(job)
    db.session.commit()
    return jsonify({'success': 'Job added', 'id': job.id}), 201


@jobs_api.route('/api/jobs/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    db.session.delete(job)
    db.session.commit()
    return jsonify({'success': 'Job deleted'})


@jobs_api.route('/api/jobs/<int:job_id>', methods=['PUT'])
def edit_job(job_id):
    job = Job.query.get(job_id)
    if not job:
        return jsonify({'error': 'Job not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Empty request'}), 400

    for key in data:
        if hasattr(job, key):
            setattr(job, key, data[key])

    db.session.commit()
    return jsonify({'success': 'Job updated'})

