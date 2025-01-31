from django.db import models

# Create your models here.


class Posts(models.Model):
    description = models.CharField(max_length=400)
    datecreated = models.DateTimeField(auto_now_add=True)
    disponibility = models.CharField(max_length=150)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    service = models.ForeignKey('services.Services', on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.description


class Requests(models.Model):
    message = models.CharField(max_length=300)
    status = models.CharField(max_length=45, default='pending')
    reason = models.CharField(max_length=350, null=True, blank=True)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.message


class StatusServices(models.Model):
    status = models.CharField(max_length=45, default='en proceso')
    comment = models.CharField(max_length=350, null=True, blank=True)
    dateupdated = models.DateTimeField(auto_now_add=True)
    request = models.ForeignKey(Requests, on_delete=models.CASCADE)
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status

class SavedPosts(models.Model):
    user = models.ForeignKey('users.Users', on_delete=models.CASCADE)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)