from django.conf.urls import  url, include
from rest_framework.routers import DefaultRouter

from .views import EspecieViewSet, VariedadeViewSet, InteracaoViewSet

router = DefaultRouter()
router.register(u'especie', EspecieViewSet, base_name='especies')
router.register(u'variedade', VariedadeViewSet, base_name='variedades')
router.register(u'interacao', InteracaoViewSet, base_name='interacoes')

urlpatterns = [
    url(r'^', include(router.urls))
]
