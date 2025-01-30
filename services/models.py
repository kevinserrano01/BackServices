from django.db import models

# Create your models here.


class Services(models.Model):
    """
    Representa un servicio con metadatos asociados.

    La clase Servicios define la estructura para gestionar y almacenar
    información relacionada con un servicio, como su título, descripción
    categoría, duración y etiquetas. Está pensada para ser utilizada dentro
    de una aplicación Django como un modelo respaldado por una tabla de base de datos.

    Attributes:
        title (str): El nombre o título del servicio, limitado a 45 caracteres.
        description (str): Una descripción detallada del servicio, limitada a
            400 caracteres.
        category (str): Categoría a la que pertenece el servicio,
            limitada a 45 caracteres.
        duration (str): La duración estimada asociada al
            servicio, limitada a 45 caracteres.
        tags (str): Palabras clave o etiquetas adicionales para la categorización,
            limitadas a 45 caracteres.
        created_at (datetime): La fecha y hora de creación del registro
            que se establece automáticamente en el momento de la creación.
        updated_at (datetime): La fecha y hora de la última actualización
            se actualizó por última vez, se establece automáticamente en las modificaciones.
    """
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=500)
    category = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    tags = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

