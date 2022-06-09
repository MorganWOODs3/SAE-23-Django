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
from. forms import AbsenceForm
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

