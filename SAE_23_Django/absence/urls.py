from django.urls import path
from . import views

urlpatterns = [
    path('absence/', views.absence),
    path("absence/revu/",views.revu),
    path("absence/ajout/",views.ajout),
    path("absence/index",views.index),
    path("",views.centre),
    path("absence/affiche/<int:id>/", views.affiche),
    path("absence/update/<int:id>/",views.update),
    path("absence/updaterevu/<int:id>/", views.updaterevu),
    path("absence/delete/<int:id>/",views.delete),

    path('cours/', views.cours),
    path('cours/affiche_cours/', views.affiche_cours),

    path('enseignant/', views.enseignant),
    path('etudiant/', views.etudiant),
    path('groupetu/', views.groupetu),
]
