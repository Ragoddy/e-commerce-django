from django.urls import path, include
from api import views


urlpatterns = [
    path('categories/', views.CategoryListAPIViewSet.as_view(), name='api-categories'),
    path('markets/', views.MarketListAPIViewSet.as_view(), name='api-markets'),
]