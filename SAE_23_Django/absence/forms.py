from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AbsencesForm(ModelForm):
    class Meta:
        model = models.Absences
        fields = ('idabsences', 'etudiant','cours','justification','justifie',)
        labels = {
            'idabsences': _('idabsences'),
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
        fields = ('idgroupes_etudiant','nom')
        labels = {
            'idgroupes_etudiant': _('idgroupes_etudiant'),
            'nom': _('Nom'),

        }
class EnseignantsForm(ModelForm):
    class Meta:
        model = models.Enseignants
        fields = ('idenseignants', 'nom','prenom','email')
        labels = {
            'idenseignants': _('Idenseignants'),
            'nom': _('Nom'),
            'prenom': _('Prenom'),
            'email': _('Email'),
        }

class CoursForm(ModelForm):
    class Meta:
        model = models.Cours
        fields = ('idcours', 'titre_cours','date','enseignant','durée','groupe',)
        labels = {
            'idcours': _('Idcours'),
            'titre_cours': _('Titre_cours'),
            'date': _('Date'),
            'enseignant': _('Enseignant'),
            'durée': _('Durée'),
            'groupe': _('Groupe'),

        }
