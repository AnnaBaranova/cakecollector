from django.db import models
from django.urls import reverse

# Create your models here.

class Cake(models.Model):
    name = models.CharField(max_length=20)
    cal = models.IntegerField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cake_id': self.id})







