from django.shortcuts import render
from django.views.generic import View, ListView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class HomeView(View):
    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        context = {}
        return render(request, 'front_market/home.html', context)
