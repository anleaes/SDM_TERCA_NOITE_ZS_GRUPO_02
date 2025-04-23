from django.shortcuts import render

# Create your views here.

from .models import Order, OrderItem
from rest_framework import viewsets
from .serializer import OrderItemSerializer

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer  