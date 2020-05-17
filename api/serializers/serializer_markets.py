from rest_framework import serializers

from markets.models import *

class CategorySerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Category
        fields = ('code', 'name', 'description', 'count_markets', 'sorting', 'image')   

       
        
class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = ['pk','type_telephone', 'number', 'first', 'market']
        
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        state = serializers.IntegerField(read_only = True)
        
        model = Telephone
        fields = ['pk','day', 'start_hour', 'end_hour', 'status', 'market', 'state']
        
                
class MarketSerializer(serializers.ModelSerializer):
    
    phone_set = TelephoneSerializer(read_only = True)
    category_set = serializers.IntegerField(read_only = True)
    minimun_price = serializers.IntegerField(read_only = True)
    state = serializers.IntegerField(read_only = True)
    class Meta:
        model = Market
        fields =('pk','code','name','addresses','longitude', 'latitude', 'location','city','minimum_price', 'status', 'phone_set', 'category_set', 'state', 'minimun_price') 



class ProductSerializer(serializers.ModelSerializer):    
    
    class Meta:
        model = Product
        fields = ('pk', 'title', 'description', 'price', 'image', 'available', 'status','creation_date', 'market')   