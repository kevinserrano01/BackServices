from django.db import models

# Create your models here.

# * implementar el modelo de Users y Ratings

class Users(models.Model):  
    name = models.CharField(max_length=45)
    lastname = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    password = models.CharField(max_length=45)
    telephone = models.CharField(max_length=45)
    is_supplier = models.BooleanField(default=False)
    is_finder = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# class Ratings(models.Model):

class Ratings(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    stars = models.IntegerField()
    comment = models.CharField(max_length=150)