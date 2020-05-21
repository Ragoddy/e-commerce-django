from rest_framework import serializers

from orders.models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['UUID', 'type_so', 'creation_date', 'payment_method', 'status_order' ,
                  'total_price', 'comments', 'address' ,'complement_address', 'name_client', 'phone']