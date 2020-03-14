from flask import Flask
# from flask_script import Manager
from settings import setting
from app.urls import index

app = Flask(__name__, template_folder='templates/', static_folder='static/')
app.config.from_object(setting["defaultConfig"])

app.register_blueprint(index)

if __name__ == "__main__":
    app.run()
