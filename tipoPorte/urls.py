from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import FaseViewSet, CicloViewSet

router = DefaultRouter()
router.register(r'fase', FaseViewSet, base_name='fase')
router.register(r'ciclo', CicloViewSet, base_name='ciclo')

urlpatterns = [
    url(r'^', include(router.urls))
]
