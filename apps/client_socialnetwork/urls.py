from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'clientes_socialnetworks'

router = routers.DefaultRouter()
router.register('', views.ClientSocialNetworkViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls) )
]