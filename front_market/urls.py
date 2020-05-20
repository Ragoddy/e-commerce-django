from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('products/', views.ProductView.as_view(), name='products_markets'),
    path('orders/', views.OrderHistoricView.as_view(), name='orders_markets'),
    path('promos/', views.PromoView.as_view(), name='promo_markets'),
    path('kyper/', views.KyperView.as_view(), name='kyper_markets'),
    
    path('create_order/', views.OrderCreateView.as_view(), name='create_order_markets'),
]