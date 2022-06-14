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



class Etudiant(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    groupetu = models.ForeignKey("groupetu", on_delete= models.CASCADE, default=None)


    def __str__(self):
        chaine = f"l'étudiant: {self.nom} {self.prenom} l'mail est :{self.email}, dans le groupe {self.groupetu}"
        return chaine

    def dico(self):
        return {"nom" : self.nom, "prenom" : self.prenom,"email" : self.email,"groupetu" : self.groupetu,"photo": self.photo}



class Groupetu(models.Model):
    groupetu = models.CharField(max_length=100)
    def __str__(self):
        chaine = f"{self.groupetu}"
        return chaine
    def dico(self):
        return {"classe": self.groupetu}


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
    nom = models.ForeignKey("enseignant", on_delete=models.CASCADE, default=None)
    groupetu = models.ForeignKey("groupetu", on_delete=models.CASCADE, default=None)



    def __str__(self):
        chaine = f"titre du cours: {self.titre}le {self.date} d'une duree de {self.duree}, dans le groupe {self.groupetu}"
        return chaine

    def dico(self):
        return {"titre": self.titre, "date": self.date, "duree": self.duree, "classe": self.groupetu, "nom": self.nom}
