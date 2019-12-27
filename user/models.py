from django.db import models
from django.contrib.auth.models import AbstractUser
class MyUser(AbstractUser):
    mobilenumber = models.CharField(verbose_name='手机号码', max_length=11)

    def __str__(self):
        return self.username