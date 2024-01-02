from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Machine


class MachineAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.machine_data = {
            'name': 'Test Machine',
            'inventory_number': '12345',
            'location': 'Test Location',
            'description': 'Test Description'
        }
        self.machine = Machine.objects.create(**self.machine_data)
        self.machine_url = reverse('machine-detail', args=[self.machine.id])

    def test_machine_list_create(self):
        url = reverse('machine-list-create')
        response = self.client.post(url, data=self.machine_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Machine.objects.count(), 1)

        response = self.client.post(url, data={
            'name': 'Another Test Machine',
            'inventory_number': '54321',
            'location': 'Test Location',
            'description': 'Test Description'
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Machine.objects.count(), 2)

    def test_machine_detail(self):
        response = self.client.get(self.machine_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('machine_details', response.data)

    def test_machine_delete(self):
        response = self.client.delete(self.machine_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Machine.objects.count(), 0)

    def test_machine_equipments_list(self):
        equipment_url = reverse('machine-equipments', args=[self.machine.id])

        response = self.client.get(equipment_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_duplicate_inventory_number(self):
        duplicate_machine_data = {
            'name': 'Duplicate Machine',
            'inventory_number': '12345',
            'location': 'Test Location',
            'description': 'Test Description'
        }
        url = reverse('machine-list-create')
        response = self.client.post(url, data=duplicate_machine_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Machine.objects.count(), 1)
