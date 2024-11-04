# inventory/tests.py
from django.test import TestCase
from django.urls import reverse
from .models import Inventory, Supplier


class InventoryTests(TestCase):

    def setUp(self):
        supplier = Supplier.objects.create(name="Test Supplier")
        Inventory.objects.create(
            name="Test Product",
            description="Test Description",
            note="Test Note",
            stock=10,
            availability=True,
            supplier=supplier
        )

    def test_inventory_list_view(self):
        response = self.client.get(reverse('inventory_list'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_api_view(self):
        response = self.client.get(reverse('inventory_api'))
        self.assertEqual(response.status_code, 200)

    def test_inventory_detail_view(self):
        inventory = Inventory.objects.first()
        response = self.client.get(reverse('inventory_detail', args=[inventory.id]))
        self.assertEqual(response.status_code, 200)
