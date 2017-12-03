from django.db import models
from django.conf  import settings
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField (max_length=250)
    price = models.FloatField ()
    size = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="static/images", blank=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name
