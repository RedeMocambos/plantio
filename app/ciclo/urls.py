from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import FaseViewSet, CicloViewSet

router = DefaultRouter()
router.register(r'fase', FaseViewSet, basename='fase')
router.register(r'ciclo', CicloViewSet, basename='ciclo')

urlpatterns = [
    url(r'^', include(router.urls))
]
