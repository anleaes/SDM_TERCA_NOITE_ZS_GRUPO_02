from socialnetwork.models import SocialNetwork
from rest_framework import serializers

class SocialnetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialNetwork
        fields = '__all__'