#!/usr/bin/env python

import os
import sys
import json

# HACK HACK
os.environ['DJANGO_SETTINGS_MODULE'] = 'ehfl.settings'
PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
sys.path.insert(0, PARENT_DIR)

from glob import glob

from ehfl.models import Ingredient
from ehfl.recipe import read_recipes

recipes = read_recipes()
all_ingredients = {}
all_units = {}
for r in recipes:
    for qty, unit, name in r.ingredientLines:
        all_ingredients[name] = True
        all_units[unit] = True
        Ingredient.objects.get_or_create(name=name,
                                         defaults={'price_per_kg': 2.00})

ingredients = list(sorted(all_ingredients.keys()))
print
print 'ALL INGREDIENTS'
print
for ing in ingredients:
    print ing

print
print 'ALL UNITS'
print
units = list(sorted(all_units.keys()))
for unit in units:
    print unit
