from django.shortcuts import render, get_object_or_404
from .models import Articles
from . import models


# Create your views here.
def index(request):
    art = Articles.objects.all()
    return render(request, 'home/index.html', {'art': art})


# def join_hood(request, id):
#     dynamic = Articles.objects.get(id=id)
#     return render(request, 'home/join_hood.html', {'dynamic': dynamic})

def detail_view(request, id):
    lang = get_object_or_404(models.Articles, id=id)
    return render(request, 'home/join_hood.html', {'lang': lang})
