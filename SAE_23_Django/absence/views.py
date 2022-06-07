from django.shortcuts import render

# Create your views here.

def absence(request):
    return render(request, "absence/absence.html")


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
        return HttpResponseRedirect("/SAE_23_Django/index")
    else :
        return render(request, "absence/ajout.html", {"form": lform})

def centre(request):
    liste = list(models.absence.objects.all())
    return render(request, "absence/centre.html", {"liste": liste})
def index(request):
    liste = list(models.absence.objects.all())
    return render(request, "absence/index.html", {"liste": liste})


def affiche(request, id):
    absence = models.absence.objects.get( pk = id)
    return render(request, "absence/affiche.html", {"absence": absence})

def update(request, id):
    absence = models.absence.objects.get(pk=id)
    form = AbsenceForm(film.dico())
    return render(request,"absence/ajout.html", {"form": form, "id": id})

def updaterevu(request, id):
    lform = AbsenceForm(request.POST)
    if lform.is_valid():
        absence = lform.save(commit = False)
        absence.id = id
        absence.save()
        return HttpResponseRedirect("/SAE_23_Django/index")
    else:
        return render(request, "absence/ajout.html", {"form": lform, "id": id})

def delete(request, id):
    absence = models.absence.objects.get(pk=id)
    absence.delete()
    return HttpResponseRedirect("/SAE_23_Django/index")
