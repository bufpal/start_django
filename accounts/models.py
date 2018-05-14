from django.conf import settings
from django.db import models
# from django.contrib.auth.models import User
from django.forms import ValidationError

# def phone_validator(value):
#     if not re.match(r'^$', value):
#         raise ValidationError('Wrong \"Phone Number\" format')

class Profile(models.Model):
    # user = models.OneToOneField(User) #FIX: BadCase
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    phone_number = models.CharField(max_length=20,
        # validators=[phone_validator]    
    )
    address = models.CharField(max_length=50)

    # def __str__(self):
    #     self.user