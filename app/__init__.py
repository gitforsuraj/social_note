from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_materialize import Material  

app = Flask(__name__)
app.config.from_object(Config)
Material(app)


db = SQLAlchemy(app)

login = LoginManager(app)
# right side is the function that's called to login users
login.login_view = 'login'

from app import routes, models