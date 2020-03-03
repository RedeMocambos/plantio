from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import PlantioViewSet

router = DefaultRouter()
router.register(u'plantios', PlantioViewSet, basename='plantios')

urlpatterns = [
    url(r'^', include(router.urls))
]
