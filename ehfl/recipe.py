
import os
import json
import sys

from glob import glob

from ehfl.models import Ingredient

PARENT_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '')
RECIPES_DIR = PARENT_DIR + 'recipes/'


def convertToDotDictRecurse(struct):
    if isinstance(struct, dict):
        for k, v in struct.iteritems():
            struct[k] = convertToDotDictRecurse(v)
        return DotDict(struct)
    elif isinstance(struct, list):
        return [convertToDotDictRecurse(elt) for elt in struct]
    else:
        return struct


class DotDict(dict):
    # At the moment this object exists pretty much solely to let you
    # get and set elements in its __dict__ dictionary via dotted
    # notation.  Someday it could do more.

    # these are fields that must not be defined to avoid causing problems
    # with Django
    _badFields = ('prepare_database_save',)

    def copy(self):
        return DotDict(self)

    def __repr__(self):
        return json.dumps(self, sort_keys=True, indent=4)

    def __getattr__(self, attr):
        if attr.startswith('__'):
            raise AttributeError(attr)  # avoids breaking copy.deepcopy
        if attr in self._badFields:
            raise KeyError(attr)
        return self.get(attr, None)
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__


# conversion to liters
VOLUME_UNITS = {
    'liters': 1.0,
    'cups': 0.23658824,
    'tablespoons': 0.014786765,
    'teaspoons': 0.0049289216,
}


# conversion to kilograms
MASS_UNITS = {
    'kilograms': 1.0,
    'pounds': 0.45359237,
    'ounces': 0.028349523,
}


ALL_INGREDIENTS = Ingredient.objects.all()
INGREDIENTS = dict(((i.name, i) for i in ALL_INGREDIENTS))
MIN_RETAIL_SIZE_KG = 0.1

def convertToKilos(qty, unit, density):
    if unit in MASS_UNITS:
        return qty * MASS_UNITS[unit]
    elif unit in VOLUME_UNITS:
        return qty * VOLUME_UNITS[unit] * density
    else:
        # FIXME: this assumes the units are pounds if we don't recognize them, totally invalid
        print >> sys.stderr, 'warning: unknown unit "%s"' % unit
        return qty * MASS_UNITS['pounds']


def ingredientBulkPrice(qty, unit, name):
    ingredient = INGREDIENTS[name]
    return convertToKilos(qty, unit, ingredient.density) * ingredient.price_per_kg


def nextPowerOf2(val):
    return math.pow(2, math.ceil(math.log(val, 2)))


def ingredientRetailPrice(qty, unit, name):
    ingredient = INGREDIENTS[name]
    qty_kg = convertToKilos(qty, unit, ingredient.density)
    retail_size = MIN_RETAIL_SIZE_KG * nextPowerOf2(float(qty_kg) / MIN_RETAIL_SIZE_KG)
    retail_markup = MIN_RETAIL_SIZE_KG / retail_size
    bulk_price = ingredient.price_per_kg
    return bulk_price * (1.0 + retail_markup) * retail_size


def get_menu_price(recipes):
    ing_qty_kg = {}
    for r in recipes:
        for qty, unit, ing_name in self.ingredientLines:
            ing = INGREDIENTS[ing_name]
            qty_kg = convertToKilos(qty, unit, ing.density)
            old_qty = ing_qty_kg.get(ing_name, 0.0)
            ing_qty_kg[ing_name] = old_qty + qty_kg

    price = 0.0
    for ing_name, qty_kg in ing_qty_kg.iteritems():
        price += ingredientRetailPrice(qty_kg, 'kilograms', ing_name)


class Recipe(object):
    def __init__(self, stuff):
        for k, v in stuff.iteritems():
            setattr(self, k, v)
        self.nutritionEstimates = dict([(rec['attribute'], rec)
                                        for rec in self.nutritionEstimates])
        self.calories = self.nutritionEstimates['ENERC_KCAL'].value

    def get_bulk_price_per_calorie(self):
        """
        Returns an estimate of the recipe price per Calorie (Kcal) based
        on the prices of its ingredients, assuming ingredients can be
        purchased in bulk.  (Generally this will underestimate the real
        price somewhat.)
        """
        price = sum((ingredientBulkPrice(qty, unit, name)
                     for qty, unit, name in self.ingredientLines))
        return price / self.calories


def read_recipe(path):
    print path
    return Recipe(convertToDotDictRecurse(json.loads(open(path, 'r').read())))


def read_recipes():
    paths = glob(RECIPES_DIR + '*.json')
    return [read_recipe(p) for p in paths]
