from django.urls import path
from . import views

urlpatterns = [
    path('', views.page_dashboard, name='dashboard'),
]

