from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import AreaViewSet, LocalidadeViewSet

router = DefaultRouter()
router.register(u'localidade/:id/areas', LocalidadeViewSet, base_name='lista_areas')
router.register(u'localidade', LocalidadeViewSet, base_name='localidades')
router.register(u'areas', AreaViewSet, base_name='areas')

urlpatterns = [
    url(r'^', include(router.urls))
]
