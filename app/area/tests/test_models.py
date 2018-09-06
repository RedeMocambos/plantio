from django.test import TestCase
from area.models import Area

class AreaTestCase(TestCase):
    def setUp(self):
        Area.objects.create(nome='Área teste 1', dimensao=1000)
        Area.objects.create(nome='Área teste 2', dimensao=5000)
    
    def test_area_criada(self):
        area1 = Area.objects.get(nome='Área teste 1')
        area2 = Area.objects.get(nome='Área teste 2')

        self.assertEqual(Area.objects.count(), 2)
        self.assertEqual(area1.dimensao, 1000)
        self.assertEqual(area2.dimensao, 5000)
        
