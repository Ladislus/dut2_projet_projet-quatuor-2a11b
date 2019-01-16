from flask import Flask
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager



app = Flask(__name__)
app.debug = True

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),p
        )
    )

db = SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager(app)

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../database.db'))
app.config['BOOTSTRAP_SERVE_LOCAL']=True
app.config["SECRET_KEY"] = "fec03c30-124c-43b2-85db-4dfb72c4b56e"
