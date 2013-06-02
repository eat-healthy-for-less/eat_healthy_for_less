#!/usr/bin/env python

import os
import sys
import json
import numpy

# HACK HACK
os.environ['DJANGO_SETTINGS_MODULE'] = 'ehfl.settings'
PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
sys.path.insert(0, PARENT_DIR)

from glob import glob

from ehfl.models import Ingredient
from ehfl.recipe import read_recipes

recipes = read_recipes()

print 'MIN_SATURATED_FAT_PER_CALORIE =', min([r.saturated_fat_per_calorie for r in recipes])
print 'MAX_SATURATED_FAT_PER_CALORIE =', max([r.saturated_fat_per_calorie for r in recipes])

# constraint thresholds
print 'MAX_SODIUM_PER_CALORIE =', numpy.median([r.sodium_per_calorie for r in recipes])
print 'MAX_SUGAR_PER_CALORIE =', numpy.median([r.sugar_per_calorie for r in recipes])
print 'MIN_FIBER_PER_CALORIE =', numpy.median([r.fiber_per_calorie for r in recipes])

for r in recipes:
    #print r.name, r.get_bulk_price_per_calorie()
    print r.name, r.convenience, r.nutrition

