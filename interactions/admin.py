from django.contrib import admin
from .models import Posts, Requests, StatusServices

# Register your models here.
admin.site.register(Posts)
admin.site.register(Requests)
admin.site.register(StatusServices)
