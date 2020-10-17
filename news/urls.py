from django.urls import path
from . import views

urlpatterns = [
    path('', views.noticia_list, name='noticia_list'),
    path('noticia/<int:pk>/', views.noticia_detail, name='noticia_detail'),
    path('noticia/new/', views.noticia_new, name='noticia_new'),
    path('noticia/<int:pk>/edit', views.noticia_edit, name='noticia_edit'),
]