from rest_framework import serializers

from orders.models import *

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['pk', 'type_so', 'creation_date', 'number_phone', 'market']