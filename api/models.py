from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    country = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)


    
class Category(models.Model):
    key = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.key
    
class News(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    info = models.TextField()
    date = models.CharField(max_length=100)  # Используем CharField для даты как строки
    image_url = models.URLField(blank=True, null=True)  # Поле для URL изображения


class Tour(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    kind = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    price = models.IntegerField()
    discount = models.IntegerField()
    img_url = models.URLField(blank=True, null=True)  # Поле для URL изображения
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    id = models.IntegerField(primary_key=True)

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    message = models.TextField()
    rate = models.IntegerField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
      return f'{self.user.username} - {self.message}'


class Request(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    place = models.CharField(max_length=200)
    explain = models.TextField()
    id = models.IntegerField(primary_key=True)