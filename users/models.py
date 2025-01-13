from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class Users(AbstractUser):
    telephone = models.CharField(max_length=45)
    is_supplier = models.BooleanField(default=False)
    is_finder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class Ratings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.CharField(max_length=150)

    def __str__(self):
        return self.comment
