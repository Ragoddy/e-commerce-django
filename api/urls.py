from django.urls import path, include
from api.views import view_markets, view_products, view_orders, view_users


urlpatterns = [
    #markets
    path('categories/', view_markets.CategoryListAPIView.as_view(), name='api-categories-list'),
    path('markets/', view_markets.MarketCreateAPIView.as_view(), name='api-markets-create'),
    path('markets/<str:longitude>/<str:latitude>/<int:category>/', view_markets.MarketListAPIView.as_view(), name='api-markets-list'),
    path('markets/news/<str:longitude>/<str:latitude>/', view_markets.MarketNewsListAPIView.as_view(), name='api-markets-news-list'),
    path('phones/', view_markets.PhoneCreateAPIView.as_view(), name='api-phones-create'),
    
    #products
    path('products/<str:id_market>/', view_products.ProductListAPIView.as_view(), name='api-product-list-table'),
    
    #Users
    path('clients/', view_users.ClientCreateAPIView.as_view(), name='api-clients-create'),
    
    #Orders
    path('orders/count/<str:id_market>/', view_orders.OrdersCountAPIView.as_view(), name='api-orders-count'),
    path('orders/', view_orders.OrderCreateAPIView.as_view(), name='api-orders-create'),
    path('orders/status/', view_orders.OrderStatusUpdateAPIView.as_view(), name='api-status-orders-update'),
    path('orders/products/<str:uuid>/', view_orders.ProductByOrderListAPIView.as_view(), name='api-product-by-order-list'),
    
    #endpoint for tables
    #products
    path('table/products/<str:id_market>/', view_products.ProductListTableAPIView.as_view(), name='api-product-list-table'),
    path('table/orders/<str:id_market>/', view_orders.OrdersListTableAPIView.as_view(), name='api-order-list-table'),
    path('table/orders/historic/<str:id_market>/', view_orders.OrdersHistoricListTableAPIView.as_view(), name='api-order-historic-list-table'),
]