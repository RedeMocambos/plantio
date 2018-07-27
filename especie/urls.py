from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import EspecieViewSet

router = DefaultRouter()
router.register('', EspecieViewSet, base_name='especies')

urlpatterns = [
    url(r'^', include(router.urls))
]
