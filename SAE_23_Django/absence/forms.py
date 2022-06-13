from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AbsenceForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = ('etudiant', 'cours','cat','just',)
        labels = {
            'etudiant': _('Etudiant'),
            'cours': _('Cours'),
            'cat': _('Catégorie'),
            'just': _('Justification'),
        }

class EtudiantForm(ModelForm):
    class Meta:
        model = models.Etudiant
        fields = ('nom', 'prenom','email','group','photo',)
        labels = {
            'nom': _('Nom'),
            'Prenom': _('Prenom'),
            'Email': _('Email'),
            'Group': _('Group'),
            'Photo': _('Photo'),
        }

class GroupetuForm(ModelForm):
    class Meta:
        model = models.Groupetu
        fields = ('groupe',)
        labels = {
            'groupe': _('Groupe'),

        }
class EnseignantForm(ModelForm):
    class Meta:
        model = models.Enseignant
        fields = ('nom', 'prenom','email',)
        labels = {
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'email': _('Email'),
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('titre', 'date','duree','enseignant','group',)
        labels = {
            'titre': _('Titre'),
            'date': _('Date'),
            'duree': _('Duree'),
            'enseignant': _('Enseignant'),
            'group': _('Group'),
        }
