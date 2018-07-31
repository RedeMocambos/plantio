from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import ManejoViewSet

router = DefaultRouter()
router.register('', ManejoViewSet, base_name='manejos')

urlpatterns = [
    url(r'^', include(router.urls))
]
