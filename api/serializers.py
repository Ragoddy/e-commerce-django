from rest_framework import serializers

from markets.models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields =('pk','code','name','description','image')       
        

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields =('pk','name','addresses','latitude','longitude','city','minimun_price', 'state')    
        
