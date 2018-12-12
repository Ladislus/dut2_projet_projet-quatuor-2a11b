from flask import Flask
from flask_bootstrap import Bootstrap
app = Flask(__name__)
app.debug=True
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)

import os.path
def mkpath(p):
    return os.path.normpath(os.path.join(os.path.dirname(__file__),p))

from flask_sqlalchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = ('sqlite:///'+mkpath('../myapp.db'))
db = SQLAlchemy(app)

app.config['SECRET_KEY']="1f32daee-b73d-4c12-beb3-fae8e7eb5a30"

from flask_login import LoginManager
login_manager = LoginManager(app)
login_manager.login_view="login"