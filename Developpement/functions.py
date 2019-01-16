from hashlib import sha512

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
    db.create_all()

def get_concerts():
    return Concert.query.all()

def get_extraits():
    medias = Media.query.filter(Media.specMed == 'EXTRAIT')
