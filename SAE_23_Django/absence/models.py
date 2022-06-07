from django.db import models

# Create your models here.
cat = [
    ('Action', 'Action'),
    ('Animation', 'Animation'),
    ('Aventure', 'Aventure'),
    ('Horreur', 'Horreur'),
    ('Fantastique', 'Fantastique'),
    ('Science Fiction', 'Science Fiction'),
    ('Guerre', 'Guerre'),
]

class Absence(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.CharField(max_length=100)
    date_parution = models.DateField(blank=True, null=True)
    dure = models.IntegerField(blank=False)
    cat = models.CharField(max_length=30, choices=cat)
    resume = models.TextField(null=True, blank=True)
    imaurl = models.URLField(max_length=300)



    def __str__(self):
        chaine = f"Titre: {self.titre} écrit par {self.realisateur}, dans la catégorie{self.cat} et avec une durée de {self.dure} minutes. Édité le {self.date_parution} et voici le résumer {self.resume}."
        return chaine

    def dico(self):
        return {"titre" : self.titre, "realisateur" : self.realisateur, "date_parution" : self.date_parution, "dure" : self.dure, "resume" : self.resume, "cat" : self.cat}

