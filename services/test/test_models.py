from django.test import TestCase
from services.models import Services

class ServiceTestCase(TestCase):
    def setUp(self):
        """Crea un objeto Services para pruebas"""
        self.instance = Services.objects.create(
            title='ServiceTest',
            description='This is a description test',
            category='CategoryTest',
            duration='10 min Test',
            tags='TagsTest'
        )

    def test_instance_str(self):
        """Verifica el objeto Services se crea correctamente"""
        self.assertEqual(str(self.instance), 'ServiceTest')