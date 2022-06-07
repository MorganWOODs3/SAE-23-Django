from django.shortcuts import render

# Create your views here.

def absence(request):
    return render(request, "absence/absence.html")
