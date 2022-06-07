from django.shortcuts import render

# Create your views here.
def enseignant(request):
    return render(request, "enseignant/enseignant.html")
