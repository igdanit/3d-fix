from django.db import models
from decimal import Decimal


def json_default():
    return {}


def price_default():
    return Decimal(0.00)


def available_default():
    return False


class Parts(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=price_default)
    available = models.BooleanField(default=available_default)
    description = models.TextField(default='')
    specifications = models.JSONField(default=json_default)
    category = models.CharField(max_length=30)
    subcategory = models.CharField(max_length=30)

    def __repr__(self):
        return self.title


class Printer(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=price_default)
    available = models.BooleanField(default=available_default)
    description = models.TextField(default='')
    specifications = models.JSONField(default=json_default)
    manufacturer = models.CharField(max_length=30)
    kinematics_type = models.CharField(max_length=20)

    def __repr__(self):
        return self.title


class Filament(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=11, decimal_places=2, default=price_default)
    available = models.BooleanField(default=available_default)
    description = models.TextField(default='')
    specifications = models.JSONField(default=json_default)
    type_of_filament = models.CharField(max_length=20)
    diameter = models.DecimalField(max_digits=4, decimal_places=2)
    color = models.CharField(max_length=30)

    def __repr__(self):
        return self.title
