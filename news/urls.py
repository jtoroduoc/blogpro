from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia_list, name='noticia_list'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),
]