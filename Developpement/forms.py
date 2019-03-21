from .models import *
from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, FieldList, FileField, FloatField, FormField, HiddenField, IntegerField, PasswordField, SelectField, SelectMultipleField, StringField, TextField, TextAreaField
from wtforms.validators import DataRequired, Length, Required, Optional

class InscriptionForm(FlaskForm):
    nomPers         = StringField('Nom', validators=[DataRequired()])
    prenomPers      = StringField('Prénom', validators=[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators=[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators=[DataRequired()])
    clarJouees      = SelectMultipleField('Clarinette jouée', choices=[], validators=[DataRequired()])
    niveau          = IntegerField('Année d\'experience', validators=[DataRequired()])
    ecole           = StringField('Ecole', validators=[DataRequired()])
    typePratique    = StringField('Type de pratique')
    nomPers         = StringField('Nom', validators=[DataRequired()])
    prenomPers      = StringField('Prénom', validators=[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators=[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators=[DataRequired()])
    clarJouees      = SelectMultipleField('Clarinette jouée', choices=[], validators=[DataRequired()])
    niveau          = IntegerField('Année d\'experience', validators=[DataRequired()])
    ecole           = StringField('Ecole', validators=[DataRequired()])
    typePratique    = StringField('Type de pratique')

class PersonForm(FlaskForm):
    nomPers         = StringField('Nom', validators=[DataRequired()])
    prenomPers      = StringField('Prénom', validators=[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators=[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators=[DataRequired()])
    clarJouees      = SelectMultipleField('Clarinette jouée', choices=[("test", "onsaitpas")], validators=[DataRequired()])
    niveau          = IntegerField('Année d\'experience', validators=[DataRequired()])
    ecole           = StringField('Ecole', validators=[DataRequired()])

class NiveauForm(FlaskForm):
    niveau = SelectField('Niveau', choices=[("Niveau 1"),("Niveau 2"),("Niveau 3")])

class LieuForm(FlaskForm):
    adrLieu         = StringField('Adresse du Lieu', validators=[DataRequired()])
    CPLieu          = IntegerField('Code Postal du Lieu', validators=[DataRequired()])
    villeLieu       = StringField('Ville du Lieu', validators=[DataRequired()])

class NiveauForm(FlaskForm):
    niveau = SelectField('Niveau', choices=['Niveau 1', 'Niveau 2', 'Niveau 3'], validators=[DataRequired()])

class RespLegalForm(FlaskForm):
    nomResp         = StringField('Nom du Responsable', validators=[DataRequired()])
    prenomResp      = StringField('Prénom du Responsable', validators=[DataRequired()])
    telPers         = StringField('Téléphone personnel', validators=[DataRequired()])
    telTrav         = StringField('Téléphone travail')
    mailPers        = StringField('Adresse Mail Personnelle', validators=[DataRequired()])
    mailTrav        = StringField('Adresse Mail de Travail')
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])

class User_ContactForm(FlaskForm):
    nomAuteur       = StringField('Nom', validators=[DataRequired()])
    prenomAuteur    = StringField('Prénom', validators=[DataRequired()])
    mailAuteur      = StringField('Adresse Mail', validators=[DataRequired()])
    objetMessage    = SelectField('Objet', choices=[("choix","--Choix--"),('stage',"Stage"),('concert',"Concert"),("autre","autre")], validators=[DataRequired()])
    contenuMessage  = TextAreaField('Contenu du message',validators=[DataRequired()])
    pjMessage       = FileField()
    autrobjMessage  = TextField('Objet autre', validators=[DataRequired()])

class Admin_ContactForm(FlaskForm):
    objetMessage    = SelectField('Objet', choices=[("choix","--Choix-- "),('admin', "Adminstratif "), ('music', "Musical "), ('ques', "Question "),('autre',"autre ")], validators=[DataRequired()])
    autrobjMessage  = TextField('Objet autre', validators=[DataRequired()])
    destMessage     = SelectField('Destinataire', choices=[("choix","--Choix-- "),('dest1', "dest1"),('dest2', "dest2"),('autre',"autre")], validators=[DataRequired()])
    autrDestMessage = TextField('Adresse autre', validators=[DataRequired()])
    contenuMessage  = TextAreaField('Contenu du message',validators=[DataRequired()])
    pjMessage       = FileField()

class AutorMedicForm(FlaskForm):
    numContactUrg1  = StringField('Numero à contacter Urgence 1', validators=[DataRequired()])
    numContactUrg2  = StringField('Numero à contacter Urgence 2', validators=[DataRequired()])
    numContactUrg3  = StringField('Numero à contacter Urgence 3')

class AutorStage_MineurForm(FlaskForm):
    autorAudioPrive = BooleanField('à effectuer un enregistrement audio de celui-ci dans le cadre du stage de l\'ensemble de clarinettes 2017.')
    autorAudioPub   = BooleanField('de cet enregistrement audio sur le site Quatuor de clarinettes DIVERTIMENTO (adresse du site) en partie publique')
    autorImag       = BooleanField('à effectuer des photographies et un enregistrement vidéo de celui-ci dans le cadre du stage de l\'ensemble de clarinettes 2017.')
    autorImagSite   = BooleanField('de ces photographies et vidéos sur le site Quatuor de clarinettes DIVERTIMENTO (adresse du site) en partie membres (accès privé par mot de passe)')

class CreateAccountForm(FlaskForm):
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired(), Length(min = 7, max = 30)])
    mdp             = PasswordField('Mot de passe', validators=[DataRequired(), Length(min = 7, max = 30)])
    mdpConfirm      = PasswordField('Confirmation Mot de passe', validators=[DataRequired()])

class ConnectForm(FlaskForm):
    next            = HiddenField()
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password        = PasswordField('Mot de passe', validators=[DataRequired()])

    def get_user(self):
        user = get_user(self.username.data)
        if user is None:
            print("USER ING GETTER " + str(user))
            return None
        return user if crypt(self.password.data) == user.mdpUt else None

class OubliMdpForm(FlaskForm):
    mail            = StringField('Adresse mail', validators=[DataRequired()])

class ModifMdPOubliForm():
    mdpNew          = PasswordField('Nouvau Mot de passe ', validators=[DataRequired()])
    mdpNewConfirm   = PasswordField('Confirmation nouveau Mot de passe actuel', validators=[DataRequired()])

class ModifMdPForm(FlaskForm):
    mdpActu         = PasswordField('Mot de passe actuel', validators=[DataRequired()])
    mdpNew          = PasswordField('Nouvau Mot de passe ', validators=[DataRequired()])
    mdpNewConfirm   = PasswordField('Confirmation nouveau Mot de passe actuel', validators=[DataRequired()])

class StageForm(FlaskForm):
    repSt       = SelectField('Repertoire du stage', choices=[("1", "TEST")], validators=[Optional()])
    intituleSt  = StringField('Intitule du stage', validators=[DataRequired()])
    adresseSt   = StringField('Adresse du stage', validators=[Optional()])
    cpSt        = StringField('Code Postal du stage', validators=[Optional()])
    villeSt     = StringField('Ville du stage', validators=[Optional()])
    nbPlaceSt   = IntegerField('Nombre de places dispos', validators=[Optional()])
    dateDebSt   = DateField('Date de début du stage', validators=[Optional()])
    dateFinSt   = DateField('Date de fin du stage', validators=[Optional()])
    tenueSt     = StringField('Tenue exigée pour le concert du stage', validators=[Optional()])
    prixSt      = FloatField('Prix du stage', validators=[Optional()])
    descSt      = TextField('Description du stage', validators=[Optional()])
    nivRequisSt = IntegerField('Niveau minimum pour intégrer le stage', validators=[Optional()])

class SouvenirsForm(FlaskForm):
    anneeSouv   = SelectField("Choix de l'année", choices=[('2015', "Année 2015"), ('2016', "Année 2016"), ('2017', "Année 2017")], validators=[DataRequired()])

class ArticleForm(FlaskForm):
    idArt       = HiddenField('idArt')
    titreArt    = StringField('Titre de l\'article', validators=[DataRequired()])
    contenuArt  = TextField('Contenu de l\'article', validators=[DataRequired()])
    mediaArt    = TextField('Médias liés à l\'article', choices=[], validators=[DataRequired()])
