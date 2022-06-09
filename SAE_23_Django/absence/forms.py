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
