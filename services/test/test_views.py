
from rest_framework.test import APITestCase
from rest_framework import status
from services.models import Services
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

class ServiceViewTestCase(APITestCase):
    """
    Casos de prueba para los endpoint de servicio de la aplicación.

    Esta clase de prueba valida el comportamiento de los endpoints de la API relacionados con los servicios, como
    como la recuperación de servicios o la creación de otros nuevos. Las pruebas garantizan que las respuestas de la API
    se adhieren a los códigos de estado HTTP esperados y verifican la corrección de la capa de datos.

    Attributes:
        user (custom user model instance): Representa el usuario de prueba creado para
            autenticación de la API.
        token (str): Token de acceso generado para el usuario de prueba para autenticar
            las solicitudes de la API.
        auth_headers (dict): Diccionario de cabeceras de autenticación utilizadas en las
            solicitudes para la autorización de usuarios.
        service (Services model instance): Instancia de un servicio preexistente.
            Creado para validar el número de servicios tras su creación.
        url (str): URL base para los endpoints de la API de servicio.
    """

    def setUp(self):
        """
        Establece los prerrequisitos necesarios para ejecutar pruebas dentro del caso de prueba. Este método
        inicializa una instancia de usuario, genera un token de autenticación y crea una instancia de servicio
        para su uso en aserciones de prueba. También define el punto final de la API que se va a probar.
        """

        # Obtén el modelo de usuario personalizado
        User = get_user_model()  # Esto se asegura de que estás usando 'users.Users'

        # Crear un usuario de prueba y generarle un token
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="testuser@example.com",
            first_name="Test",
            last_name="User",
            telephone="1234567890",
            is_supplier=1,
            is_finder=0
        )
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)
        self.auth_headers = {'AUTHORIZATION': f'Token {self.token}'}

        # Crear un servicio existente (para verificar conteo al final)
        self.service = Services.objects.create(
            title="Servicio existente",
            description="Descripción existente",
            category="categoryTest",
            duration="30 minutos",
            tags="tag1"
        )
        self.url = "/api/services/"  # endpoint de services

    def test_get_request(self):
        """
        Envía una solicitud GET a la URL especificada y comprueba el estado de la respuesta.

        Este método comprueba si una solicitud GET a la URL proporcionada
        devuelve un código de estado HTTP 200 OK. Asume que la URL y el cliente se han
        se han configurado correctamente en el entorno de pruebas.

        Raises:
            AssertionError: Si el código de estado de la respuesta GET no es igual a
            HTTP 200 OK.
        """
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_request(self):
        """
        Crea un servicio enviando una solicitud `POST` al endpoint correspondiente.

        Envía una solicitud POST con datos válidos al punto final, autentica la solicitud utilizando un usuario
        preconfigurado y verifica el código de estado de la respuesta para confirmar que se ha realizado correctamente.
        un usuario preconfigurado, y verifica el código de estado de la respuesta para confirmar la correcta
        la creación de un servicio. Además, comprueba que el número total de servicios
        en la base de datos ha aumentado como se esperaba después de la operación.

        Attributes:
            self.user:
                La instancia de usuario autenticado necesaria para realizar la petición POST.
            self.client:
                El cliente de prueba utilizado para simular las peticiones HTTP.
            self.url:
                El endpoint URL al que se envía la petición POST.
            self.auth_headers:
                Las cabeceras de autenticación necesarias para la petición.

        Raises:
            AssertionError:
                Si el código de estado de la respuesta no es 201 CREADO, o si el número de servicios
                no coincide con el número esperado.
        """
        # Envía una solicitud POST con datos válidos
        data = {
            "title": "Ejemplo",
            "description": "Descripción válida",
            "category": "categoryTest",
            "duration": "1 hora",
            "tags": "tag1, tag2"
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.url, data, **self.auth_headers)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Services.objects.count(), 2)

    def test_filter_services_by_category(self):
        """
        Filtra los servicios por una categoría específica y válida la respuesta.

        Esta prueba pretende verificar que el filtrado de servicios por categorías funciona correctamente.
        Crea servicios con distintas categorías, realiza una solicitud a la API para filtrar
        servicios por una categoría determinada, y se asegura de que la respuesta contiene solo
        servicios que pertenecen a la categoría especificada.

        Raises:
            AssertionError:
                Aparece cuando falla alguna condición de las afirmaciones.
        """

        # Crear servicios con diferentes categorías para poder probar el filtrado.
        Services.objects.create(
            title="Servicio 1",
            description="Descripción 1",
            category="Desarrollo Web",
            duration="1 hora",
            tags="tag1",
        )
        Services.objects.create(
            title="Servicio 2",
            description="Descripción 2",
            category="Educacion",
            duration="2 horas",
            tags="tag2",
        )

        # Filtrar por categoría "Educacion"
        response = self.client.get(f"{self.url}?category=Educacion")

        # Validar los resultados (Afirmaciones que yo quiero esperar)
        self.assertEqual(response.status_code, status.HTTP_200_OK) # Verifica que el código de estado sea `200 OK`.
        self.assertEqual(len(response.data), 1) # Debería haber un servicio listado
        self.assertEqual(response.data[0]["title"], "Servicio 2")
        self.assertEqual(response.data[0]["category"], "Educacion")


    def test_filter_services_no_results(self):
        """
        Probar el comportamiento de la API al filtrar por una categoría inexistente.
        Verifica que la API devuelve una lista vacía si no hay servicios que cumplan con el filtro.

        Esta prueba garantiza que la API devuelva un estado 200 OK y una lista vacía cuando
        ningún servicio coincide con los criterios de filtrado dados. Válida que el mecanismo de filtrado
        gestiona sin errores los casos en los que no se encuentra ninguna coincidencia.

        Raises:
            AssertionError: Si la respuesta no cumple el estado esperado o los
                datos devueltos no son una lista vacía.
        """
        response = self.client.get(f"{self.url}?category=Inexistente")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 0)  # Lista vacía si no hay coincidencias