from .models import ClientSocialnetwork
from rest_framework import serializers

class ClientSocialNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClientSocialnetwork
        fields = '__all__'
        