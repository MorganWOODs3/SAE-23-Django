from django.urls import path
from . import views

urlpatterns = [

    path("absence/revu/",views.revu),
    path("absence/ajout/",views.ajout),
    path("absence/index/",views.index),
    path("absence/centre/",views.centre),
    path("absence/affiche/<int:id>/", views.affiche),
    path("absence/update/<int:id>/",views.update),
    path("absence/updaterevu/<int:id>/", views.updaterevu),
    path("absence/delete/<int:id>/",views.delete),

    path("cours/revu_cours/",views.revu_cours),
    path('cours/affiche_cours/<int:id>/', views.affiche_cours),
    path('cours/ajout_cours/', views.ajout_cours),
    path('cours/index_cours/', views.index_cours),
    path("cours/update_cours/<int:id>/",views.update_cours),
    path("cours/updaterevu_cours/<int:id>/", views.updaterevu_cours),
    path("cours/delete_cours/<int:id>/",views.delete_cours),


    path("enseignant/revu_enseignant/",views.revu_enseignant),
    path('enseignant/affiche_enseignant/<int:id>/', views.affiche_enseignant),
    path('enseignant/ajout_enseignant/', views.ajout_enseignant),
    path('enseignant/index_enseignant/', views.index_enseignant),
    path("enseignant/update_enseignant/<int:id>/", views.update_enseignant),
    path("enseignant/updaterevu_enseignant/<int:id>/", views.updaterevu_enseignant),
    path("enseignant/delete_enseignant/<int:id>/", views.delete_enseignant),

    path("etudiant/revu_etudiant/", views.revu_etudiant),
    path('etudiant/affiche_etudiant/<int:id>/', views.affiche_etudiant),
    path('etudiant/ajout_etudiant/', views.ajout_etudiant),
    path('etudiant/index_etudiant/', views.index_etudiant),
    path("etudiant/update_etudiant/<int:id>/", views.update_etudiant),
    path("etudiant/updaterevu_etudiant/<int:id>/", views.updaterevu_etudiant),
    path("etudiant/delete_etudiant/<int:id>/", views.delete_etudiant),

    path("groupetu/revu_groupetu/", views.revu_groupetu),
    path('groupetu/affiche_groupetu/<int:id>/', views.affiche_groupetu),
    path('groupetu/ajout_groupetu/', views.ajout_groupetu),
    path('groupetu/index_groupetu/', views.index_groupetu),
    path("groupetu/update_groupetu/<int:id>/", views.update_groupetu),
    path("groupetu/updaterevu_groupetu/<int:id>/", views.updaterevu_groupetu),
    path("groupetu/delete_groupetu/<int:id>/", views.delete_groupetu),
]
