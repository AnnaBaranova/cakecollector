from django.contrib import admin
from .models import Cake, Combo, Topping, Photo
# Register your models here.

admin.site.register(Cake)
admin.site.register(Combo)
admin.site.register(Topping)
admin.site.register(Photo)

