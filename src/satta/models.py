from django.db import models


class IntegerRangeField(models.IntegerField):
    def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        models.IntegerField.__init__(self, verbose_name, name, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value':self.max_value}
        defaults.update(kwargs)
        return super(IntegerRangeField, self).formfield(**defaults)


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


class Slot(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
        null=False
    )
    order = models.IntegerField(
        unique=True,
        null=False
    )
    time_of_day = models.TimeField(
        auto_now=True,
        null=False
    )
    result_delta = IntegerRangeField(
        default=0,
        min_value=0,
        max_value=299
    )