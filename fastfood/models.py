from django.db import models

# Create your models here.


class Booking_food(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=230)
    phone_no = models.IntegerField()
    dish = models.CharField(max_length=20)


class Dishes(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='dish_img')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField()