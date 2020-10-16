from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia_list, name='noticia_list'),

]