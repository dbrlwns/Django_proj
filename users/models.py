from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    # default field : password, username, last_login, date_joined
    #                   email, username
    phone = models.CharField(max_length=11, blank=True, null=True)
    posts = models.IntegerField(default=0)

    profile_img = models.ImageField(upload_to='userImages/', blank=True, null=True)


    def __str__(self):
        return self.username
