from flask import Flask
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
