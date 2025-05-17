from flask import Flask
from models.users import db
from routers.main_routers_11_12 import bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///firm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(debug=True, port=8080)