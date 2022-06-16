from django.shortcuts import render

# Create your views here.


#################################################################

from django.shortcuts import render, HttpResponseRedirect
from. forms import AbsencesForm, CoursForm, EtudiantsForm, EnseignantsForm, GroupesEtudiantForm

from . import models

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AbsencesForm(request)
        return render(request, "absence/ajout.html", {"form": form})
    else :
        form = AbsencesForm()
        return render(request, "absence/ajout.html", {"form": form})

def revu(request):
    lform = AbsencesForm(request.POST)
    if lform.is_valid():
        absences = lform.save()
        return HttpResponseRedirect("/absence/index")
    else :
        return render(request, "absence/ajout.html", {"form": lform})

def centre(request):
    liste = list(models.Absences.objects.all())
    return render(request, "absence/centre.html", {"liste": liste})
def index(request):
    liste = list(models.Absences.objects.all())
    return render(request, "absence/index.html", {"liste": liste})

def affiche(request, idabsences):
    absences = models.Absences.objects.get( pk = idabsences)
    return render(request, "absence/affiche.html", {"absences": absences})

def update(request, idabsences):
    absences = models.Absences.objects.get(pk=idabsences)
    form = AbsencesForm(absences.dico())
    return render(request,"absence/ajout.html", {"form": form, "idabsences": idabsences})

def updaterevu(request, idabsences):
    lform = AbsencesForm(request.POST)
    if lform.is_valid():
        absences = lform.save(commit = False)
        absences.idabsences = idabsences
        absences.save()
        return HttpResponseRedirect("/absence/index")
    else:
        return render(request, "absence/ajout.html", {"form": lform, "idabsences": idabsences})

def delete(request, id):
    absences = models.Absences.objects.get(pk=id)
    absences.delete()
    return HttpResponseRedirect("/absence/index")

##############################################################################
def ajout_cours(request):
    if request.method == "POST":
        form = CoursForm(request)
        return render(request, "cours/ajout_cours.html", {"form": form})
    else :
        form = CoursForm()
        return render(request, "cours/ajout_cours.html", {"form": form})

def revu_cours(request):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        cours = lform.save()
        return HttpResponseRedirect("/cours/index_cours")
    else :
        return render(request, "cours/ajout_cours.html", {"form": lform})

def affiche_cours(request,idcours):
    cours = models.Cours.objects.get( pk=idcours)
    return render(request, "cours/affiche_cours.html", {"cours": cours})

def index_cours(request):
    liste = list(models.Cours.objects.all())
    return render(request, "cours/index_cours.html", {"liste": liste})

def update_cours(request,  idcours):
    cours = models.Cours.objects.get(pk=idcours)
    form = CoursForm(cours.dico())
    return render(request,"cours/ajout_cours.html", {"form": form, "idcours": idcours})

def updaterevu_cours(request,idcours):
    lform = CoursForm(request.POST)
    if lform.is_valid():
        cours = lform.save(commit = False)
        cours.idcours = idcours
        cours.save()
        return HttpResponseRedirect("/cours/index_cours")
    else:
        return render(request, "cours/ajout_cours.html", {"form": lform, "idcours": idcours})

def delete_cours(request,idcours):
    cours = models.Cours.objects.get(pk=idcours)
    cours.delete()
    return HttpResponseRedirect("/cours/index_cours")


#############################################################################
def ajout_enseignant(request):
    if request.method == "POST":
        form = EnseignantsForm(request)
        return render(request, "enseignant/ajout_enseignant.html", {"form": form})
    else:
        form = EnseignantsForm()
        return render(request, "enseignant/ajout_enseignant.html", {"form": form})


def affiche_enseignant(request,idenseignants):
    enseignants = models.Enseignants.objects.get(pk=idenseignants)
    return render(request, "enseignant/affiche_enseignant.html", {"enseignants": enseignants})


def index_enseignant(request):
    liste = list(models.Enseignants.objects.all())
    return render(request, "enseignant/index_enseignant.html", {"liste": liste})

def revu_enseignant(request):
    lform = EnseignantsForm(request.POST)
    if lform.is_valid():
        enseignants = lform.save()
        return HttpResponseRedirect("/enseignant/index_enseignant")
    else :
        return render(request, "enseignant/ajout_enseignant.html", {"form": lform})


def update_enseignant(request,idenseignants):
    enseignants = models.Enseignants.objects.get(pk=idenseignants)
    form = EnseignantsForm(enseignants.dico())
    return render(request,"enseignant/ajout_enseignant.html", {"form": form, "idenseignants": idenseignants})

def updaterevu_enseignant(request,idenseignants):
    lform = EnseignantsForm(request.POST)
    if lform.is_valid():
        enseignants = lform.save(commit = False)
        enseignants.idenseignants = idenseignants
        enseignants.save()
        return HttpResponseRedirect("/enseignant/index_enseignant")
    else:
        return render(request, "enseignant/ajout_enseignant.html", {"form": lform, "idenseignants": idenseignants})

def delete_enseignant(request, idenseignants):
    enseignants = models.Enseignants.objects.get(pk=idenseignants)
    enseignants.delete()
    return HttpResponseRedirect("/enseignant/index_enseignant")


###############################################################################
def ajout_etudiant(request):
    if request.method == "POST":
        form = EtudiantsForm(request)
        return render(request, "etudiant/ajout_etudiant.html", {"form": form})
    else:
        form = EtudiantsForm()
        return render(request, "etudiant/ajout_etudiant.html", {"form": form})


def affiche_etudiant(request, idetudiants):
    etudiant = models.Etudiants.objects.get(pk=idetudiants)
    return render(request, "etudiant/affiche_etudiant.html", {"etudiant": etudiant})


def index_etudiant(request):
    liste = list(models.Etudiants.objects.all())
    return render(request, "etudiant/index_etudiant.html", {"liste": liste})

def revu_etudiant(request):
    lform = EtudiantsForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save()
        return HttpResponseRedirect("/etudiant/index_etudiant")
    else :
        return render(request, "etudiant/ajout_etudiant.html", {"form": lform})



def update_etudiant(request, idetudiants):
    etudiant = models.Etudiants.objects.get(pk=idetudiants)
    form = EtudiantsForm(etudiant.dico())
    return render(request,"etudiant/ajout_etudiant.html", {"form": form, "idetudiants": idetudiants})

def updaterevu_etudiant(request,idetudiants):
    lform = EtudiantsForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save(commit = False)
        etudiant.idetudiants = idetudiants
        etudiant.save()
        return HttpResponseRedirect("/etudiant/index_etudiant")
    else:
        return render(request, "etudiant/ajout_etudiant.html", {"form": lform, "idetudiants": idetudiants})

def delete_etudiant(request, idetudiants):
    etudiant = models.Etudiants.objects.get(pk=idetudiants)
    etudiant.delete()
    return HttpResponseRedirect("/etudiant/index_etudiant")

##############################################################################


def ajout_groupetu(request):
    if request.method == "POST":
        form = GroupesEtudiantForm(request)
        return render(request, "groupetu/ajout_groupetu.html", {"form": form})
    else:
        form = GroupesEtudiantForm()
        return render(request, "groupetu/ajout_groupetu.html", {"form": form})

def index_groupetu(request):
    liste = list(models.GroupesEtudiant.objects.all())
    return render(request, "groupetu/index_groupetu.html", {"liste": liste})

def revu_groupetu(request):
    lform = GroupesEtudiantForm(request.POST)
    if lform.is_valid():
        groupetu = lform.save()
        return HttpResponseRedirect("/groupetu/index_groupetu")
    else :
        return render(request, "groupetu/ajout_groupetu.html", {"form": lform})

def update_groupetu(request,idgroupes_etudiant):
    groupetu = models.GroupesEtudiant.objects.get(pk=idgroupes_etudiant)
    form = GroupesEtudiantForm(groupetu.dico())
    return render(request,"groupetu/ajout_groupetu.html", {"form": form, "idgroupes_etudiant": idgroupes_etudiant})

def updaterevu_groupetu(request,idgroupes_etudiant):
    lform = GroupesEtudiantForm(request.POST)
    if lform.is_valid():
        groupetu = lform.save(commit = False)
        groupetu.idgroupes_etudiant = idgroupes_etudiant
        groupetu.save()
        return HttpResponseRedirect("/groupetu/ajout_groupetu")
    else:
        return render(request, "groupetu/ajout_groupetu.html", {"form": lform, "idgroupes_etudiant": idgroupes_etudiant})

def delete_groupetu(request, idgroupes_etudiant):
    groupetu = models.GroupesEtudiant.objects.get(pk=idgroupes_etudiant)
    groupetu.delete()
    return HttpResponseRedirect("/groupetu/index_groupetu")

