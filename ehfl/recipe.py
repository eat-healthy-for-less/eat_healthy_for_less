
import os
import json

from glob import glob

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
RECIPES_DIR = PARENT_DIR + 'recipes/'

def read_recipe(path):
    return json.loads(open(path, 'r').read())


def read_recipes():
    paths = glob(RECIPES_DIR + '*.json')
    return [read_recipe(p) for p in paths]


