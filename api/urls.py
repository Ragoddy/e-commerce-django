from django.urls import path, include
from api.views import view_markets, view_orders, view_users


urlpatterns = [
    #markets
    path('categories/', view_markets.CategoryListAPIView.as_view(), name='api-categories-list'),
    path('markets/', view_markets.MarketCreateAPIView.as_view(), name='api-markets-create'),
    path('markets/<str:longitude>/<str:latitude>/', view_markets.MarketListAPIView.as_view(), name='api-markets-list'),
    path('phones/', view_markets.PhoneCreateAPIView.as_view(), name='api-phones-create'),
    
    #products
    path('products/<str:id_market>/', view_markets.ProductListAPIView.as_view(), name='api-product-list-table'),
    
    #Users
    path('clients/', view_users.ClientCreateAPIView.as_view(), name='api-clients-create'),
    
    #Orders
    path('orders/', view_orders.OrderCreateAPIView.as_view(), name='api-orders-create'),
    
    #endpoint for tables
    #products
    path('table/products/<str:id_market>/', view_markets.ProductListTableAPIView.as_view(), name='api-product-list-table'),
     path('table/orders/<str:id_market>/', view_orders.OrdersListTableAPIView.as_view(), name='api-order-list-table'),
]