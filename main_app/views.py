from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

class Cake:  
  def __init__(self, name, cal, description):
    self.name = name
    self.cal = cal
    self.description = description

cakes = [
  Cake ('LemonBomb', 400, 'lemon taste'),
  Cake ('Macarrone', 350, 'crazy natty'),
  Cake ('Heaven', 450, 'berries and cheese')
]


def home(request):
  return HttpResponse('<h1>Hello, Cake Lover!</h1>')

def about(request):
    return render(request, 'about.html')

def cakes_index(request):
    return render(request, 'cakes/index.html', {'cakes': cakes})
