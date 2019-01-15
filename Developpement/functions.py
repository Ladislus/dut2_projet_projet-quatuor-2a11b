from hashlib import sha512
from models import *

def crypt(password):
    """
    Crypte le parametre "password" (String) avec le SHA512
    """
    crypter = sha512()
    crypter.update(password.encode())
    return crypter.hexigest()

def init_db(filename = None):
    """
    Initialise la base de donnée
    """
    # creation de toutes les tables
    db.create_all()
