from flask import Flask

from app.extensions import db
from routers.main_routers_16_19 import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)

app.register_blueprint(bp)

# with app.app_context():
#    db.create_all()

if __name__ == '__main__':
    app.run(debug=True, port=8080)
    print(id(db))
