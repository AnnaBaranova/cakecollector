from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
     path('about/', views.about, name='about'),
     path('cakes/', views.cakes_index, name='index'),
     path('cakes/<int:cake_id>/', views.cake_detail, name='detail'),
     path('cakes/create/', views.CakeCreate.as_view(), name='cakes_create'),
]