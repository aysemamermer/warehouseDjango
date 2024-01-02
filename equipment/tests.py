from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Equipment, Machine


class EquipmentAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.equipment_data = {
            'name': 'Test Equipment',
            'inventory_number': 'TEST001',
        }
        self.machine = Machine.objects.create(name='Test Machine')
        self.equipment_with_machine_data = {
            'name': 'Test Equipment with Machine',
            'inventory_number': 'TEST002',
            'machine_id': self.machine.id,
        }

    def test_create_equipment(self):
        url = reverse('equipment-list-create')
        response = self.client.post(url, data=self.equipment_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipment.objects.count(), 1)
        self.assertEqual(Equipment.objects.get().name, 'Test Equipment')

    def test_create_equipment_with_machine(self):
        url = reverse('equipment-list-create')
        response = self.client.post(url, data=self.equipment_with_machine_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Equipment.objects.count(), 1)
        equipment = Equipment.objects.get()
        self.assertEqual(equipment.name, 'Test Equipment with Machine')
        self.assertEqual(equipment.machine, self.machine)

    def test_get_equipment_list(self):
        Equipment.objects.create(name='Equipment 1', inventory_number='INV001')
        Equipment.objects.create(name='Equipment 2', inventory_number='INV002')

        url = reverse('equipment-list-create')
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_equipment_detail(self):
        equipment = Equipment.objects.create(name='Test Equipment', inventory_number='TEST001')
        url = reverse('equipment-detail', args=[equipment.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Equipment')

    def test_update_equipment(self):
        equipment = Equipment.objects.create(name='Test Equipment', inventory_number='TEST001')
        url = reverse('equipment-detail', args=[equipment.id])
        updated_data = {'name': 'Updated Equipment', 'inventory_number': 'UPDATED001'}

        response = self.client.put(url, data=updated_data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        equipment.refresh_from_db()
        self.assertEqual(equipment.name, 'Updated Equipment')
        self.assertEqual(equipment.inventory_number, 'UPDATED001')

    def test_delete_equipment(self):
        equipment = Equipment.objects.create(name='Test Equipment', inventory_number='TEST001')
        url = reverse('equipment-delete', args=[equipment.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Equipment.objects.count(), 0)
