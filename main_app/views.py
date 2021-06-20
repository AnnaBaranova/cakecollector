from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Cake, Topping
from .forms import ComboForm

# Create your views here.

from django.http import HttpResponse

from main_app import models


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cakes_index(request):
  cakes = Cake.objects.all()
  return render(request, 'cakes/index.html', {'cakes': cakes})

def cake_detail(request, cake_id):
  cake = Cake.objects.get(id=cake_id)
  combo_form = ComboForm()
  return render(request, 'cakes/detail.html', { 
    'cake': cake, "combo_form": combo_form
     })

class CakeCreate(CreateView):
  model = Cake
  fields = '__all__'
  success_url = '/cakes/'


class CakeUpdate(UpdateView):
  model = Cake
  fields = '__all__'

class CakeDelete(DeleteView):
  model = Cake
  success_url = '/cakes/'

def add_combo(request, cake_id):
  form = ComboForm(request.POST)
  if form.is_valid():
    new_combo = form.save(commit=False)
    new_combo.cake_id = cake_id
    new_combo.save()
  return redirect('detail', cake_id=cake_id)

class ToppingList(ListView):
    model = Topping

class ToppingDetail(DetailView):
    model = Topping

class ToppingCreate(CreateView):
    model = Topping
    fields = '__all__'