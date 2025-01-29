from django.contrib import admin
from .models import Services

# Register your models here.


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de registros
    list_display = ('title', 'category', 'duration',
                    'tags', 'created_at', 'updated_at')
    # Campos por los que se puede filtrar
    list_filter = ('category', 'duration', 'tags',
                   'created_at', 'updated_at')
    # Campos por los que se puede buscar
    search_fields = ('title', 'category')
    # Campo por el que se puede filtrar por fecha
    date_hierarchy = 'created_at'
    # Ordenar por fecha de creación descendente
    ordering = ('-created_at',)
