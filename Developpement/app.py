import os.path
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_mail import Mail, Message
import os.path

app = Flask(__name__)
app.debug = True

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__), p ))

db = SQLAlchemy(app)
Bootstrap(app)

login_manager = LoginManager(app)
login_manager.login_view = "other_connexion"

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('database.db'))
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config["SECRET_KEY"] = "fec03c30-124c-43b2-85db-4dfb72c4b56e"
