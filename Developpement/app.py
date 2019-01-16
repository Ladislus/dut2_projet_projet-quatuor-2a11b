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
            os.path.dirname(__file__),p
        )
    )

Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('database.db'))
app.config['BOOTSTRAP_SERVE_LOCAL']=True
app.config["SECRET_KEY"] = "fec03c30-124c-43b2-85db-4dfb72c4b56e"
app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'projetquatuordivertimento',
    MAIL_PASSWORD = '[projettest]'
))

mail = Mail(app)
