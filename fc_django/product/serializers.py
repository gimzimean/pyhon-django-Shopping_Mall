from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer): # 직렬화 
    class Meta:
        model = Product
        fields = '__all__'