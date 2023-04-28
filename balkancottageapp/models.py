from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))


class Home(models.Model):

    welcome_page = models.CharField(max_length=120)


# Model for the Menu which is created by the Admin
class Menu(models.Model):
    dish_name = models.CharField(max_length=130)
    extra = models.CharField(max_length=130)
    description = models.CharField(max_length=200)
    price = models.FloatField()
    image = CloudinaryField('image', default='')
    content = models.CharField(max_length=999)
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

# Table Model


class Table(models.Model):
    TABLE_CHOICES = (
        ('4', '4 persons'),
        ('8', '8 persons'),
        ('10', '10 persons'),
    )
    table_number = models.IntegerField(unique=True)
    capacity = models.CharField(max_length=2, choices=TABLE_CHOICES)
    is_available = models.BooleanField(default=True)

# Comments from registered Users


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='liked_comments')
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Commented by {self.user.username}'


