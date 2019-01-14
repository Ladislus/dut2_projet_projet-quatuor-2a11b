<<<<<<< HEAD
### FICHIER DES METHODES PERMETTANT L'ACCES a LA BD ###

from .app import db

class Utilisateur(db.Model):
    """
    Creation de la table 'Utilisateur' dans la BD
    """

    idUt = db.Column(db.Integer(), primary_key = True)
    usernameUt = db.Column(db.String(30))
    mdpUt = db.Column(db.Integer())
    nomUt = db.Column(db.String(20))
    prenomUt = db.Column(db.String(20))
    mailUt = db.Column(db.String(75))
    dateNUt = db.Column(db.Date())
    idLieu = db.Column(db.Integer(), db.ForeignKey("lieu.id"))
    ecoleUt = db.Column(db.String(50))
    niveauUt = db.Column(db.Integer())
    roleUt = db.Column(db.String(10)) #UTILISATEUR, STAGIAIRE, MEMBRE, ADMIN

class Stage(db.Model):
    """
    Creation de la table 'Stage' dans la BD
    """
    idSt = db.Column(db.Integer(), primary_key = True)
    idRep = db.Column(db.Integer(), db.ForeignKey("repertoire.id"))
    intituleSt = db.Column(db.String(30))
    nbPlaceSt = db.Column(db.Integer())
    dateDebSt = db.Column(db.Date())
    dateFinSt = db.Column(db.Date())
    idLieu = db.Column(db.Integer(), db.ForeignKey("lieu.id"))
    vetSt = db.Column(db.String(30))
    prixSt = db.Column(db.Integer(6,2))
    descSt = db.Column(db.Longtext())
    nivRequisSt = db.Column(db.Integer())

class Partition(db.Model):
    """
    Creation de la table 'Partition' dans la BD
    """
    idPart = db.Column(db.Integer(), primary_key = True)
    idInstru = db.Column(db.Integer(), db.ForeignKey("instrument.id"))
    nomPart = db.Column(db.String(30))
    autPart = db.Column(db.String(30))
    stylePart = db.Column(db.String(20))
    origPart = db.Column(db.String(10)) #ORIGINALE ou ARRANGEE
    ficPart = db.Column(db.MediumBlob())

class Recette(db.Model):
    """
    Creation de la table 'Recette' dans la BD
    """

class Concert(db.Model):
    """
    Creation de la table 'Concert' dans la BD
    """

class Lieu(db.Model):
    """
    Creation de la table 'Lieu' dans la BD
    """

class Article(db.Model):
    """
    Creation de la table 'Article' dans la BD
    """

class Media(db.Model):
    """
    Creation de la table 'Media' dans la BD
    """

class Avis(db.Model):
    """
    Creation de la table 'Avis' dans la BD
    """

class Media(db.Model):
    """
    Creation de la table 'Media' dans la BD
    """
#############################################

def quatuor_getRepertoire(n=None):
    """
    retourne une liste de tuples comportant :
        - la musique jouee
        - l'auteur
    """

def quatuor_getMedia(n=None):
    """
    retourne une liste de tuples comportant :
        - les extraits musicaux
        - le titre de la musique correspondante
        - une liste des instruments utilises
    """
=======
from app import db

from sqlalchemy.dialects.sqlite import BLOB

class Utilisateur(db.Model):
    idUt       = db.Column(db.Integer, primary_key = True)
    ecoleUt    = db.Column(db.String(50))
    nivUt      = db.Column(db.Integer)
    usernameUt = db.Column(db.String(30), nullable = False, unique = True)
    mdpUt      = db.Column(db.String(30), nullable = False)
    roleUt     = db.Column(db.String(10))

    pers_id    = db.Column(Integer, ForeignKey("personne.idPers"))

    personne   = db.relationsip("Personne", db.backref="utilisateur")

class Personne(db.Model):
    idPers      = db.Column(db.Integer, primary_key = True)
    nomPers     = db.Column(db.String(20))
    prenomPers  = db.Column(db.String(20))
    mailPers    = db.Column(db.String(50), unique = True)
    telPersUn   = db.Column(db.String(10))
    dateNPers   = db.Column(db.DateTime)
    newsPers    = db.Column(db.Boolean, default = False)

    adresse_id  = db.Column(db.Integer, ForeignKey("Lieu.idLieu"))

    adresse     = db.relationsip("Adresse")
    tuteur      = db.relationsip("Personne", remote_side = [idPers])

    #TODO : relation de tuteur (Personne vers Personne)
    # alternates = db.relationship('Issue',
    #             backref=db.backref('parent', remote_side=[id])
    #         )
    # #This is what you need to add to make the database link it self
    # parent_id=db.Column(db.Integer, db.ForeignKey('issues.id'))
    # children=db.relationship('Issue', backref=db.backref('parent', remote_side=[id]))
    # #Calling children would send you all the children of the parent.
    # #Calling parent would give you the parent of the current group. If it returns None then you are looking at a root Issue.


class Participe(db.Model):
    statePaieSt = db.Column(db.String(10), nullable = False, default = 'EN ATTENTE')
    stateValSt  = db.Column(db.String(10), nullable = False, default = 'EN ATTENTE')
    ficheMed    = db.Column(BLOB, nullable = False)
    autParent   = db.Column(BLOB)   #TODO : Trigger if Personne.age < 18

    idUt        = db.Column(db.Integer, ForeignKey("utilisateur.idUt"), primary_key = True)
    idSt        = db.Column(db.Integer, ForeignKey("stage.idSt"), primary_key = True)

    utilisateur = db.relationsip("Utilisateur", db.backref="participations")
    stage       = db.relationsip("Stage", db.backref="participants")

class InscrireInstru(db.Model)
>>>>>>> ajout de Utilisateur, Personne et Participe dans le model
