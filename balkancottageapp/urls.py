from . import views
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from .views import CreateReservation, MyReservations, Menu, UpdateReservation

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
    path('reservation/', views.CreateReservation.as_view(), name='reservation'),
    path('my_reservations/', views.MyReservations.as_view(), name='my_reservations'),
    path('update_reservation/<int:pk>/update/', views.UpdateReservation.as_view(), name='update_reservation'),
    path('delete/<reservation_id>', views.delete_reservation, name='delete'),

]
