from django.urls import reverse
from rest_framework.test import APITestCase

from area.models import Area

class AreaAPITests(APITestCase):

    def setUp(self):
        Area.objects.get_or_create(nome='Área 1', dimensao='1000')
    
    def test_areas_list(self):
        url = reverse('areas-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        
    def test_localidades_list(self):
        url = reverse('localidades-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)

    def test_lista_areas(self):
        url = reverse('lista_areas-list')
        data = {'id': 1}
        response = self.client.get(url, data)
        self.assertEquals(response.status_code, 200)
