from django.db import models
from django.db.models.deletion import CASCADE
from django.urls import reverse

# Create your models here.

DRINKS = (
    ('T', 'Tea'),
    ('C', 'Coffee'),
    ('W', 'Water'),
)


class Cake(models.Model):
    name = models.CharField(max_length=20)
    cal = models.IntegerField()
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'cake_id': self.id})

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
        ordering = ['-date']



