from django.test import TestCase
from rest_framework.test import APIClient
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        Menu.objects.create(title="Pizza", price=120, inventory=50)
        Menu.objects.create(title="Burger", price=70, inventory=40)

    def test_get_all_menu_items(self):
        response = self.client.get('/restaurant/menu/')
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), serializer.data)
