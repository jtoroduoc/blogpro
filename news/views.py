from django.shortcuts import render
from .models import Noticia
from django.utils import timezone

# Create your views here.

def noticia_list(request):
    noticias = Noticia.objects.all()
    return render(request, 'news/noticia_list.html', {'noticias': noticias})
