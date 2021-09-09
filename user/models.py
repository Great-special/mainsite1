from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User_Details(models.Model):
    main_user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=200)
    address = models.CharField(max_length=230)
    phone_no = models.CharField(max_length=11)
    email = models.EmailField()

    GENDER = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    gender = models.CharField(max_length=2, choices=GENDER)

