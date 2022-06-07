from django.urls import path
from . import views

urlpatterns = [
    path('etudiant/', views.etudiant),

]