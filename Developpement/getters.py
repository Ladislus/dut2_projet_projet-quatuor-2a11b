def get_concerts():
    return Concert.query.all()

def get_extraits():
    return Media.query.filter(Media.specMed == 'EXTRAIT')

def get_user(username):
    return Utilisateur.query.get(username)
