from rest_framework.test import APITestCase
from rest_framework import status

class PermissionTestCase(APITestCase):
    def test_unauthorized_access(self):
        response = self.client.get("/api/services/1/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)