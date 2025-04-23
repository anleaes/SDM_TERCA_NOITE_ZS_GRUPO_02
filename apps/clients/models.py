from django.db import models

class Client(models.Model):
    adress = models.CharField('Endereço', max_length=100)
    cell_phone = models.TextField('Telefone', max_length=50)
    email = models.EmailField('Email', max_length=50) 
    gender = models.Choices('Gênero', choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro')
    ], default='O')
    

class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering =['id']

def __str__(self):
    return self.name
