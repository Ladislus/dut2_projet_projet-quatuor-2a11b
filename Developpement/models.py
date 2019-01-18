from .app import db, app
from .functions import *
from .getters import *
from .inserts import *

from sqlalchemy.dialects.sqlite import BLOB
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, Text, Float, Date, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

from flask_login import UserMixin
from flask_security import RoleMixin, SQLAlchemySessionUserDatastore, Security

Base = db.Model

#Tables associatives
repertoire_partition = Table("repertoire_partition", Base.metadata,
                        Column("idRep", Integer, ForeignKey("Repertoire.idRep")),
                        Column("idPart", Integer, ForeignKey("Partition.idPart")) )

article_media         = Table("article_media", Base.metadata,
                         Column("idArt", Integer, ForeignKey("Article.idArt")),
                         Column("idMed", Integer, ForeignKey("Media.idMed")) )

stage_media           = Table("stage_media", Base.metadata,
                         Column("idSt", Integer, ForeignKey("Stage.idSt")),
                         Column("idMed", Integer, ForeignKey("Media.idMed")) )

#Tables
class Utilisateur(Base, UserMixin):
    __tablename__ = "Utilisateur"

    idUt           = Column(Integer, primary_key = True, autoincrement = True)
    ecoleUt        = Column(String(50))
    nivUt          = Column(Integer)
    usernameUt     = Column(String(30), nullable = False, unique = True)
    mdpUt          = Column(String(30), nullable = False)
    roleUt         = Column(String(10), default = 'UTILISATEUR')

    id_Role        = Column(Integer, ForeignKey("Role.idRole"))
    id_Pers        = Column(Integer, ForeignKey("Personne.idPers"))

    personne       = relationship("Personne")
    roleUt         = relationship("Role", back_populates = "membres")
    instruments    = relationship("JoueInstrument", back_populates = "joueur")
    participations = relationship("Participe", back_populates = "utilisateur")
    instruInscrits = relationship("InscrireInstru", back_populates = "utilisateur")
    articles       = relationship("Article", back_populates = "auteur")
    commentaires   = relationship("Commentaire", back_populates = "auteur")

class Role(Base, RoleMixin):
    __tablename__ = "Role"

    idRole  = Column(Integer, primary_key = True, autoincrement = True)
    nomRole = Column(String(20), unique = True)

    membres = relationship("Utilisateur", back_populates = "roleUt")

class Personne(Base, UserMixin):
    __tablename__ = "Personne"

    idPers      = Column(Integer, primary_key = True, autoincrement = True)
    nomPers     = Column(String(20))
    prenomPers  = Column(String(20))
    mailPers    = Column(String(50), unique = True)
    telPersUn   = Column(String(10), nullable = False)
    telPersDeux = Column(String(10))
    dateNPers   = Column(Date)

    idTuteur    = Column(Integer)                                               #TODO : obligatoire si age < 18; trigger pour savoir si tuteur.age > 18

    id_Lieu     = Column(Integer, ForeignKey("Lieu.idLieu"))

    adresse     = relationship("Lieu", back_populates = "residants")

class JoueInstrument(Base):
    __tablename__ = "JoueInstrument"

    niveauInstru = Column(Integer)

    idUt         = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idInstru     = Column(Integer, ForeignKey("Instrument.idInstru"), primary_key = True)

    joueur       = relationship("Utilisateur", back_populates = "instruments")
    instrument   = relationship("Instrument", back_populates = "joueurs")

class Participe(Base):
    __tablename__ = "Participe"

    statePaieSt = Column(String(10), nullable = False, default = 'EN ATTENTE')
    stateValSt  = Column(String(10), nullable = False, default = 'EN ATTENTE')
    newsPers    = Column(Boolean, default = False)
    audPrivPers = Column(Boolean, default = False)
    audPublPers = Column(Boolean, default = False)
    imgPrivPers = Column(Boolean, default = False)
    imgPublPers = Column(Boolean, default = False)
    telUrg1     = Column(String(10), nullable = False)
    telUrg2     = Column(String(10), nullable = False)
    telUrg3     = Column(String(10))

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idSt        = Column(Integer, ForeignKey("Stage.idSt"), primary_key = True)

    utilisateur = relationship("Utilisateur", back_populates = "participations")
    stage       = relationship("Stage", back_populates = "participants")

class InscrireInstru(Base):
    __tablename__ = "InscrireInstru"

    voieJoue    = Column(String(20), nullable = False)

    idUt        = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    idSt        = Column(Integer, ForeignKey("Stage.idSt"), primary_key = True)
    idInstru    = Column(Integer, ForeignKey("Instrument.idInstru"), primary_key = True)

    utilisateur = relationship("Utilisateur", back_populates = "instruInscrits")
    stage       = relationship("Stage", back_populates = "instruInscrits")
    instrument  = relationship("Instrument")

class Stage(Base):
    __tablename__ = "Stage"

    idSt           = Column(Integer, primary_key = True, autoincrement = True)
    idRep          = Column(Integer)                                               #TODO : Trigger lors de l'insertion/modification si l'idRep est dans Repertoire
    intituleSt     = Column(String(30), nullable = False)
    nbPlaceSt      = Column(Integer)
    dateDebSt      = Column(Date, unique = True)                                   #TODO : Trigger lors de l'insertion/modification si un autre stage est en cour
    dateFinSt      = Column(Date)                                                  #TODO : trigger lors de l'insertion/modification si la date de fin n'est pas enterieur a la date de début
    idLieu         = Column(Integer)                                               #TODO : trigger lors de l'insertion/modification si l'idLieu est dans Lieu
    vetSt          = Column(String(40))
    prixSt         = Column(Float)
    descSt         = Column(Text)
    nivRequisSt    = Column(Integer)

    participants   = relationship("Participe", back_populates = "stage")
    instruInscrits = relationship("InscrireInstru", back_populates = "stage")
    medias         = relationship("Media", secondary = stage_media, back_populates = "stages")

class Instrument(Base):
    __tablename__ = "Instrument"

    idInstru    = Column(Integer, primary_key = True, autoincrement = True)
    nomInstru   = Column(String(20), unique = True, nullable = False)

    joueurs     = relationship("JoueInstrument", back_populates = "instrument")
    partitions  = relationship("Partition", back_populates = "instrument")

class Repertoire(Base):
    __tablename__ = "Repertoire"

    idRep       = Column(Integer, primary_key = True, autoincrement = True)
    nomRep      = Column(String(20), unique = True, nullable = False)

    partitions  = relationship("Partition", secondary = repertoire_partition, back_populates = "repertoires")

class Partition(Base):
    __tablename__ = "Partition"

    idPart      = Column(Integer, primary_key = True, autoincrement = True)
    nomPart     = Column(String(20), nullable = False)
    autPart     = Column(String(20), nullable = False)
    stylePart   = Column(String(20), nullable = False)
    origPart    = Column(String(10), default = 'ORIGINAL')
    ficPart     = Column(BLOB)

    id_Instru   = Column(Integer, ForeignKey("Instrument.idInstru"))

    instrument  = relationship("Instrument", back_populates = "partitions")
    repertoires = relationship("Repertoire", secondary = repertoire_partition, back_populates = "partitions")

    UniqueConstraint(nomPart, autPart, id_Instru, name = "unique_partition")

class Concert(Base):
    __tablename__ = "Concert"

    idConcert       = Column(Integer, primary_key = True, autoincrement = True)
    titreConcert    = Column(String(30), nullable = False)
    dateConcert     = Column(Date, unique = True)                               #TODO : Trigger lors de l'insertion/modification si un autre concert est en cour
    isStageConcert  = Column(Boolean, default = False)
    descConcert     = Column(Text)
    idLieu          = Column(Integer)                                           #TODO : Trigger lors de l'insertion/modification si l'idLieu est dans Lieu

class Lieu(Base):
    __tablename__ = "Lieu"

    idLieu    = Column(Integer, primary_key = True, autoincrement = True)
    adrLieu   = Column(Text, nullable = False)
    codeLieu  = Column(Integer, nullable = False)
    villeLieu = Column(String(50), nullable = False)

    residants = relationship("Personne", back_populates = "adresse")

    UniqueConstraint(adrLieu, codeLieu, villeLieu, name = "unique_lieu")

class Article(Base):
    __tablename__ = "Article"

    idArt        = Column(Integer, primary_key = True, autoincrement = True)
    titreArt     = Column(String(200), unique = True)
    datePubArt   = Column(Date, nullable = False)
    contenuArt   = Column(Text)

    id_Ut        = Column(Integer, ForeignKey("Utilisateur.idUt"))

    auteur       = relationship("Utilisateur", back_populates = "articles")
    medias       = relationship("Media", secondary = "article_media", back_populates = "articles")
    commentaires = relationship("Commentaire", back_populates = "article")

class Media(Base):
    __tablename__ = "Media"

    idMed        = Column(Integer, primary_key = True, autoincrement = True)
    nomMed       = Column(String(40), nullable = False)
    typeMed      = Column(String(10), nullable = False)
    ficMed       = Column(BLOB, nullable = False)
    specMed      = Column(String(10), default = 'NOPE') #Peut être 'EXTRAIT',

    articles     = relationship("Article", secondary = "article_media", back_populates = "medias")
    stages       = relationship("Stage", secondary = "stage_media", back_populates = "medias")

class Commentaire(Base):
    __tablename__ = "Commentaire"

    idCom       = Column(Integer, primary_key = True)
    dateCom     = Column(Date, nullable = True)
    contenuCom  = Column(Text, nullable = True)

    id_Ut       = Column(Integer, ForeignKey("Utilisateur.idUt"), primary_key = True)
    id_Art      = Column(Integer, ForeignKey("Article.idArt"))

    auteur      = relationship("Utilisateur", back_populates = "commentaires")
    article     = relationship("Article", back_populates = "commentaires")

user_datastore = SQLAlchemySessionUserDatastore(db, Utilisateur, Role)
app.security = Security(app, user_datastore)
