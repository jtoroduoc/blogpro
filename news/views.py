from django.shortcuts import render, get_object_or_404
from .models import Noticia
from django.utils import timezone

# Create your views here.

def noticia_list(request):
    noticias = Noticia.objects.filter(publicacion__lte=timezone.now()).order_by('-publicacion')
    return render(request, 'news/noticia_list.html', {'noticias': noticias})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'news/noticia_detail.html', {'noticia': noticia})