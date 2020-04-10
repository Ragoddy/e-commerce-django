# -*- coding: utf-8 -*-
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point

from markets.models import Category, Market, Telephone

from api.serializers.serializer_markets import CategorySerializer, MarketSerializer, TelephoneSerializer, ProductSerializer


class CategoryListAPIView(APIView):
    """
    API endpoint for categories app.
    """
    def get(self, request, version, format=None):   
        """
        Return a list of all categories.
        """     
        queryset = Category.objects.all()
        serializer = CategorySerializer(queryset, many=True, context={"request":request})
        
        return Response({"success":True, "data": serializer.data, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)

    

class PhoneCreateAPIView(APIView):
    """
    API endpoint for create phones for markets app
    """
    def post(self, request, version, format=None):
        serializer = TelephoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)


    
class MarketListAPIView(APIView):
    """
    API endpoint for markets app
    """
    def get(self, request, longitude, latitude, version, format=None):      
        """
        Return a list of all markets for distance latitud and longitude.
        """        
        longitude = float(longitude)
        latitude = float(latitude)
        market_location = Point(longitude, latitude)
        
        queryset = []
         
        markets = Market.objects.filter(state = 1,location__distance_lt=(market_location, Distance(m=2000))) 
        
        for market in markets:    
            
            queryset_phone = Telephone.objects.filter(market = market.id)
            serializer_phones = TelephoneSerializer(queryset_phone, many=True)  

            queryset_category = market.categories.all()
            serializer_category = CategorySerializer(queryset_category, many=True, context={"request":request})        
            
            queryset_products = market.products.all()
            serializer_products = ProductSerializer(queryset_products, many=True)      
            
            obj ={
                    "code": market.code,
                    "name": market.name,
                    "addresses": market.addresses,
                    "city": market.city,
                    "longitude": market.longitude,
                    "latitude": market.latitude,
                    "minimun_price": market.minimun_price,
                    "phones": serializer_phones.data,
                    "categories": serializer_category.data,
                    "products": serializer_products.data
                }
            queryset.append(obj)
                
        return Response({"success":True, "data": queryset, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)




class MarketCreateAPIView(APIView):
    """
    API endpoint for create markets app
    """
    def post(self, request, version, format=None):
        serializer = MarketSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            ##save phone    
            data_phone = {
                          'type_telephone': 2,
                          'number': request.data['phone_set'], 
                          'first': 1, 
                          'market': serializer.data['pk']
                        }
            
            serializer_phone = TelephoneSerializer(data=data_phone)
            if serializer_phone.is_valid():
                serializer_phone.save()                
           
            market = Market.objects.get(pk = serializer.data['pk'])
            category = Category.objects.get(pk= request.data['category_set'])
            market.categories.add(category)
            
            return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
