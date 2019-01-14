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
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Float, Date, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = db.Model

#Tables associatives
article_media        = Table("article_media", Base.metadata,
                        Column("idArt", Integer, ForeignKey("Article.idArt")),
                        Column("idMed", Integer, ForeignKey("Media.idMed")) )

repertoire_partition = Table("repertoire_partition", Base.metadata,
                        Column("idRep", Integer, ForeignKey("Repertoire.idRep")),
                        Column("idPart", Integer, ForeignKey("Partition.idPart")) )

stage_media          = Table("stage_media", Base.metadata,
                        Column("idSt", Integer, ForeignKey("Stage.idSt")),
                        Column("idMed", Integer, ForeignKey("Media.idMed")) )

#Tables
class Utilisateur(Base):
    idUt       = Column(Integer, primary_key = True, autoincrement = True)
    ecoleUt    = Column(String(50))
    nivUt      = Column(Integer)
    usernameUt = Column(String(30), nullable = False, unique = True)
    mdpUt      = Column(String(30), nullable = False)
    roleUt     = Column(String(10), default = 'UTILISATEUR')

    idPers     = Column(Integer, ForeignKey("Personne.idPers"))

    personne   = relationship("Personne", backref = "utilisateur")

class Personne(Base):
    idPers      = Column(Integer, primary_key = True, autoincrement = True)
    nomPers     = Column(String(20))
    prenomPers  = Column(String(20))
    mailPers    = Column(String(50), unique = True)
    telPersUn   = Column(String(10), nullable = False)
    telPersDeux = Column(String(10))
    dateNPers   = Column(Date)
    newsPers    = Column(Boolean, default = False)
    ifTuteur    = Column(Integer)                                                #TODO : obligatoire si age < 18; trigger pour savoir si tuteur.age > 18

    idLieu      = Column(Integer, ForeignKey("Lieu.idLieu"))

    adresse     = relationship("Adresse")
    tuteur      = relationship("Personne", remote_side = [idPers])

    #TODO : relation de tuteur (Personne vers Personne)
    # alternates = relationship('Issue',
    #             backref=backref('parent', remote_side=[id])
    #         )
    # #This is what you need to add to make the database link it self
    # parent_id=Column(Integer, ForeignKey('issues.id'))
    # children=relationship('Issue', backref=backref('parent', remote_side=[id]))
    # #Calling children would send you all the children of the parent.
    # #Calling parent would give you the parent of the current group. If it returns None then you are looking at a root Issue.

class JoueInstrument(Base):
    niveauInstru = Column(Integer)

    idUt         = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idInstru     = Column(Integer, ForeignKey("Instrument.idInstru"), primary_key = True)

    utilisateur  = relationship("Utilisateur", backref = "instruments")
    instrument   = relationship("Instrument", backref = "utilisateurs")

class Participe(Base):
    statePaieSt = Column(String(10), nullable = False, default = 'EN ATTENTE')
    stateValSt  = Column(String(10), nullable = False, default = 'EN ATTENTE')
    ficheMed    = Column(BLOB, nullable = False)
    autParent   = Column(BLOB)                                                          #TODO : Trigger if Personne.age < 18

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idSt        = Column(Integer, ForeignKey("Stage.idSt"), primary_key = True)

    utilisateur = relationship("Utilisateur", backref = "participations")
    stage       = relationship("Stage", backref = "participants")

class InscrireInstru(Base):
    voieJoue    = Column(String(20), nullable = False)

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idSt        = Column(Integer, ForeignKey("Stage.idSt"), primary_key = True)
    idInstru    = Column(Integer, ForeignKey("Instrument.idInstru"), primary_key = True)

    utilisateur = relationship("Utilisateur")
    instrument  = relationship("Instrument")
    stage       = relationship("Stage", backref = "instruments")

class Stage(Base):
    idSt        = Column(Integer, primary_key = True, autoincrement = True)
    idRep       = Column(Integer)                                               #TODO : Trigger lors de l'insertion/modification si l'idRep est dans Repertoire
    intituleSt  = Column(String(30), nullable = False)
    nbPlaceSt   = Column(Integer)
    dateDebSt   = Column(Date, unique = True)                                   #TODO : Trigger lors de l'insertion/modification si un autre stage est en cour
    dateFinSt   = Column(Date)                                                  #TODO : trigger lors de l'insertion/modification si la date de fin n'est pas enterieur a la date de début
    idLieu      = Column(Integer)                                               #TODO : trigger lors de l'insertion/modification si l'idLieu est dans Lieu
    vetSt       = Column(String(40))
    prixSt      = Column(Float)
    descSt      = Column(Text)
    nivRequisSt = Column(Integer)

    medias      = relationship("Media", secondary = stage_media, back_populates = "stages")

class Instrument(Base):
    idInstru  = Column(Integer, primary_key = True, autoincrement = True)
    nomInstru = Column(String(20), unique = True, nullable = False)

class Repertoire(Base):
    idRep    = Column(Integer, primary_key = True, autoincrement = True)
    idSt     = Column(Integer)                                                  #TODO : Trigger lors de l'insertion/modification si la stage existe
    nomRep   = Column(String(20), unique = True, nullable = False)

    idInstru = Column(Integer, ForeignKey("Instrument.idInstru"))

    partitions = relationship("Partition", secondary = repertoire_partition, back_populates = "repertoires")

class Partition(Base):
    idPart      = Column(Integer, primary_key = True, autoincrement = True)
    nomPart     = Column(String(20), nullable = False)
    autPart     = Column(String(20), nullable = False)
    stylePart   = Column(String(20), nullable = False)
    origPart    = Column(String(10), default = 'ORIGINAL')
    ficPart     = Column(BLOB)

    idInstru    = Column(Integer, ForeignKey("Instrument.idInstru"), nullable = False)

    repertoires = relationship("Repertoire", secondary = repertoire_partition, back_populates = "partitions")

    UniqueConstraint(nomPart, autPart, idInstru, name = "unique_partition")

class Concert(Base):
    idConcert       = Column(Integer, primary_key = True, autoincrement = True)
    titreConcert    = Column(String(30), nullable = False)
    dateConcert     = Column(Date, unique = True)                               #TODO : Trigger lors de l'insertion/modification si un autre concert est en cour
    isStageConcert  = Column(Boolean, default = False)
    descConcert     = Column(Text)
    idLieu          = Column(Integer)                                           #TODO : Trigger lors de l'insertion/modification si l'idLieu est dans Lieu

class Lieu(Base):
    idLieu    = Column(Integer, primary_key = True, autoincrement = True)
    adrLieu   = Column(Text, nullable = False)
    codeLieu  = Column(Integer, nullable = False)
    villeLieu = Column(String(50), nullable = False)

    UniqueConstraint(adrLieu, codeLieu, villeLieu, name = "unique_lieu")

class Article(Base):
    idArt       = Column(Integer, primary_key = True, autoincrement = True)
    titreArt    = Column(String(200), unique = True)
    datePubArt  = Column(Date, nullable = False)
    contenuArt  = Column(Text)

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"))

    medias      = relationship("Media", secondary = article_media, back_populates = "articles")
    utilisateur = relationship("Utilisateur", backref = "articles")

class Media(Base):
    idMed        = Column(Integer, primary_key = True, autoincrement = True)
    nomMed       = Column(String(40), nullable = False)
    typeMed      = Column(String(10), nullable = False)
    ficMed       = Column(BLOB, nullable = False)

    idCom        = Column(Integer, ForeignKey("Commentaire.idCom"))

    articles     = relationship("Article", secondary = article_media, back_populates = "medias")
    stages       = relationship("Stage", secondary = stage_media, back_populates = "medias")
    commentaires = relationship("Commentaire", backref = "article")

    UniqueConstraint(nomMed, typeMed, name = "unique_media")

class Commentaire(Base):
    idCom       = Column(Integer, primary_key = True, autoincrement = True)
    dateCom     = Column(Date, nullable = True)
    contenuCom  = Column(Text, nullable = True)

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)

<<<<<<< HEAD
class InscrireInstru(db.Model)
>>>>>>> ajout de Utilisateur, Personne et Participe dans le model
=======
    utilisateur = relationship("Utilisateur", backref = "commentaires")
>>>>>>> Base de donnée v1.
