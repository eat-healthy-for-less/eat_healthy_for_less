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
for r in recipes:
    for qty, unit, name in r.ingredientLines:
        Ingredient.objects.get_or_create(name=name)
