
import json
import sys

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from ehfl.forms import MenuPreferencesForm
from ehfl.MealResult import MealResult, FakeResult
from ehfl import MealSelector


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

    constraints = []
    for constraint_name in ('low_sugar', 'high_fiber', 'low_sodium'):
        if form.cleaned_data[constraint_name]:
            constraints.append(constraint_name)

    calories_per_meal = calories_per_day * 0.75
    menu = MealSelector.select_optimal_menu(budget, calories_per_meal, constraints)
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


def test_res():
	return """{
   "attribution":{
      "html":"<a href='http://www.yummly.com/recipe/Mushroom-casserole-308810'>Mushroom Casserole recipe</a> information powered by <img alt='Yummly' src='http://static.yummly.com/api-logo.png'/>",
      "url":"http://www.yummly.com/recipe/Mushroom-casserole-308810",
      "text":"Mushroom Casserole recipes: information powered by Yummly",
      "logo":"http://static.yummly.com/api-logo.png"
   },
   "ingredientLines":[
      "1/2 pound (8 ounces) brown mushrooms, cleaned and chopped",
      "1 large onion, well chopped",
      "3 cloves garlic, finely chopped",
      "3 cups cooked brown rice, room temperature",
      "2 large eggs",
      "1 cup cottage cheese",
      "1/2 cup sour cream",
      "1/2 teaspoon fine grain sea salt",
      "1/3 cup freshly grated Parmesan cheese",
      "a bit of fresh tarragon, chopped"
   ],
   "flavors":{
      "Sweet":0.001136062666773796,
      "Meaty":0.0013550840085372329,
      "Piquant":0.0,
      "Sour":0.004854891914874315,
      "Bitter":0.013377883471548557,
      "Salty":0.0012329670134931803
   },
   "nutritionEstimates":[
      {
         "attribute":"ENERC_KCAL",
         "description":"Energy",
         "value":697.64,
         "unit":{
            "id":"fea252f8-9888-4365-b005-e2c63ed3a776",
            "name":"calorie",
            "abbreviation":"kcal",
            "plural":"calories",
            "pluralAbbreviation":"kcal"
         }
      },
      {
         "attribute":"FAT",
         "description":"Total lipid (fat)",
         "value":15.67,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"FASAT",
         "description":"Fatty acids, total saturated",
         "value":8.71,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"CHOLE",
         "description":"Cholesterol",
         "value":0.03,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"NA",
         "description":"Sodium, Na",
         "value":0.52,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"K",
         "description":"Potassium, K",
         "value":0.70,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"CHOCDF",
         "description":"Carbohydrate, by difference",
         "value":114.39,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"FIBTG",
         "description":"Fiber, total dietary",
         "value":6.63,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"SUGAR",
         "description":"Sugars, total",
         "value":6.22,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"PROCNT",
         "description":"Protein",
         "value":24.56,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"VITA_IU",
         "description":"Vitamin A, IU",
         "value":358.76,
         "unit":{
            "id":"ed46fe0c-44fe-4c1f-b3a8-880f92e30930",
            "name":"IU",
            "abbreviation":"IU",
            "plural":"IU",
            "pluralAbbreviation":"IU"
         }
      },
      {
         "attribute":"VITC",
         "description":"Vitamin C, total ascorbic acid",
         "value":0.00,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"CA",
         "description":"Calcium, Ca",
         "value":0.24,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      },
      {
         "attribute":"FE",
         "description":"Iron, Fe",
         "value":0.00,
         "unit":{
            "id":"12485d26-6e69-102c-9a8a-0030485841f8",
            "name":"gram",
            "abbreviation":"g",
            "plural":"grams",
            "pluralAbbreviation":"grams"
         }
      }
   ],
   "images":[
      {
         "hostedLargeUrl":"http://i.yummly.com/Mushroom-casserole-308810-272984.l.jpg",
         "hostedSmallUrl":"http://i.yummly.com/Mushroom-casserole-308810-272984.s.jpg"
      }
   ],
   "name":"Mushroom Casserole",
   "attributes":{
      "course":[
         "Side Dishes",
         "Main Dishes"
      ],
      "cuisine":[
         "American"
      ]
   },
   "totalTimeInSeconds":null,
   "rating":5,
   "numberOfServings":4,
   "source":{
      "sourceRecipeUrl":"http://www.101cookbooks.com/archives/mushroom-casserole-recipe.html",
      "sourceSiteUrl":"http://www.101cookbooks.com/",
      "sourceDisplayName":"101 Cookbooks"
   },
   "id":"Mushroom-casserole-308810"
}"""
