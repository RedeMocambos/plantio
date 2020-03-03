from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import FamiliaViewSet

router = DefaultRouter()
router.register('', FamiliaViewSet, basename='familias')

urlpatterns = [
    url(r'^', include(router.urls))
]
