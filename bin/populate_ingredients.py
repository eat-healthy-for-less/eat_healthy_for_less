#!/usr/bin/env python

import os
import sys
import json

# HACK HACK
os.environ['DJANGO_SETTINGS_MODULE'] = 'ehfl.settings'
PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
sys.path.insert(0, PARENT_DIR)

from glob import glob

from ehfl import models
from ehfl.recipe import read_recipes

recipes = read_recipes()
print json.dumps(recipes, sort_keys=True, indent=4)
