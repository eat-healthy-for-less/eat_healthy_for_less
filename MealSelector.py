import random
import math


#### WARNING: I've not really written python, so please yell at me about style!!

DEFAULT_NUM_ITERS = 100
DEFAULT_NUM_EPISODES = 100
DEFAULT_DAYS_PER_WEEK = 7
DEFAULT_NUM_RANDOM_MEALS = 100

class Meal:
    """
    a class representing a single meal.
    ingredients is either a dictionary or an a-list associating ingredients to
    amounts, where amount is the actual amount divided by the smallest amount one can buy
    nutrition and convenience go on an arbitrary scale.
    """

    def __init__(self, ingredients, nutrition, convenience,tags=[]):
        self.ingredients = ingredients
        self.nutrition = nutrition
        self.convenience = convenience


##### type Menu = [Meal] ##### (I can't write this in Python, but the spirit is still there)



# determines the price of the menu, given a price_per function.
# price_per takes two arguments, an ingrediant and an amount, and returns the price you would need to pay for that in a store.
# for instance, if you need 5 units of something and you can only buy that in powers of 2, price_per(that_ingrediant,5) returns the price of buying 8 units.
# menu is a list of meals.
def menu_price(price_per,menu):
    result = {}
    for m in menu:
        for ing, val in m.ingredients:
            if result.has_key(ing):
                result[ing] = result[ing]+val
            else:
                result[ing] = val
    return sum(map(lambda p: price_per(p[0],p[1]),result.items()))

#simple sums of conveniences and nutritions
menu_nutrition = lambda menu : sum(map(lambda m: m.nutition,menu))
menu_convenience = lambda menu : sum(map(lambda m: m.convenience,menu))

# an implementation of Trey's pricing algorithm, where price_fun(ing) returns the price-per-unit of an infinite amount of ing
# perhaps a good default base_prices_fun
def logarithmic_pricing(price_fun,ing,amt):
    log_amt_needed = math.ceil(math.log(amt))
    price_multiplier = 2-sum(map(lambda i:1.0/2**(i+1),
                                 range(log_amt_needed)))
    return price_fun(ing)*(2**log_amt_needed)*price_multiplier

class MealPenalizer:
    """
    A class for computing the penalty of a Menu.
    requires a budget and coefficients of each part of the penalty (b_pen,c_pen,n_pen), so one can choose to prioritze health, convenience or cost.
    The attribute base_prices_fun :: (Ingrediant,Amount) -> Price
    """
    def __init__(self,budget,b_pen,c_pen,n_pen,base_prices_fun):
        self.budget = budget
        self.budget_penalty=b_pen
        self.nutrition_penalty=n_pen
        self.convenience_penalty=c_pen
        self.base_prices_fun = base_prices_fun
    tag_reqs=[]
    def penalty(self,menu):
        b_pen = self.budget_penalty*max(0,menu_price(menu,self.base_prices_fun))-self.budget)
        n_pen = self.nutrition_penalty*menu_nutrition(menu)
        c_pen = self.convenience_penalty*menu_convenience(menu)
        return b_pen-n_pen+c_pen

class SelectionDriver:
    """
    SelectionDriver takes a list of menues and a penalty function and picks a 'good' menu based on Trey's randomized hill-climbing algorithm.
    penalty_fun :: Menu -> Double
    The function pick_menu is really the only 'public' one.
    It takes a list of meals and returns a 'good' menu.
    usage:
       my_menu = SelectionDriver(mp.penalty).pick_menu(meals)
    where meals :: [Meal], mp :: MealPenalizer
    """
    num_iters=DEFAULT_NUM_ITERS
    num_episodes=DEFAULT_NUM_EPISODES
    menu_size=DEFAULT_DAYS_PER_WEEK
    def __init__(self,penalty_fun)
        self.penalty = penalty
    def random_menu(self,meals):
        return map(lambda x:random.choice(meals),range(self.menu_size))
    def optimize_episode(self,menu,meals):
        pen = self.penalty(menu)
        for i in range(self.num_iters):
            newMenu = map(lambda x:x,menu)
            newMenu[random.randint(0,len(menu)-1)] = random.choice(meals)
            p = self.penalty(newMenu)
            if(p<pen):
                pen  = p
                menu = newMenu
        return menu
    def pick_menu(self,meals):
        return min(map(lambda menu: self.optimize_episode(self.random_menu(meals),meals),
                       range(self.num_episodes)),
                   key=self.penalty)

