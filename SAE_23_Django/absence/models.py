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


group = [
    ('RT111', 'RT111'),
    ('RT112', 'RT112'),
    ('RT121', 'RT122'),
    ('RT131', 'RT132'),
]

class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    group = models.CharField(max_length=30, choices=group)
    photo = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"l'étudiant: {self.nom} {self.prenom} l'mail est :{self.email}, dans le groupe {self.group}"
        return chaine

    def dico(self):
        return {"nom" : self.nom, "prenom" : self.prenom,"email" : self.email,"group" : self.group},{"photo" : self.photo}



class Groupetu(models.Model):
    groupe = models.CharField(max_length=100)
    def __str__(self):
        chaine = f"{self.groupe}"
        return chaine
    def dico(self):
        return {"classe": self.groupe}


class Enseignant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)


    def __str__(self):
        chaine = f"l'enseignant: {self.nom} {self.prenom} l'mail est :{self.email}"
        return chaine

    def dico(self):
        return {"nom": self.nom, "prenom": self.prenom, "email": self.email}

class Cours(models.Model):
    titre = models.CharField(max_length=100)
    date = models.DateField(blank=True, null=True)
    duree = models.IntegerField(blank=False)
    enseignant = models.CharField(max_length=100)
    group = models.CharField(max_length=30, choices=group)



    def __str__(self):
        chaine = f"titre du cours: {self.titre}le {self.date} d'une duree de {self.duree}, dans le groupe {self.group}"
        return chaine

    def dico(self):
        return {"titre" : self.titre, "date" : self.date,"duree" : self.duree,"classe" : self.group , "enseignant" : self.enseignant}
