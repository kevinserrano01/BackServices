from rest_framework.test import APITestCase
from rest_framework import status
from interactions.models import Requests, Posts
from services.models import Services
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Create your tests here.
class OferenteRequestTestCase(APITestCase):
    """
    Caso de prueba para la gestión de operaciones relacionadas con solicitudes (Requests) en la API.
    Esta clase está diseñada para probar varios escenarios relacionados con solicitudes
    dentro de la API. Verifica la creación y validación de
    solicitudes enviadas por un usuario con un rol específico (buscador) a un
    proveedor.
    """
    def setUp(self):
        User = get_user_model()
        # finder (User): Un objeto usuario con el rol de 'buscador'.
        self.finder = User.objects.create_user(
            username="finder",
            password="finder123",
            email="finder@example.com",
            first_name="finder",
            last_name="finder",
            telephone="999999999",
            is_supplier=0,
            is_finder=1
        )

        refresh = RefreshToken.for_user(self.finder)
        # token (str): El token de autorización generado para el usuario 'finder'.
        self.token = str(refresh.access_token)
        # auth_headers (dict): Diccionario que contiene las cabeceras de autenticación utilizadas en las solicitudes API.
        self.auth_headers = {'AUTHORIZATION': f'Token {self.token}'}
        # service (Services): Un objeto de servicio creado en la base de datos para las pruebas.
        self.service = Services.objects.create(
            title="Servicio existente",
            description="Descripción existente",
            category="categoryTest",
            duration="30 minutos",
            tags="tag1"
        )
        # post (Posts): Un objeto post asociado al usuario 'finder' y al servicio creado en la base de datos para las pruebas.
        self.post = Posts.objects.create(
            id=1,
            description="Post de prueba",
            disponibility="Disponible 24/7",
            user_id=self.finder.id,
            service_id=self.service.id
        )
        # url (str): El endpoint de la API para gestionar las solicitudes.
        self.url = "/api/requests/"

    def test_send_request_to_supplier(self):
        """
        Caso de prueba para enviar una solicitud a un Oferente (supplier).
        Esta prueba valida el comportamiento del sistema cuando un usuario buscador intenta
        enviar una solicitud al proveedor a través de un endpoint específico.

        Raises:
            AssertionError:
                Si la respuesta HTTP no es la esperada, los datos de respuesta no coinciden con
                el resultado esperado, o el objeto de la petición no se guarda correctamente en la
                base de datos.

        Tests:
            Esta prueba realiza las siguientes comprobaciones:
                1. El código de estado de la respuesta es 201 (Creado).
                2. El mensaje devuelto y el motivo coinciden con los datos enviados.
                3. Se crea correctamente un objeto de solicitud en la base de datos con los campos
                   correctamente asignados: `message`, `reason`, `post_id`, y `user`.
        """

        data = {
            "message": "Solicitud de prueba desde un finder",
            "reason": "Necesito algo de ayuda",
            "post_id": self.post.id
        }

        self.client.force_authenticate(user=self.finder)
        # Realizar una solicitud POST al endpoint correspondiente.
        response = self.client.post(self.url, data, **self.auth_headers)
        # Afirmaciones para validar comportamiento esperado.
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["message"], "Solicitud de prueba desde un finder")
        self.assertEqual(response.data["reason"], "Necesito algo de ayuda")
        # Validar que el objeto Request fue creado en la base de datos.
        self.assertEqual(Requests.objects.count(), 1)

        # Verificar que la solicitud creada tenga los datos correctos en la base de datos
        request = Requests.objects.first()
        self.assertEqual(request.message, "Solicitud de prueba desde un finder")
        self.assertEqual(request.reason, "Necesito algo de ayuda")
        self.assertEqual(request.post_id, self.post.id)
        self.assertEqual(request.user, self.finder)










