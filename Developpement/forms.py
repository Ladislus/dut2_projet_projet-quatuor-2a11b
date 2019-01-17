from .models import *
from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, FieldList, FileField, FloatField, FormField, HiddenField, IntegerField, MultipleFileField, PasswordField, SelectField, SelectMultipleField, StringField, TextField
from wtforms.validators import DataRequired

class PersonForm(FlaskForm):
    nomPers         = StringField('Nom', validators=[DataRequired()])
    prenomPers      = StringField('Prénom', validators=[DataRequired()])
    dateNPers       = DateField('Date de naissance', validators=[DataRequired()])
    tel1Pers        = StringField('Téléphone principal', validators=[DataRequired()])
    mailPers        = StringField('Adresse Mail', validators=[DataRequired()])
    clarJouees      = SelectMultipleField('Clarinette jouée', choices=[], validators=[DataRequired()])
    niveau          = IntegerField('Année d\'experience', validators=[DataRequired()])
    ecole           = StringField('Ecole', validators=[DataRequired()])
    typePratique    = StringField('Type de pratique')

class LieuForm(FlaskForm):
    adrLieu         = StringField('Adresse du Lieu', validators=[DataRequired()])
    CPLieu          = IntegerField('Code Postal du Lieu', validators=[DataRequired()])
    villeLieu       = StringField('Ville du Lieu', validators=[DataRequired()])


class RespLegalForm(FlaskForm):
    nomResp         = StringField('Nom du Responsable', validators=[DataRequired()])
    prenomResp      = StringField('Prénom du Responsable', validators=[DataRequired()])
    telPers         = StringField('Téléphone personnel', validators=[DataRequired()])
    telTrav         = StringField('Téléphone travail')
    mailPers        = StringField('Adresse Mail Personnelle', validators=[DataRequired()])
    mailTrav        = StringField('Adresse Mail de Travail')

class User_ContactForm(FlaskForm):
    nomAuteur       = StringField('Nom Auteur mail', validators=[DataRequired()])
    prenomAuteur    = StringField('Prénom Auteur mail', validators=[DataRequired()])
    mailAuteur      = StringField('Mail Auteur', validators=[DataRequired()])
    objetMessage    = SelectField('Objet', choices=[], validators=[DataRequired()])
    contenuMessage  = TextField('Contenu message', validators=[DataRequired()])
    pjMessage       = MultipleFileField(u'Image File')

class Admin_ContactForm(FlaskForm):
    objetMessage    = SelectField('Objet', choices=[('admin', "Adminstratif"), ('music', "Musical"), ('ques', "Question")], validators=[DataRequired()])
    destMessage     = SelectMultipleField('Destinataire', choices=[('dest1', "dest1"),('dest2', "dest2")], validators=[DataRequired()])
    contenuMessage  = TextField('Contenu message', validators=[DataRequired()])
    pjMessage       = MultipleFileField(u'Image File')

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
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    mail            = StringField('Adresse mail', validators=[DataRequired()])
    confirmMail     = StringField('Confirmation Adresse Mail', validators=[DataRequired()])
    mdp             = PasswordField('Mot de passe', validators=[DataRequired()])
    mdpConfirm      = PasswordField('Confirmation Mot de passe', validators=[DataRequired()])

class ConnectForm(FlaskForm):
    next            = HiddenField()
    username        = StringField('Nom d\'utilisateur', validators=[DataRequired()])
    password        = PasswordField('Mot de passe', validators=[DataRequired()])

    def get_authentificated_user(self):
        user = get_user(self.username.data)
        if user is None:
            return None
        passwd = crypt(self.password.data)
        return user if passwd == user.password else None

class OubliMdpForm(FlaskForm):
    mail            = StringField('Adresse mail', validators=[DataRequired()])

class ModifMdPOubliForm():
    mdpNew          = HiddenField('Nouvau Mot de passe ', validators=[DataRequired()])
    mdpNewConfirm   = HiddenField('Confirmation nouveau Mot de passe actuel', validators=[DataRequired()])

class ModifMdPForm(FlaskForm):
    mdpActu         = HiddenField('Mot de passe actuel', validators=[DataRequired()])
    mdpNew          = HiddenField('Nouvau Mot de passe ', validators=[DataRequired()])
    mdpNewConfirm   = HiddenField('Confirmation nouveau Mot de passe actuel', validators=[DataRequired()])

class StageForm(FlaskForm):
    idSt        = HiddenField('idSt')
    repSt       = SelectField('Repertoire du stage', choices=[], validators=[DataRequired()])
    intituleSt  = StringField('Intitule du stage', validators=[DataRequired()])
    adresseSt   = StringField('Adresse du stage', validators=[DataRequired()])
    cpSt        = StringField('Code Postal du stage', validators=[DataRequired()])
    villeSt     = StringField('Ville du stage', validators=[DataRequired()])
    nbPlaceSt   = IntegerField('Nombre de places dispos', validators=[DataRequired()])
    dateDebSt   = DateField('Date de début du stage', validators=[DataRequired()])
    dateFinSt   = DateField('Date de fin du stage', validators=[DataRequired()])
    tenueSt     = StringField('Tenue exigée pour le concert du stage')
    prixSt      = FloatField('Prix du stage')
    descSt      = TextField('Description du stage', validators=[DataRequired()])
    nivRequisSt = IntegerField('Niveau minimum pour intégrer le stage')

class SouvenirsForm(FlaskForm):
    anneeSouv   = SelectField("Choix de l'année", choices=[('2015', "Année 2015"), ('2016', "Année 2016"), ('2017', "Année 2017")], validators=[DataRequired()])
