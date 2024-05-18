from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    image = models.ImageField(upload_to='user_images', blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    class Meta:
        db_table = 'user'