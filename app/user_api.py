from flask import Blueprint, jsonify, request
from app.models.users import User
from app.extensions import db

users_api = Blueprint('users_api', __name__)


# Получить всех пользователей
@users_api.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])


# Получить одного пользователя
@users_api.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user.to_dict())


# Добавить нового пользователя
@users_api.route('/api/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Empty request'}), 400

    required_fields = ['surname', 'name', 'age', 'email']
    missing = [field for field in required_fields if field not in data]
    if missing:
        return jsonify({'error': 'Missing fields', 'missing': missing}), 400

    try:
        user = User(
            surname=data['surname'],
            name=data['name'],
            age=int(data['age']),
            position=data.get('position'),
            speciality=data.get('speciality'),
            address=data.get('address'),
            email=data['email'],
            hashed_password=data['password'],
        )
        db.session.add(user)
        db.session.commit()
        return jsonify({'success': 'User added', 'id': user.id}), 201
    except Exception as e:
        return jsonify({'error': f'Error adding user: {str(e)}'}), 400


# Обновить пользователя
@users_api.route('/api/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    data = request.get_json()
    if not data:
        return jsonify({'error': 'Empty request'}), 400

    for key in data:
        if hasattr(user, key):
            setattr(user, key, data[key])

    db.session.commit()
    return jsonify({'success': 'User updated'})


# Удалить пользователя
@users_api.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'error': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': 'User deleted'})