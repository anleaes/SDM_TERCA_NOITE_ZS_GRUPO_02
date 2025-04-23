from django.urls import path, include
from django.urls import path, include
from . import views
from rest_framework import routers

app_name = 'socialnetwork'

router = routers.DefaultRouter()
router.register('', views.ClientViewSet, basename='redessociais')

urlpatterns = [
    path('', include(router.urls) )
]