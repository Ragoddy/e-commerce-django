from django.urls import path, include
from . import views


urlpatterns = [
    path('kyper/', views.LandingKyperView.as_view(), name='landing_page_kyper'),
    path('', views.LandingUserView.as_view(), name='landing_page_user'),
    path('create_kyper/', views.LandingCreateKyperView.as_view(), name='create_kyper_landing'),
]