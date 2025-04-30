from django.db import models
from clients.models import Client
from socialnetwork.models import SocialNetwork

class ClientSocialnetwork(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    socialnetwork = models.ForeignKey(SocialNetwork, on_delete=models.CASCADE)

class Meta:
    verbose_name = 'Redes Social do Cliente'
    verbose_name_plural = 'Redes Social do Cliente'
    ordering =['id']

def __str__(self):
    return self.socialnetwork.name 
