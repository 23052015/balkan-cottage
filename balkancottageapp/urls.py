from . import views
from django.urls import path
from .views import CreateReservation, MyReservations, Menu

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation/', views.CreateReservation.as_view(), name='reservation'),
    path('my_reservations/', views.MyReservations.as_view(), name='my_reservations'),

]
