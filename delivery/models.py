from django.db import models

# Create your models here.


class Booking_delivery(models.Model):
    sender_name = models.CharField(max_length=200)
    sender_address = models.CharField(max_length=230)
    sender_phone_no = models.CharField(max_length=11)

    receiver_name = models.CharField(max_length=200)
    receiver_address = models.CharField(max_length=230)
    receiver_phone_no = models.CharField(max_length=11)

    package_name = models.CharField(max_length=100)
    package_desc = models.TextField()

    location_sender = models.CharField(max_length=100)
    location_receiver = models.CharField(max_length=100)

    urgent = models.BooleanField(default=False)
    tracking_code = models.CharField(max_length=32)
