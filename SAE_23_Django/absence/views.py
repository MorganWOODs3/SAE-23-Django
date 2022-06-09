from django.shortcuts import render

# Create your views here.

def absence(request):
    return render(request, "absence/absence.html")
def cours(request):
    return render(request, "cours/index_cours.html")
def enseignant(request):
    return render(request, "enseignant/affiche_enseignant.html")
def etudiant(request):
    return render(request, "etudiant/affiche_etudiant.html")
def groupetu(request):
    return render(request, "groupetu/affiche_groupetu.html")

def affiche_cours(request):
    return render(request, "cours/affiche_cours.html")

#################################################################

from django.shortcuts import render, HttpResponseRedirect
from. forms import AbsenceForm, CoursForm, EtudiantForm, EnseignantForm, GroupetuForm

from . import models

# Create your views here.
def ajout(request):
    if request.method == "POST":
        form = AbsenceForm(request)
        return render(request, "absence/ajout.html", {"form": form})
    else :
        form = AbsenceForm()
        return render(request, "absence/ajout.html", {"form": form})

def revu(request):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        absence = lform.save()
        return HttpResponseRedirect("/absence/index")
    else :
        return render(request, "absence/ajout.html", {"form": lform})

def centre(request):
    liste = list(models.Absence.objects.all())
    return render(request, "absence/centre.html", {"liste": liste})
def index(request):
    liste = list(models.Absence.objects.all())
    return render(request, "absence/index.html", {"liste": liste})

def affiche(request, id):
    absence = models.Absence.objects.get( pk = id)
    return render(request, "absence/affiche_groupetu.html", {"absence": absence})

def update(request, id):
    absence = models.Absence.objects.get(pk=id)
    form = AbsenceForm(absence.dico())
    return render(request,"absence/ajout.html", {"form": form, "id": id})

def updaterevu(request, id):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        absence = lform.save(commit = False)
        absence.id = id
        absence.save()
        return HttpResponseRedirect("/absence/index")
    else:
        return render(request, "absence/ajout.html", {"form": lform, "id": id})

def delete(request, id):
    absence = models.Absence.objects.get(pk=id)
    absence.delete()
    return HttpResponseRedirect("/absence/index")

##############################################################################
def ajout_cours(request):
    if request.method == "POST":
        form = CoursForm(request)
        return render(request, "cours/ajout_cours.html", {"form": form})
    else :
        form = CoursForm()
        return render(request, "cours/ajout_cours.html", {"form": form})

def affiche_cours(request, id):
    cours = models.Cours.objects.get( pk = id)
    return render(request, "cours/affiche_cours.html", {"absence": absence})

def index_cours(request):
    liste = list(models.Cours.objects.all())
    return render(request, "cours/index_cours.html", {"liste": liste})

def update_cours(request, id):
    cours = models.Cours.objects.get(pk=id)
    form = CoursForm(cours.dico())
    return render(request,"cours/ajout_cours.html", {"form": form, "id": id})

def updaterevu_cours(request, id):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        cours = lform.save(commit = False)
        cours.id = id
        cours.save()
        return HttpResponseRedirect("cours/index_cours.html")
    else:
        return render(request, "cours/ajout_cours.html", {"form": lform, "id": id})

def delete_cours(request, id):
    cours = models.Cours.objects.get(pk=id)
    cours.delete()
    return HttpResponseRedirect("cours/index_cours.html")


#############################################################################
def ajout_enseignant(request):
    if request.method == "POST":
        form = EnseignantForm(request)
        return render(request, "enseignant/ajout_enseignant.html", {"form": form})
    else:
        form = EnseignantForm()
        return render(request, "enseignant/ajout_enseignant.html", {"form": form})


def affiche_enseignant(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    return render(request, "enseignant/affiche_enseignant.html", {"absence": absence})


def index_enseignant(request):
    liste = list(models.Enseignant.objects.all())
    return render(request, "enseignant/index_enseignant.html", {"liste": liste})

def update_enseignant(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    form = EnseignantForm(enseignant.dico())
    return render(request,"enseignant/ajout_enseignant.html", {"form": form, "id": id})

def updaterevu_enseignant(request, id):
    lform = EnseignantForm(request.POST)
    if lform.is_valid():
        enseignant = lform.save(commit = False)
        enseignant.id = id
        enseignant.save()
        return HttpResponseRedirect("enseignant/index_enseignant.html")
    else:
        return render(request, "enseignant/ajout_enseignant.html", {"form": lform, "id": id})

def delete_enseignant(request, id):
    enseignant = models.Enseignant.objects.get(pk=id)
    enseignant.delete()
    return HttpResponseRedirect("enseignant/index_enseignant.html")


###############################################################################
def ajout_etudiant(request):
    if request.method == "POST":
        form = EtudiantForm(request)
        return render(request, "etudiant/ajout_etudiant.html", {"form": form})
    else:
        form = EtudiantForm()
        return render(request, "etudiant/ajout_etudiant.html", {"form": form})


def affiche_etudiant(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    return render(request, "etudiant/affiche_etudiant.html", {"absence": absence})


def index_etudiant(request):
    liste = list(models.Etudiant.objects.all())
    return render(request, "etudiant/index_etudiant.html", {"liste": liste})

def update_etudiant(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    form = EtudiantForm(etudiant.dico())
    return render(request,"etudiant/ajout_etudiant.html", {"form": form, "id": id})

def updaterevu_etudiant(request, id):
    lform = EtudiantForm(request.POST)
    if lform.is_valid():
        etudiant = lform.save(commit = False)
        etudiant.id = id
        etudiant.save()
        return HttpResponseRedirect("etudiant/index_etudiant.html")
    else:
        return render(request, "etudiant/ajout_etudiant.html", {"form": lform, "id": id})

def delete_etudiant(request, id):
    etudiant = models.Etudiant.objects.get(pk=id)
    etudiant.delete()
    return HttpResponseRedirect("etudiant/index_etudiant.html")

##############################################################################


def ajout_groupetu(request):
    if request.method == "POST":
        form = GroupetuForm(request)
        return render(request, "groupetu/ajout_groupetu.html", {"form": form})
    else:
        form = GroupetuForm()
        return render(request, "groupetu/ajout_groupetu.html", {"form": form})


def affiche_groupetu(request, id):
    groupetu = models.Groupetu.objects.get(pk=id)
    return render(request, "groupetu/affiche_groupetu.html", {"absence": absence})


def index_groupetu(request):
    liste = list(models.Groupetu.objects.all())
    return render(request, "groupetu/index_groupetu.html", {"liste": liste})

def update_groupetu(request, id):
    groupetu = models.Groupetu.objects.get(pk=id)
    form = GroupetuForm(groupetu.dico())
    return render(request,"groupetu/ajout_groupetu.html", {"form": form, "id": id})

def updaterevu_groupetu(request, id):
    lform = GroupetuForm(request.POST)
    if lform.is_valid():
        groupetu = lform.save(commit = False)
        groupetu.id = id
        groupetu.save()
        return HttpResponseRedirect("groupetu/index_groupetu.html")
    else:
        return render(request, "groupetu/ajout_groupetu.html", {"form": lform, "id": id})

def delete_groupetu(request, id):
    groupetu = models.Groupetu.objects.get(pk=id)
    groupetu.delete()
    return HttpResponseRedirect("groupetu/index_groupetu.html")

