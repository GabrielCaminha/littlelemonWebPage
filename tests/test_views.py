from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import MenuItem

class MenuViewTest(TestCase):
    def setUp(self):
        # Configuração inicial do cliente e criação de objetos
        self.client = APIClient()
        self.menu_item_1 = MenuItem.objects.create(
            title="Item 1", price=10.99, inventory=5
        )
        self.menu_item_2 = MenuItem.objects.create(
            title="Item 2", price=15.99, inventory=3
        )
        self.url = reverse('menu-items')  # Nome registrado na URL

    def test_getall(self):
        # Faz uma requisição GET para recuperar todos os itens do menu
        response = self.client.get(self.url)

        # Testa se a requisição foi bem-sucedida
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Testa se os dados retornados estão corretos
        menu_items = response.json()
        self.assertEqual(len(menu_items), 2)
        self.assertEqual(menu_items[0]['title'], self.menu_item_1.title)
        self.assertEqual(menu_items[1]['title'], self.menu_item_2.title)
