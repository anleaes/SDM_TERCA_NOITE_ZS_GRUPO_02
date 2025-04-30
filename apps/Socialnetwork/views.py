from rest_framework import viewsets
from clients.models import Client, SocialNetwork
from clients.serializer import ClientSerializer
from socialnetwork.serializer import SocialnetworkSerializer

# ViewSet para o modelo Client
class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()  # Consulta todos os clientes
    serializer_class = ClientSerializer  # Usando o serializer de Client

# ViewSet para o modelo SocialNetwork
class SocialNetworkViewSet(viewsets.ModelViewSet):
    queryset = SocialNetwork.objects.all()  # Consulta todas as redes sociais
    serializer_class = SocialnetworkSerializer  
