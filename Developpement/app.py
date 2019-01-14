from flask import Flask
<<<<<<< HEAD
from flask_bootstrap import Bootstrap
import os.path
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__),p))


app =Flask(__name__)
app.config['SECRET_KEY']= "4b26de02-bc1b-46ff-9501-06e041851b00"
app.debug=True
app.config['BOOTSTRAP_SERVE_LOCAL']=True
app.config['SQLALCHEMY_DATABASE_URI']=('sqlite:///'+mkpath('../myapp.db'))
db=SQLAlchemy(app)
Bootstrap(app)
login_manager = LoginManager(app)
=======

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.debug = True

import os.path
def mkpath(p):
    return os.path.normpath(
        os.path.join(
            os.path.dirname(__file__),p
        )
    )

app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../database.db'))

db = SQLAlchemy(app)

app.config["SECRET_KEY"] = "fec03c30-124c-43b2-85db-4dfb72c4b56e"
>>>>>>> ajout de Utilisateur, Personne et Participe dans le model
