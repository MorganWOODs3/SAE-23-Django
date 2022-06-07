from django.shortcuts import render

# Create your views here.
def cours(request):
    return render(request, "cours/cours.html")
