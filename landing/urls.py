from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.LandingKyperView.as_view(), name='landing_page'),
    path('create_kyper/', views.LandingCreateKyperView.as_view(), name='create_kyper_landing'),
]