from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField



STATUS = ((0, "Draft"), (1, "Published"))


class Home(models.Model):

    welcome_page = models.CharField(max_length=120)


# Model for the Menu which is created by the Admin
class Menu(models.Model):
    dish_name = models.CharField(max_length=130)
    image = CloudinaryField('image', default='')
    content = models.CharField(max_length=200)
    status = models.IntegerField(choices=STATUS, default=0)



# Reservation model

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    message = models.TextField(default='Special requests, alergies etc.', max_length=300)
