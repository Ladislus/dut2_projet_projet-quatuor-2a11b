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

def get_concert():
    return Concert.query.all()

def get_extrait():
    medias = Media.query.filter(Media.typeMed == ".mp4")
    return [ media for media in medias if media.specMed == 'EXTRAIT' ]

def get_articles():
    return Article.query().all()
