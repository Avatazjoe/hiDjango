from django.db import models
from django.conf  import settings
from django.utils.text import slugify
from django.core.urlresolvers import reverse
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField (max_length=250)
    price = models.FloatField ()
    size = models.CharField(max_length=30)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    logo = models.ImageField(upload_to="static/images", blank=True)

    def save(self):
        if not self.id:
            self.slug = slugify(self.name)
        super(Product, self).save()

    def __str__(self):
        return self.name
    slug = models.SlugField(editable=True) # hide from admin

class Category(models.Model):
    name = models.CharField(max_length=30)
    def __str__(self):
        return self.name

class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    product = models.ForeignKey('Product',on_delete=models.CASCADE,related_name="product")
    created = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.product.name+" => "+self.user.username

    def TotalPrice(self):
        return self.quantity * self.product.price