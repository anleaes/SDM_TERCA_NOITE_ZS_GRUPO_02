from django.db import models

class Client(models.Model):
    name = models.CharField('Nome', max_length=50)
    description = models.TextField('Descrição', max_length=100) 
    
class Meta:
        verbose_name = 'Rede Social'
        verbose_name_plural = 'Redes Sociais'
        ordering =['id']

def __str__(self):
    return self.name
