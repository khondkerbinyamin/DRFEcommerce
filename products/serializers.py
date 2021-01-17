from rest_framework import serializers
from .models import Product,ProductOption





class ProductOptionSerializer(serializers.ModelSerializer):
    # name = serializers.RelatedField(source=product.name, read_only=True)
    # category = serializers.RelatedField(source=product.category, read_only=True)
    # price = serializers.RelatedField(source=product.price, read_only=True)
    # description = serializers.RelatedField(source=product.description, read_only=True) 
    # is_in_stock = serializers.RelatedField(source=product.is_in_stock)
   # product = ProductSerializer()

    class Meta:
        model = ProductOption
        fields = ['size', 'color']
        depth = 1
        
       



class ProductSerializer(serializers.ModelSerializer):
    product_options = ProductOptionSerializer(read_only=True, many=True)
    #size = serializers.CharField(source='ProductOption.size', read_only=True)
    
    class Meta:
        model = Product
        fields = ['id','name','price','description','is_in_stock', 'product_options']