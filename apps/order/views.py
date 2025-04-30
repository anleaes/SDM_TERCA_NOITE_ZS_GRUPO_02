from .models import Order
from rest_framework import viewsets
from .serializer import OrderSerializer

# Após o comentario "# Create your views here." e crie as views "SocialNetwork".

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer  