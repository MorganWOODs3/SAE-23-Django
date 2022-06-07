from django.shortcuts import render

# Create your views here.
def groupetu(request):
    return render(request, "groupetu/groupetu.html")
