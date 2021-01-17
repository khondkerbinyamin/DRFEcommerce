from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.FloatField()
    description = models.TextField(max_length=100, default='')
    is_in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_options")
    size = models.CharField(max_length = 50, default= '')
    color = models.CharField(max_length = 20, default= '')

    def __str__(self):
        return self.product.name + ' ' + self.size + ' ' + self.color
    