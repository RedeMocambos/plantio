from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import AreaViewSet, LocalidadeViewSet

router = DefaultRouter()
router.register(u'localidade/:id/areas', LocalidadeViewSet, basename='lista_areas')
router.register(u'localidade', LocalidadeViewSet, basename='localidades')
router.register(u'areas', AreaViewSet, basename='areas')

urlpatterns = [
    url(r'^', include(router.urls))
]
