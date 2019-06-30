from django.urls import path

from . import views

urlpatterns = [
    path('', views.Stations, name='Stations'),
    path('isspassenger/', views.PassengerDetails, name='PassengerDetail'),
    path('isslocation/', views.IssLocation, name='IssLocation'),
]