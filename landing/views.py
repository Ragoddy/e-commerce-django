# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse

from api.serializers.serializer_markets import MarketSerializer, TelephoneSerializer

class LandingKyperView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'landing/index.html', context)

class LandingCreateKyperView(View):
    def post(self, request, *args, **kwargs):
        
        data = {
                'name': request.POST['name'],
                'addresses': request.POST['addresses'],
                'city': request.POST['city'],
                'minimun_price': 4000,
                'state': 0
                }
        
        serializer = MarketSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            
            data_phone = {
                          'type_telephone': 2,
                          'number': request.POST['phone'], 
                          'first': 1, 
                          'market': serializer.data['pk']
                        }
            
            serializer = TelephoneSerializer(data=data_phone)
            if serializer.is_valid():
                serializer.save()
                
        return HttpResponseRedirect("/")