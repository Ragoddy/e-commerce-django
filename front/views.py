# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import View, ListView, FormView
from django.http import HttpResponseRedirect, HttpResponse


class FrontKyperView(View):
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'front/index.html', context)