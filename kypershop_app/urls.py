"""kypershop_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path

from django.conf import settings
from django.conf.urls.static import static

#DFR Lib´s
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework.authtoken import views 


schema_view = get_schema_view(
   openapi.Info(
      title="Kypershop API",
      default_version='v1',
      description="Kypershop API for Mobile",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    
    #ADMIN
    path('administrator_app/', admin.site.urls),
    path('accounts/', include('allauth.urls')),    
    
    #WEB
    path('', include('landing.urls')),
    path('search/', include('front.urls')),
    path('web/markets/', include('front_market.urls')),   
    
    
    #API
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('api-token-auth/', views.obtain_auth_token, name='api-tokn-auth'),
    re_path('api/(?P<version>(v1))/', include('api.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                    document_root=settings.MEDIA_ROOT)
