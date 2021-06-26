from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
import uuid
import boto3
import sys
from .models import Cake, Topping, Photo
from .forms import ComboForm
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


S3_BASE_URL = 'https://s3.us-east-1.amazonaws.com/'
BUCKET = 'annacakecollector'

# Create your views here.

from django.http import HttpResponse

from main_app import models


def home(request):
  return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

@login_required
def cakes_index(request):
  cakes = Cake.objects.filter(user=request.user)
  return render(request, 'cakes/index.html', {'cakes': cakes})

@login_required
def cake_detail(request, cake_id):
  cake = Cake.objects.get(id=cake_id)
  if cake.user == request.user:
    cake_no_toppings = Topping.objects.exclude(id__in = cake.toppings.all().values_list('id'))
    combo_form = ComboForm()
    return render(request, 'cakes/detail.html', { 
    'cake': cake, "combo_form": combo_form,
    'toppings': cake_no_toppings
     })
  redirect('/')

class CakeCreate(LoginRequiredMixin, CreateView):
  model = Cake
  fields = ['name', 'cal', 'description']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)
  

class CakeUpdate(LoginRequiredMixin, UpdateView):
  model = Cake
  fields = '__all__'

class CakeDelete(LoginRequiredMixin, DeleteView):
  model = Cake
  success_url = '/cakes/'

@login_required
def add_combo(request, cake_id):
  form = ComboForm(request.POST)
  if form.is_valid():
    new_combo = form.save(commit=False)
    new_combo.cake_id = cake_id
    new_combo.save()
  return redirect('detail', cake_id=cake_id)

class ToppingList(LoginRequiredMixin, ListView):
    model = Topping

class ToppingDetail(LoginRequiredMixin, DetailView):
    model = Topping

class ToppingCreate(LoginRequiredMixin, CreateView):
    model = Topping
    fields = '__all__'

class ToppingUpdate(LoginRequiredMixin, UpdateView):
    model = Topping
    fields = ['portion']

class ToppingDelete(LoginRequiredMixin, DeleteView):
    model = Topping
    success_url = '/toppings/'

@login_required
def assoc_topping(request, cake_id, topping_id):
  Cake.objects.get(id=cake_id).toppings.add(topping_id)
  return redirect('detail', cake_id=cake_id)

@login_required
def unassoc_topping(request, cake_id, topping_id):
  Cake.objects.get(id=cake_id).toppings.remove(topping_id)
  return redirect('detail', cake_id=cake_id)

@login_required
def add_photo(request, cake_id):
    photo_file = request.FILES.get('photo-file', None)
    if photo_file:
        s3 = boto3.client('s3')
        # need a unique "key" for S3 / needs image file extension too
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        # just in case something goes wrong
        try:
            s3.upload_fileobj(photo_file, BUCKET, key)
            # build the full url string
            url = f"{S3_BASE_URL}{BUCKET}/{key}"
            # we can assign to cat_id or cat (if you have a cat object)
            photo = Photo(url=url, cake_id=cake_id)
            photo.save()
        except Exception as e:
            print('An error occurred uploading file to S3', e)
    return redirect('detail', cake_id=cake_id)

def signup(request):
  error_message = ''
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save()
      login(request, user)
      return redirect('index')
    else:
      error_message = 'Invalid sign up - try again'
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)