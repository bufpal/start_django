from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User


class Profile(models.Model):
    # user = models.OneToOneField(User) #FIX: BadCase
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20)
    address = models.CharField(max_length=50)

    # def __str__(self):
    #     self.user