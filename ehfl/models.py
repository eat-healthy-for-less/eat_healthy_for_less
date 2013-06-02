
from django.db import models


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
