def get_concerts():
    return Concert.query.all()

def get_extraits():
    return Media.query.filter(Media.specMed == 'EXTRAIT')
