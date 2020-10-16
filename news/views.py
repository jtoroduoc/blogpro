from django.shortcuts import render

# Create your views here.

def noticia_list(request):
    return render(request, 'news/noticia_list.html', {})
