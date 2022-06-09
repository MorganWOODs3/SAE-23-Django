from django.db import models

# Create your models here.
cat = [
    ('Justifié', 'Justifié'),
    ('Non Justifié', 'Non Justifié'),
]

class Absence(models.Model):
    etudiant = models.CharField(max_length=100)
    cours = models.CharField(max_length=100)
    cat = models.CharField(max_length=30, choices=cat)
    just = models.CharField(max_length=100)





    def __str__(self):
        chaine = f"l'étudiant: {self.etudiant} dans le ou les cours de : {self.cours}, l'absence est :{self.cat}, la " \
                 f"justification est {self.just}. "
        return chaine

    def dico(self):
        return {"etudiant" : self.etudiant, "cours" : self.cours,"cat" : self.cat,"just" : self.just}

