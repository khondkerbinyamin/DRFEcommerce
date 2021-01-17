from django.contrib import admin
from .models import Product,ProductOption

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductOption)