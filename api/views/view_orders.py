# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated 
from rest_framework import status

from django.contrib.gis.measure import Distance
from django.contrib.gis.geos import Point

from orders.models import Order

from api.serializers.serializer_orders import OrderSerializer


class OrderCreateAPIView(APIView):
    """
    API endpoint for create orders of the market app
    """
    def post(self, request, version, format=None):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"success":True, "data": serializer.data, "message": "Datos guardados correctamente"}, status=status.HTTP_201_CREATED)
        return Response({"success":False, "data": serializer.errors, "message": "Datos incorrectos"}, status=status.HTTP_400_BAD_REQUEST)


class OrderStatusUpdateAPIView(APIView):
    """
    API endpoint for update status orders
    """
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
    