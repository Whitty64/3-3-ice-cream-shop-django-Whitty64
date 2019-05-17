from django.db import models
from django.urls import reverse


# Create your models here.
class Menu(models.Model):
        VANILLA = 'Vanilla'
        CHOCOLATE = 'Chocolate'

        DAILY = 'Daily'
        WEEKLY = 'Weekly'
        SEASONAL = 'Seasonal'


        BASE = [(VANILLA, 'Vanilla'), (CHOCOLATE, 'Chocolate')]
        AVAILABLE = [(DAILY, 'Daily'), (WEEKLY, 'Weekly'), (SEASONAL, 'Seasonal')]

        flavor = models.CharField(max_length=100)
        date_churned = models.DateField()
        available = models.CharField(max_length=75, choices=AVAILABLE)
        base = models.CharField(max_length=75, choices=BASE)
        featured = models.BooleanField(default=False)
        model_pic = models.CharField(max_length=255)

        def __str__(self):
            return self.flavor[:20]

        def get_absolute_url(self):
            return reverse('home')


