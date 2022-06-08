from django.urls import path
from . import views

urlpatterns = [
    path('absence/', views.absence),
    path("revu/",views.revu),
    path("ajout/",views.ajout),
    path("index",views.index),
    path("",views.centre),
    path("affiche/<int:id>/", views.affiche),
    path("update/<int:id>/",views.update),
    path("updaterevu/<int:id>/", views.updaterevu),
    path("delete/<int:id>/",views.delete),
]
