from django.test import TestCase
from services.serializers import ServicesSerializer


class ServiceSerializerTestCase(TestCase):
    """
    Conjunto de pruebas para validar la funcionalidad de la clase ServicesSerializer.

    Esta clase contiene casos de prueba para validar el comportamiento del ServicesSerializer, asegurando que
    el serializador maneja correctamente conjuntos de datos válidos e inválidos. Los casos de prueba se centran en
    comprobar el método `is_valid`, asegurando que valida o invalida correctamente los datos
    proporcionados de acuerdo con las reglas del serializador.
    """
    def test_valid_serialization(self):
        """
        Comprueba la validez de la serialización de datos por una instancia de ServicesSerializer
        con los datos de entrada proporcionados. La entrada incluye varios campos como título
        descripción, categoría, duración y etiquetas. La prueba garantiza que la
        serialización es válida para la entrada válida dada.

        Raises:
            AssertionError: Si el serializador no es válido durante la ejecución de la prueba.
        """
        # Datos válidos
        data = {
            "title": "Ejemplo",
            "description": "Descripción válida",
            "category": "categoryTest",
            "duration": "1 hora",
            "tags": "tag1, tag2"
        }
        serializer = ServicesSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_invalid_serialization(self):
        """
        Comprueba la serialización de datos no válidos y se asegura de que el serializador
        identifica los errores correctamente.

        Este método valida que una instancia del serializador reconoce problemas específicos
        problemas con la entrada proporcionada cuando los datos no cumplen con el
        esquema esperado.

        Raises:
            AssertionError:
                Aparece cuando no se cumplen las condiciones de la prueba. En concreto, si el
                serializador valida incorrectamente una entrada no válida o si los errores
                esperados no están presentes en la salida de errores del serializador.
        """

        # Datos inválidos
        data = {
            "title": "", # Esto debería causar un error, ya que 'title' está vacío
            "description": "Descripción válida",
            "category": "categoryTest",
            "duration": "1 hora",
            "tags": "tag1, tag2"
        }
        serializer = ServicesSerializer(data=data)
        self.assertFalse(serializer.is_valid()) # Debe devolver False
        self.assertIn("title", serializer.errors) # 'title' debe estar en los errores
