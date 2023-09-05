from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=11)
    address = models.CharField(max_length=200)
    reg_date = models.DateTimeField(auto_now_add=True)


class Goods(models.Model):
    product_name = models.CharField(max_length=100)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=10, decimal_places=2)
    product_quantity = models.IntegerField()
    date_item_add = models.DateTimeField()


class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    goods = models.ManyToManyField(Goods)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
# Create your models here.
