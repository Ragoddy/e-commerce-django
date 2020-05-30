from rest_framework import serializers

from orders.models import *

class OrderSerializer(serializers.ModelSerializer):    
    class Meta:
        model = Order
        fields = ['UUID','type_so', 'payment_method' , 'total_price', 'creation_date', 'comments', 'address' ,'complement_address', 'name_client', 'phone', 'status_order']
        read_only_fields = ['pk','UUID' 'status_order']
        

class OrderCreateSerializer(serializers.ModelSerializer):
    
    products = serializers.ReadOnlyField(read_only = True)
    class Meta:
        model = Order
        fields = ['pk','UUID','type_so', 'payment_method' , 'total_price', 'comments', 'address' ,'complement_address', 'name_client', 'phone', 'market',
                   'status_order', 'products']
        read_only_fields = ['pk','UUID', 'status_order']
        extra_kwargs = {'products': {'write_only': True}}
        
        
class ProductByOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.title')
    
    class Meta:
        model = ProductByOrder
        fields = ['creation_date', 'product', 'amount' , 'product_name',
                  'unit_price', 'total_price', 'status']