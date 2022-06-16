from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AbsencesForm(ModelForm):
    class Meta:
        model = models.Absences
        fields = ('etudiant','cours','justification','justifie',)
        labels = {
            'etudiant': _('etudiant'),
            'cours': _('cours'),
            'justification': _('justification'),
            'justifie': _('justifie'),
        }

class EtudiantsForm(ModelForm):
    class Meta:
        model = models.Etudiants
        fields = ('nom','prenom','email','photo','groupes',)
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'email': _('Email'),
            'photo': _('Photo'),
            'groupes': _('Groupes')
        }

class GroupesEtudiantForm(ModelForm):
    class Meta:
        model = models.GroupesEtudiant
        fields = ('nom',)
        labels = {
            'nom': _('Nom')
        }
class EnseignantsForm(ModelForm):
    class Meta:
        model = models.Enseignants
        fields = ('nom','prenom','email')
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'email': _('Email'),
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre_cours','date','enseignant','durée','groupe',)
        labels = {
            'titre_cours': _('Titre_cours'),
            'date': _('Date'),
            'enseignant': _('Enseignant'),
            'durée': _('Durée'),
            'groupe': _('Groupe'),

        }
