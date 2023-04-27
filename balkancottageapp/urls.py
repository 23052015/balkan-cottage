from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePage.as_view(), name='home'),
    path('menu', views.MenuList.as_view(), name='menu'),
]
