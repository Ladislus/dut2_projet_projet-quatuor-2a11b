from .app import db

def new_role(nom):
    db.seesion.add(Role(nom))
    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
