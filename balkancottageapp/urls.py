from . import views
from django.urls import path
from .views import CreateReservation

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation/', views.CreateReservation.as_view(), name='reservation'),
    path('my_reservation/', views.CreateReservation.as_view(), name='my_reservation'),

]
