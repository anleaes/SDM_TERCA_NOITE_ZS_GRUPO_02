from django.shortcuts import render
from .models import ClientSocialnetwork
from rest_framework import viewsets
from .serializer import ClientSocialNetworkSerializer

class ClientSocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = ClientSocialnetwork.objects.all()
    serializer_class = ClientSocialNetworkSerializer  