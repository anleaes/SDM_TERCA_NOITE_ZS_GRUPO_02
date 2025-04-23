from django.db import models
from categories.models import Category

class Product(models.Model):
    total_price = models.DecimalField('Preço Total', max_length=50)
    status = models.BooleanField('Status', max_length=100)
    client = models.ClientField()
    

class Meta:
        verbose_name = 'Ordem'
        verbose_name_plural = 'Ordens'
        ordering =['id']

def __str__(self):
    return self.name