from django.contrib import admin
from .models import Users, Ratings

# Register your models here.
admin.site.register(Users)


@admin.register(Ratings)
class RatingsAdmin(admin.ModelAdmin):
    # Campos a mostrar en la lista de registros
    list_display = ('comment', 'user', 'stars')
