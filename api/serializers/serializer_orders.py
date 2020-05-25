from rest_framework import serializers

from orders.models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['UUID', 'type_so', 'creation_date', 'payment_method', 'status_order' ,
                  'total_price', 'comments', 'address' ,'complement_address', 'name_client', 'phone']
        

class ProductByOrderSerializer(serializers.ModelSerializer):
    product_name = serializers.ReadOnlyField(source='product.title')
    
    class Meta:
        model = ProductByOrder
        fields = ['creation_date', 'product', 'amount' , 'product_name',
                  'unit_price', 'total_price', 'status']