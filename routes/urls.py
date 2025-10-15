# flight_routes/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.flight_routes_view, name='main'),
]