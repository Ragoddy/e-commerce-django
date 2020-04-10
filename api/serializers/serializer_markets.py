from rest_framework import serializers

from markets.models import *

class CategorySerializer(serializers.ModelSerializer):
    
    # img_url = serializers.ImageField(max_length=None, use_url=True, allow_null=True, required=False)
    # img_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = ('code', 'name', 'description')
    
    def get_img_url(self, category):
        request = self.context.get('request')        
        img_url = category.image.url
        return request.build_absolute_uri(img_url)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['pk','name', 'description', 'size', 'price']
        
        
class TelephoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = ['pk','type_telephone', 'number', 'first', 'market']
        
        
class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Telephone
        fields = ['pk','day', 'start_hour', 'end_hour', 'state', 'market']
        
                
class MarketSerializer(serializers.ModelSerializer):
    
    phone_set = TelephoneSerializer(read_only = True)
    category_set = serializers.IntegerField(read_only = True)
    class Meta:
        model = Market
        fields =('pk','code','name','addresses','longitude', 'latitude', 'location','city','minimun_price', 'state', 'phone_set', 'category_set') 
        