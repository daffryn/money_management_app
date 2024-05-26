"""
URL configuration for money_management project.

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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('app_landing.urls')),
    path('login/', include('app_login.urls')),
    path('dashboard/', include('app_dashboard.urls')),
    path('pocket/', include('app_pocket.urls')),
    path('transaction/', include('app_transaction.urls')),
    path('transfer/', include('app_transfer.urls')),
    path('admin/', admin.site.urls),
]
