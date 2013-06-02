
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
    quantity_unit = models.ForeignKey('QuantityUnit', null=True, blank=True)
    price = models.FloatField(null=True, blank=True)

    def __unicode__(self):
        if self.quantity_unit is None:
            qname = None
        else:
            qname = self.quantity_unit.name
        return (u'%s Ingredient(%s, %s, %s)'
                % (self.id,
                   self.name,
                   qname,
                   self.price))
