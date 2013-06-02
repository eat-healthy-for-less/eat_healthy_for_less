
from django.db import models


class QuantityUnit(models.Model):
    """
    Example: cups, tablespoons, pounds

    There is a special QuantityUnit (id 1) to use if there is no natural
    unit (like "2 onions").  Its name is the empty string.
    """
    name = models.CharField(max_length=160, blank=True)

    def __unicode__(self):
        return '%s: %s' % (self.id, self.name)


class QuantityUnitConversion(models.Model):
    you_have = models.ForeignKey('QuantityUnit', related_name='conversion_you_have')
    you_want = models.ForeignKey('QuantityUnit', related_name='conversion_you_want')
    multiply_by = models.FloatField()


class Ingredient(models.Model):
    name = models.CharField(max_length=160)
    price_per_kg = models.FloatField(null=True, blank=True)
    density = models.FloatField(default=1.0)

    def __unicode__(self):
        return (u'%s: Ingredient(%s, price_per_kg=%s, density=%s)'
                % (self.id,
                   self.name,
                   self.price_per_kg,
                   self.density))
