from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User


# Create your models here.

DRINKS = (
    ('T', 'Tea'),
    ('C', 'Coffee'),
    ('W', 'Water'),
)

class Topping(models.Model):
    name = models.CharField(max_length=20)
    portion = models.IntegerField()

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('toppings_detail', kwargs={'pk': self.id})

class Cake(models.Model):
    name = models.CharField(max_length=20)
    cal = models.IntegerField()
    description = models.TextField(max_length=100)
    toppings = models.ManyToManyField(Topping)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cake_id': self.id})
    
    def combo_for_today(self):
        return self.combo_set.filter(date=date.today()).count() >= len(DRINKS)

class Combo(models.Model):
    date = models.DateField('Order date')
    drink = models.CharField(
        max_length=1,
        choices=DRINKS,
        default=DRINKS[2][0]
    )
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_drink_display()} on {self.date}"


    class Meta:
        ordering = ['date']

class Photo(models.Model):
    url = models.CharField(max_length=200)
    cake = models.ForeignKey(Cake, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for cake_id: {self.cake_id} @{self.url}"

