from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone = models.PositiveBigIntegerField(null=True)
    about = models.TextField(null=True)

    class Meta(AbstractUser.Meta):
        db_table = "users"
