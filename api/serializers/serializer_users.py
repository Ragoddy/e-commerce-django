from rest_framework import serializers

from users.models import *


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['UUID', 'longitude', 'latitude', 'location', 'state', 'creation_date']