from django.urls import path, include
from api import views


urlpatterns = [
    path('categories/', views.CategoryListAPIView.as_view(), name='api-categories'),
    path('markets/', views.MarketCreateAPIView.as_view(), name='api-markets-create'),
    path('markets/<str:longitude>/<str:latitude>/', views.MarketListAPIView.as_view(), name='api-markets-list'),
    path('phones/', views.PhoneCreateAPIView.as_view(), name='api-phones-create'),
]