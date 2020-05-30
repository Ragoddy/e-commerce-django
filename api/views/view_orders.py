# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.db import IntegrityError, transaction

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework import status


from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point

from orders.models import Order, ProductByOrder
from markets.models import Category, Market, Product

from api.serializers.serializer_orders import OrderSerializer, OrderCreateSerializer, ProductByOrderSerializer


class OrderCreateAPIView(APIView):
    """
    API endpoint for create orders of the market app
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    @transaction.atomic
    def post(self, request, version, format=None):
        serializer = None
           
        if "products" in request.data:  
            
            market_id = Market.objects.get(UUID = request.data["market"]).id
            data_order = {
                "type_so":request.data["type_so"],
                "payment_method": request.data["payment_method"] , 
                "total_price": request.data["total_price"], 
                "comments": request.data["comments"], 
                "address":request.data["address"] ,
                "complement_address":request.data["complement_address"], 
                "name_client": request.data["name_client"], 
                "phone": request.data["phone"], 
                "market": market_id,
                "status_order": 1
            }
            
            serializer = OrderCreateSerializer(data=data_order)     
            if serializer.is_valid():
                serializer.save()                    
                
                order = Order.objects.get(pk=serializer.data['pk'])
                
                for prod in request.data['products']:
                    product = Product.objects.get(pk=prod['pk'])
                    pbo = ProductByOrder()
                    pbo.order = order
                    pbo.product = product
                    pbo.amount = prod['amount']
                    pbo.unit_price = product.price   
                    pbo.total_price = product.price 
                    pbo.save()
                
                return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)                
        else:
            return Response({"success":False, "data": "Se deben agregar productos al pedido", "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)    
            
        return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)


class OrderStatusUpdateAPIView(APIView):
    """
    API endpoint for update status orders
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, version, format=None):
        data = request.data       
        status_order = 0 
        if data['order_id']:
            status_order = int(data['status_order'])
            order = Order.objects.get(UUID=data['order_id'])   
            order.status_order = status_order
            order.save()
            return Response({"success":True, "data": "", "message": "Datos actualizados correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "data": "Error al actualizar el pedido", "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)


class ProductByOrderListAPIView(APIView):
    """
    API endpoint for orders historic
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, uuid, version, format=None):      
        """
        Return a list of orders histocic.
        """     
        id_order = 0
        uuid = str(uuid)
        
        if Order.objects.filter(UUID = uuid).exists():
            id_order = Order.objects.get(UUID = uuid).id        
        queryset = ProductByOrder.objects.filter(order=id_order, status= 1).order_by('-creation_date')
        serializer = ProductByOrderSerializer(queryset, many=True, context={"request":request})
        
        return Response({"success":True, "data": serializer.data, "message": "Datos consultados correctamente"}, status=status.HTTP_200_OK)
    

class OrdersCountAPIView(APIView):
    """
    API endpoint count orders for type.
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id_market, version, format=None):      
        """
        Return a count orders for type.
        """     
        orders_count = 0
        orders_historic_count = 0   
        
        id_market = int(id_market)
        
        queryset_order = Order.objects.filter(market=id_market);
        orders_count = queryset_order.exclude(status_order__in=[0,3]).count()        
        orders_historic_count = queryset_order.exclude(status_order__in=[1,2]).count()  
        
        data = {'orders_count': orders_count, 'orders_historic_count': orders_historic_count}
        
        return Response({"success":True, "data": data, "message": "Datos consultados correctamente"}, status=status.HTTP_200_OK)


class OrdersHistoricListTableAPIView(APIView):
    """
    API endpoint for orders historic
    """
    def get(self, request, id_market, version, format=None):      
        """
        Return a list of orders histocic.
        """     
        id_market = int(id_market)
        
        queryset = Order.objects.filter(market=id_market, status_order__in=[0,3]).order_by('-creation_date')
        serializer = OrderSerializer(queryset, many=True, context={"request":request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrdersListTableAPIView(APIView):
    """
    API endpoint for orders
    """
    def get(self, request, id_market, version, format=None):      
        """
        Return a list of orders.
        """     
        id_market = int(id_market)
        
        queryset = Order.objects.filter(market=id_market).exclude(status_order__in=[0,3]).order_by('-creation_date')
        serializer = OrderSerializer(queryset, many=True, context={"request":request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    