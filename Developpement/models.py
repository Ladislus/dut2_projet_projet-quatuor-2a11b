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
