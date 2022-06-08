from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models

class AbsenceForm(ModelForm):
    class Meta:
        model = models.Absence
        fields = ('titre', 'realisateur', 'date_parution','dure','resume','cat','imaurl',)
        labels = {
            'titre': _('Titre'),
            'realisateur': _('Réalisateur'),
            'date_parution': _('Date de parution'),
            'dure': _('Duré du film en minutes'),
            'remume': _('Résumé'),
            'cat': _('Catégorie'),
            'imaurl': _('Image avec Url')


        }
