from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(
        max_length=255,
        null=False
    )
    user_type = models.CharField(
        max_length=255,
        null=False
    )
    mobile_number = models.IntegerField(
        null=False
    )
    user_id = models.CharField(
        max_length=255,
        unique=True,
        null=False
    )
    password = models.CharField(
        max_length=255,
        null=False
    )