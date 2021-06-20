from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cakes/', views.cakes_index, name='index'),
    path('cakes/<int:cake_id>/', views.cake_detail, name='detail'),
    path('cakes/create/', views.CakeCreate.as_view(), name='cakes_create'),
    path('cakes/<int:pk>/update/', views.CakeUpdate.as_view(), name='cakes_update'),
    path('cakes/<int:pk>/delete/', views.CakeDelete.as_view(), name='cakes_delete'),
    path('cakes/<int:cake_id>/add_combo/', views.add_combo, name='add_combo'),
    path('toppings/', views.ToppingList.as_view(), name='toppings_index'),
    path('toppings/<int:pk>/', views.ToppingDetail.as_view(), name = 'toppings_detail'),
    path('toppings/create/', views.ToppingCreate.as_view(), name="toppings_create"),
    path('toppings/<int:pk>/update/', views.ToppingUpdate.as_view(), name='toppings_update'),
    path('toppings/<int:pk>/delete/', views.ToppingDelete.as_view(), name="toppings_delete"),
]