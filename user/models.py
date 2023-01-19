from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.PositiveBigIntegerField(null=True)
    hobby = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = "user"
