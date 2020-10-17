from django.core.exceptions import TooManyFieldsSent
from django.shortcuts import redirect, render, get_object_or_404
from .models import Noticia
from django.utils import timezone
from .forms import NoticiaForm

# Create your views here.

def noticia_list(request):
    noticias = Noticia.objects.filter(publicacion__lte=timezone.now()).order_by('-publicacion')
    return render(request, 'news/noticia_list.html', {'noticias': noticias})

def noticia_detail(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'news/noticia_detail.html', {'noticia': noticia})

def noticia_new(request):
    if request.method == "POST":
        form = NoticiaForm(request.POST)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.publicacion = timezone.now()
            noticia.save()
            return redirect('noticia_detail', pk=noticia.pk)
    else:
        form = NoticiaForm()
    return render(request, 'news/noticia_edit.html', {'form': form})


def noticia_edit(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == "POST":
        form = NoticiaForm(request.POST, instance=noticia)
        if form.is_valid():
            noticia = form.save(commit=False)
            noticia.autor = request.user
            noticia.publicacion = timezone.now()
            noticia.save()
            return redirect('noticia_detail', pk=noticia.pk)
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'news/noticia_edit.html', {'form': form})
