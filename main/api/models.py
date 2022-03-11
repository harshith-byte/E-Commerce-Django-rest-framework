
from statistics import mode
from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
# Create your models here.
class category(models.Model):
    name=models.CharField(max_length=200)
    image=models.ImageField(upload_to="category",null=True,blank=True)
    def __str__(self):
        return self.name


class products(models.Model):
    category_id=models.ForeignKey(category, on_delete=models.CASCADE)

    product_name=models.CharField(max_length=200)
    product_description=models.CharField(max_length=1000)
    product_image=models.ImageField(upload_to="product",null=True,blank=True)
    price=models.FloatField()

    def __str__(self):
        return self.product_name
    
class customer(models.Model):
    username=models.CharField(max_length=200)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=200)


class Cart(models.Model):
    product=models.ForeignKey(products, on_delete=models.CASCADE)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    quantity=models.IntegerField()


