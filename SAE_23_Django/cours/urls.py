from django.urls import path
from . import views

urlpatterns = [
    path('cours/', views.cours),

]