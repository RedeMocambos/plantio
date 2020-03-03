from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import EspecieViewSet, VariedadeViewSet, InteracaoViewSet

router = DefaultRouter()
router.register(u'especie', EspecieViewSet, basename='especies')
router.register(u'variedade', VariedadeViewSet, basename='variedades')
router.register(u'interacao', InteracaoViewSet, basename='interacoes')

urlpatterns = [
    url(r'^', include(router.urls))
]
