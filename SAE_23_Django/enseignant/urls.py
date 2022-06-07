from django.urls import path
from . import views

urlpatterns = [
    path('enseignant/', views.enseignant),

]