from django.db import models

# Create your models here.


class Posts(models.Model):
    description = models.CharField(max_length=150)
    datecreated = models.DateTimeField(auto_now_add=True)
    disponibility = models.CharField(max_length=45)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Services', on_delete=models.CASCADE)


class Requests(models.Model):
    message = models.CharField(max_length=150)
    status = models.CharField(max_length=45)
    reason = models.CharField(max_length=45)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)


class StatusServices(models.Model):
    status = models.CharField(max_length=45)
    comment = models.CharField(max_length=150)
    dateupdated = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
