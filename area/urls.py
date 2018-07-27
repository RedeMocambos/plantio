from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import AreaViewSet

router = DefaultRouter()
router.register('', AreaViewSet, base_name='areas')

urlpatterns = [
    url(r'^', include(router.urls))
]
