
import os
import json
import sys
import math

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
        # print >> sys.stderr, 'warning: unknown unit "%s"' % unit
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


def get_menu_price(recipes, calories_per_meal):
    ing_qty_kg = {}
    for r in recipes:
        scaling_factor = calories_per_meal / r.calories
        for qty, unit, ing_name in r.ingredientLines:
            ing = INGREDIENTS[ing_name]
            qty_kg = scaling_factor * convertToKilos(qty, unit, ing.density)
            old_qty = ing_qty_kg.get(ing_name, 0.0)
            ing_qty_kg[ing_name] = old_qty + qty_kg

    price = 0.0
    for ing_name, qty_kg in ing_qty_kg.iteritems():
        price += ingredientRetailPrice(qty_kg, 'kilograms', ing_name)

    return price

MIN_SATURATED_FAT_PER_CALORIE = 0.00358961974181
MAX_SATURATED_FAT_PER_CALORIE = 0.042421544625

MAX_SODIUM_PER_CALORIE = 0.00166074486301
MAX_SUGAR_PER_CALORIE = 0.0101351028251
MIN_FIBER_PER_CALORIE = 0.00753173084391

class Recipe(object):
    def __init__(self, stuff):
        for k, v in stuff.iteritems():
            setattr(self, k, v)
        self.nutritionEstimates = dict([(rec['attribute'], rec)
                                        for rec in self.nutritionEstimates])
        self.calories = self.nutritionEstimates['ENERC_KCAL'].value
        self.sodium_per_calorie = float(self.nutritionEstimates['NA'].value) / self.calories
        self.sugar_per_calorie = float(self.nutritionEstimates['SUGAR'].value) / self.calories
        self.fiber_per_calorie = float(self.nutritionEstimates['FIBTG'].value) / self.calories
        self.saturated_fat_per_calorie = float(self.nutritionEstimates['FASAT'].value) / self.calories
        indicator = (float(MAX_SATURATED_FAT_PER_CALORIE - self.saturated_fat_per_calorie)
                     / (MAX_SATURATED_FAT_PER_CALORIE - MIN_SATURATED_FAT_PER_CALORIE))
        self.nutrition = 2 * indicator - 1.0

        self.convenience = getattr(self, 'totalTimeInSeconds')
        if self.convenience is None:
            self.convenience = 1800

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

    def get_display_price(self, calories_per_meal):
        return self.get_bulk_price_per_calorie() * calories_per_meal

    def satisfies_constraint(self, constraint_name):
        if constraint_name == 'low_sodium':
            return self.sodium_per_calorie < MAX_SODIUM_PER_CALORIE
        elif constraint_name == 'low_sugar':
            return self.sugar_per_calorie < MAX_SUGAR_PER_CALORIE
        elif constraint_name == 'high_fiber':
            return self.fiber_per_calorie > MIN_FIBER_PER_CALORIE

    def satisfies_constraints(self, constraint_names):
        return all((self.satisfies_constraint(n) for n in constraint_names))


def read_recipe(path):
    return Recipe(convertToDotDictRecurse(json.loads(open(path, 'r').read())))


def read_recipes():
    paths = glob(RECIPES_DIR + '*.json')
    return [read_recipe(p) for p in paths]
