from django.contrib import admin
from .models import Posts, Requests, StatusServices

# Register your models here.


@admin.register(Posts)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('description', 'datecreated',
                    'disponibility', 'user', 'service')


@admin.register(Requests)
class RequestsAdmin(admin.ModelAdmin):
    list_display = ('message', 'status', 'reason', 'user', 'post')


@admin.register(StatusServices)
class StatusServicesAdmin(admin.ModelAdmin):
    list_display = ('status', 'comment', 'dateupdated', 'request', 'user')
