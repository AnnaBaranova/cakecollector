from django.shortcuts import render
from .models import Cake

# Create your views here.

from django.http import HttpResponse


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cakes_index(request):
  cakes = Cake.objects.all()
  return render(request, 'cakes/index.html', {'cakes': cakes})

def cake_detail(request, cake_id):
  cake = Cake.objects.get(id=cake_id)
  return render(request, 'cakes/detail.html', { 'cake': cake })
