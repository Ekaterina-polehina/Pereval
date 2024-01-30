"""
URL configuration for Pereval_virt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from rest_framework import permissions
from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = "Simple Inventory API",
        default_version = '1.0.0',
        description = "This is a simple API",
        terms_of_service = "https://virtserver.swaggerhub.com/Kati0709_1/Pereval/1.0.0",
        contact=openapi.Contact(email="kati0709@mail.ru"),
        license=openapi.License(name="BSD License"),
    ),
    public = True,
    permission_classes = [permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('pereval.urls')),

]

