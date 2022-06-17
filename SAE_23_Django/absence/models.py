# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cours(models.Model):
    idcours = models.AutoField(db_column='idCours', primary_key=True)  # Field name made lowercase.
    titre_cours = models.CharField(db_column='titre cours', max_length=100, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    date = models.DateTimeField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    enseignant = models.ForeignKey('Enseignants', models.DO_NOTHING, db_column='enseignant')
    durée = models.TimeField(db_column='Durée', blank=True, null=True)  # Field name made lowercase.
    groupe = models.ForeignKey('GroupesEtudiant', models.DO_NOTHING, db_column='Groupe')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Cours'
        unique_together = (('idcours', 'groupe', 'enseignant'),)

    def __str__(self):
        chaine = f"Le cours : {self.titre_cours} le  {self.date} d'une durée de {self.durée} minutes avec l'enseignant {self.enseignant} dans le groupe {self.groupe}"
        return chaine
    def dico(self):
        return {"idcours": self.idcours,"titre_cours": self.titre_cours,"date": self.date,"durée": self.durée,"enseignant": self.enseignant,"groupe": self.groupe,}

class Enseignants(models.Model):
    idenseignants = models.AutoField(db_column='idEnseignants', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(max_length=45, blank=True, null=True)
    email = models.CharField(max_length=144, blank=True, null=True)

    class Meta:
            managed = False
            db_table = 'Enseignants'

    def __str__(self):
        chaine = f"L'Enseignants : {self.nom} {self.prenom},l'email {self.email}"
        return chaine
    def dico(self):
        return {"idenseignants": self.idenseignants,"nom": self.nom,"prenom": self.prenom,"email": self.email,}



class Etudiants(models.Model):
    idetudiants = models.AutoField(db_column='idEtudiants', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=45, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=144, blank=True, null=True)  # Field name made lowercase.
    photo = models.URLField(db_column='Photo', blank=True, null=True)  # Field name made lowercase.
    groupes = models.ForeignKey('GroupesEtudiant', models.DO_NOTHING, db_column='groupes')

    class Meta:
        managed = False
        db_table = 'Etudiants'
        unique_together = (('idetudiants', 'groupes'),)

    def dico(self):
        return {"idetudiants": self.idetudiants,"nom": self.nom,"prenom": self.prenom,"email": self.email,"photo": self.photo,"groupes": self.groupes,}

    def __str__(self):
        chaine = f"{self.prenom}{self.nom}"
        return chaine


class GroupesEtudiant(models.Model):
    idgroupes_etudiant = models.AutoField(db_column='idGroupes-etudiant', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    nom = models.CharField(db_column='Nom', max_length=45, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Groupes-etudiant'
    def dico(self):
        return {"idgroupe_etudiant": self.idgroupes_etudiant, "nom": self.nom}

    def __str__(self):
        chaine = f"{self.nom}"
        return chaine


class Absences(models.Model):
    idabsences = models.IntegerField(primary_key=True)
    etudiant = models.ForeignKey(Etudiants, models.DO_NOTHING, db_column='Etudiant')  # Field name made lowercase.
    cours = models.ForeignKey(Cours, models.DO_NOTHING, db_column='Cours')  # Field name made lowercase.
    justification = models.TextField(blank=True, null=True)
    justifie = models.CharField(max_length=7, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'absences'
        unique_together = (('idabsences', 'etudiant', 'cours'),)
    def __str__(self):
        chaine = f"L'étudiant : {self.etudiant} dans le cours {self.cours}, l'absence est {self.justification}" \
                 f"et la justification est {self.justifie}"
        return chaine
    def dico(self):
        return {"idabsences": self.idabsences, "etudiant": self.etudiant, "cours": self.cours, "justification": self.justification, "justifie": self.justifie}
