from flask import Flask
from routers.main_routers_8_10 import bp

app = Flask(__name__)
app.register_blueprint(bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
