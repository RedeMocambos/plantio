from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import ManejoViewSet,PadroesPlantioViewSet

router = DefaultRouter()
router.register(
    r'manejo',
    ManejoViewSet,
    base_name='manejos'
)

router.register(
    r'padroes',
    PadroesPlantioViewSet,
    base_name='padroes-plantios')

urlpatterns = [
    url(r'^', include(router.urls))
]
