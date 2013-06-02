
import json
import sys

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from ehfl.forms import MenuPreferencesForm
from ehfl.MealResult import MealResult, FakeResult
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
    for m in menu:
        m.est_price = m.get_display_price(calories_per_meal)

    alternate_meals = [r for r in recipes if r not in menu]
    for m in alternate_meals:
        m.est_price = m.get_display_price(calories_per_meal)

    # debug
    print >> sys.stderr, 'menu:', [r.name for r in menu]

    return render(request, 'results.html')


def results(request):
   """Results Page"""
   # test_result = json.loads(test_res())
   # result_set = [test_result]*7
   # return_set = list()
   # for result in result_set:
   #    res = dict()
   #    res['id'] = 1
   #    res['name'] = result['name']
   #    image_list = result['images']
   #    res['img'] = image_list[0]['hostedSmallUrl']
   #    res['url'] = result['attribution']['url']
   #    res['est_price'] = "100"
   #    res['cook_time'] = "100"
   #    print res
   #    return_set.append(res)
   x = MealResult()
   return_set = [x]*7
   return render(request, 'results.html',{'results_set':return_set})

def savemenu(request):
  meal_set = [request.GET.get('meal-1'), request.GET.get('meal-2'),
  request.GET.get('meal-3'),request.GET.get('meal-4'),request.GET.get('meal-5'),
  request.GET.get('meal-6'),request.GET.get('meal-7')]
  res_set = list()
  for id in meal_set:
    pass
    #TODO: get python mealresults from id's
    # combine with shopping list

def shoppinglist(request):
    """
    Presents the shoppinglist page for user input
    """
    test_result = json.loads(test_res())
    result_set = [test_result]*14
    return_set = list()
    for result in result_set:
       res = dict()
       res['name'] = result['name']
       image_list = result['images']
       res['img'] = image_list[0]['hostedSmallUrl']
       res['url'] = result['attribution']['url']
       res['est_price'] = "200"
       res['cook_time'] = "100"
       res['ingredient'] = result['ingredientLines']


       print res
       return_set.append(res)

    return render(request, 'shoppinglist.html', {'results_set':return_set})

    """return render(request, 'shoppinglist.html')"""
