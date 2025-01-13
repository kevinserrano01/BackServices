from django.db import models

# Create your models here.


class Services(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=400)
    category = models.CharField(max_length=45)
    duration = models.CharField(max_length=45)
    tags = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

