# -*- coding: utf-8 -*-
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

import traceback
import sys

from markets.models import Category, Market, Telephone, Product
from api.serializers.serializer_markets import CategorySerializer, MarketSerializer, TelephoneSerializer, ProductSerializer


class CategoryListAPIView(APIView):
    """
    API endpoint for categories app.
    """
    def get(self, request, version, format=None):   
        """
        Return a list of all categories.
        """     
        queryset = Category.objects.all().order_by('sorting')
        serializer = CategorySerializer(queryset, many=True, context={"request":request})
        
        return Response({"success":True, "data": serializer.data, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)

    

class PhoneCreateAPIView(APIView):
    """
    API endpoint for create phones for markets app
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, version, format=None):
        serializer = TelephoneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)



class MarketNewsLocationListAPIView(APIView):
    """
    API endpoint for markets app
    """
    def get(self, request, longitude, latitude, version, format=None):      
        """
        Return a list of all markets for distance latitud and longitude.
        """        
        longitude = float(longitude)
        latitude = float(latitude)
        client_location = Point(longitude, latitude, srid=4326)
        
        queryset = []              
        markets = Market.objects.filter(status=1, location__distance_lt=(client_location, D(m=2000)))\
                .annotate(distance=Distance('location', client_location)).order_by('distance','-creation_date')[0:5]
                
        for market in markets:    
            queryset_phone = Telephone.objects.filter(market = market.id)
            serializer_phones = TelephoneSerializer(queryset_phone, many=True)  

            queryset_category = market.categories.all()
            serializer_category = CategorySerializer(queryset_category, many=True, context={"request":request})        
            
            queryset_products = Product.objects.filter(market=market.id, status=1).order_by('-creation_date')
            serializer_products = ProductSerializer(queryset_products, many=True,  context={"request":request})      
            
            image_url = None
            if market.image:
                image_url = request.build_absolute_uri(market.image.url)                 
                
            obj ={
                    "UUID": market.UUID,
                    "code": market.code,
                    "name": market.name,
                    "addresses": market.addresses,
                    "city": market.city,
                    "longitude": market.longitude,
                    "latitude": market.latitude,
                    "minimum_price": market.minimum_price,
                    "delivery_price": market.delivery_price,
                    "image": image_url,
                    "phones": serializer_phones.data,
                    "categories": serializer_category.data,
                    "products": serializer_products.data
                }
            queryset.append(obj)
                
        return Response({"success":True, "data": queryset, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)
    

class MarketNewsListAPIView(APIView):
    """
    API endpoint for markets app
    """
    def get(self, request, version, format=None):      
        """
        Return a list of all markets for distance latitud and longitude.
        """        
        queryset = []              
        markets = Market.objects.filter(status=1).order_by('-creation_date')[0:5]
                
        for market in markets:  
            queryset_category = market.categories.all()
            serializer_category = CategorySerializer(queryset_category, many=True, context={"request":request}) 
            
            image_url = None
            if market.image:
                image_url = request.build_absolute_uri(market.image.url)                 
                
            obj ={
                    "UUID": market.UUID,
                    "code": market.code,
                    "name": market.name,
                    "addresses": market.addresses,
                    "city": market.city,
                    "longitude": market.longitude,
                    "latitude": market.latitude,
                    "minimum_price": market.minimum_price,
                    "delivery_price": market.delivery_price,
                    "image": image_url,
                    "categories": serializer_category.data
                }
            queryset.append(obj)
                
        return Response({"success":True, "data": queryset, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)
    
    
        
class MarketListAPIView(APIView):
    """
    API endpoint for markets app
    """
    def get(self, request, longitude, latitude, version, format=None, category=None):      
        """
        Return a list of all markets for distance latitud and longitude.
        """        
        longitude = float(longitude)
        latitude = float(latitude)
        if not category is None:
            category = int(category)
        else: 
            category = 0
        client_location = Point(longitude, latitude, srid=4326)
        
        
        queryset = []  
        print(category)          
        if category > 0:            
            markets = Market.objects.filter(status=1, categories = category, location__distance_lt=(client_location, D(m=2000)))\
                        .annotate(distance=Distance('location', client_location)).order_by('distance', '-creation_date')[0:30]
        else:
            markets = Market.objects.filter(status=1, location__distance_lt=(client_location, D(m=2000)))\
                        .annotate(distance=Distance('location', client_location)).order_by('distance', '-creation_date')[0:30]
                        
        for market in markets:    
            queryset_phone = Telephone.objects.filter(market = market.id)
            serializer_phones = TelephoneSerializer(queryset_phone, many=True)  

            queryset_category = market.categories.all()
            serializer_category = CategorySerializer(queryset_category, many=True, context={"request":request})        
            
            queryset_products = Product.objects.filter(market=market.id, status=1).order_by('-creation_date')
            serializer_products = ProductSerializer(queryset_products, many=True, context={"request":request})      
            
            image_url = None
            if market.image:
                image_url = request.build_absolute_uri(market.image.url)         
            
            obj ={
                    "UUID": market.UUID,
                    "code": market.code,
                    "name": market.name,
                    "addresses": market.addresses,
                    "city": market.city,
                    "longitude": market.longitude,
                    "latitude": market.latitude,
                    "minimum_price": market.minimum_price,
                    "delivery_price": market.delivery_price,
                    "image": image_url,
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
        try:
            serializer = MarketSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                ##save phone                    
                try:
                    data_phone = {
                            'type_telephone': 2,
                            'number': request.data['phone_set'], 
                            'first': 1, 
                            'market': serializer.data['pk']
                            }
                
                    serializer_phone = TelephoneSerializer(data=data_phone)
                    if serializer_phone.is_valid():
                        serializer_phone.save()          
                except KeyError:
                    print("Error in telephone_set")                      

                #save category  
                try:
                    market = Market.objects.get(pk = serializer.data['pk'])
                    category = Category.objects.get(pk= request.data['category_set'])
                    market.categories.add(category)
                except KeyError:
                    print("Error in category_set")                
                
                return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
            print("error: " , str(serializer.errors))
            return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as error:
            error_msg = traceback.format_exc()
            print(error_msg)
            return Response({"success":False, "data": None , "message": error_msg }, status=status.HTTP_400_BAD_REQUEST)



