from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Home(models.Model):

    welcome_page = models.CharField(max_length=120)


# Model for the Menu which is created by the Admin
class Menu(models.Model):
    dish_name = models.CharField(max_length=130)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = CloudinaryField('image', default='')
    content = models.CharField(max_length=200)
    likes = models.ManyToManyField(
        User, related_name='dish_like', blank=True
        )
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.dish_name

    def number_of_likes(self):
        return self.likes.count()


# Reservation model


class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    table = models.IntegerField()
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
