from django.db import models

class Shop(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=40)

class Product(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=40)

class ListItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.FloatField()
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    bought = models.BooleanField(default=False)