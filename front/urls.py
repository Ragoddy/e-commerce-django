from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.FrontKyperView.as_view(), name='search_markets'),
]