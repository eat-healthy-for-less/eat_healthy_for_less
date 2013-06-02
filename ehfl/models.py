
from django.db import models


class QuantityUnit(models.Model):
    """
    Example: cups, tablespoons, pounds

    There is a special QuantityUnit (id 1) to use if there is no natural unit (like "2 onions").
    Its name is the empty string.
    """
    name = models.CharField(max_length=160)


class QuantityUnitConversion(models.Model):
    you_have = models.ForeignKey('QuantityUnit', related_name='conversion_you_have')
    you_want = models.ForeignKey('QuantityUnit', related_name='conversion_you_want')
    multiply_by = models.FloatField()


class Ingredient(models.Model):
    name = models.CharField(max_length=160)
    quantity_unit = models.ForeignKey('QuantityUnit')
    price = models.FloatField()
