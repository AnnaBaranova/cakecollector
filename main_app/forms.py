from django.db import models
from django.forms import ModelForm, fields
from .models import Combo

class ComboForm(ModelForm):
    class Meta:
        model = Combo
        fields = ['date', 'drink']