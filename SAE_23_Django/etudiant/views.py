from django.shortcuts import render

# Create your views here.
def etudiant(request):
    return render(request, "etudiant/etudiant.html")
