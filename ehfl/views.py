
import json
import sys

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from ehfl.forms import MenuPreferencesForm
from ehfl.recipe import read_recipes, ingredientRetailPrice, INGREDIENTS, convertToKilos
from ehfl import MealSelector
from ehfl import recipe


def index(request):
    return HttpResponseRedirect('/setup/')


def setup(request):
    if request.method == 'POST':
        form = MenuPreferencesForm(request.POST)
        if form.is_valid():
            return menu(request, form)
        else:
            return render(request, 'setup.html', {'form': form})
    elif request.method == 'GET':
        return render(request, 'setup.html')
    else:
        raise Exception()


def menu(request, form):
    calories_per_day = form.cleaned_data['calories_per_day']
    budget = form.cleaned_data['budget']
    address = form.cleaned_data['address']

    constraint_names = []
    for constraint_name in ('low_sugar', 'high_fiber', 'low_sodium'):
        if form.cleaned_data[constraint_name]:
            constraint_names.append(constraint_name)

    # choose recipes that match constraints
    recipes = recipe.read_recipes()
    recipes = [r for r in recipes
               if r.satisfies_constraints(constraint_names)]

    calories_per_meal = calories_per_day * 0.75
    menu = MealSelector.select_optimal_menu(recipes, budget, calories_per_meal)
    alternate_meals = [r for r in recipes if r not in menu]
    for m in alternate_meals:
        m.est_price = m.get_display_price(calories_per_meal)
        m.est_price = str(m.get_display_price(calories_per_meal))[:5]
        m.cook_time = m.convenience/60
        m.img = m.images[0]['hostedSmallUrl']
    for m in menu:
        m.est_price = str(m.get_display_price(calories_per_meal))[:5]
        m.cook_time = m.convenience/60
        m.img = m.images[0]['hostedSmallUrl']
        m.alterns = alternate_meals
    # debug
    print >> sys.stderr, 'menu:', [r.name for r in menu]
    return render(request, 'results.html', {'results_set':menu, 'cals':calories_per_meal})

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
    res_list = list()
    for ing_name, qty_kg in ing_qty_kg.iteritems():
        res_list.append([ing_name, str(qty_kg)[:5], str(ingredientRetailPrice(qty_kg, 'kilograms', ing_name))[:7]])
        price += ingredientRetailPrice(qty_kg, 'kilograms', ing_name)

    return res_list, str(price)[:6]


def savemenu(request):
  meal_set = [request.GET.get('meal-1'), request.GET.get('meal-2'),
  request.GET.get('meal-3'),request.GET.get('meal-4'),request.GET.get('meal-5'),
  request.GET.get('meal-6'),request.GET.get('meal-7')]
  cals = float(request.GET.get('cals'))
  recipe_set = list()
  recipes = dict(((i.name, i) for i in read_recipes()))
  # print recipes.keys()
  for id in meal_set:
    recipe_set.append(recipes[id])
  res_set, price = get_menu_price(recipe_set, cals)
  print res_set, price
  return render(request, 'shoppinglist.html', {'results_set':res_set, 'total':price})
