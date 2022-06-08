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
    imaurl = models.URLField(max_length=300)
    photo = models.FileField(upload_to ='photo')



    def __str__(self):
        chaine = f"l'étudiant: {self.etudiant} dans le ou les cours de : {self.cours}, l'absence est :{self.cat}."
        return chaine

    def dico(self):
        return {"titre" : self.etudiant, "realisateur" : self.cours,"cat" : self.cat}

