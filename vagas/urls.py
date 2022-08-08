from django.urls import path
from . import views

urlpatterns = [
    path('criar_vaga', views.criar_vaga, name='criar_vaga'),
]