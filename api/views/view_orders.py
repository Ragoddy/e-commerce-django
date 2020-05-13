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
