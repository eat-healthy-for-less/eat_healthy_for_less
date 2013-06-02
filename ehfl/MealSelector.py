
import random
import math

from ehfl import recipe

#### WARNING: I've not really written python, so please yell at me about style!! -Joseph

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

    def __init__(self, ingredients, nutrition, convenience, tags=[]):
        self.ingredients = ingredients
        self.nutrition = nutrition
        self.convenience = convenience

##### type Menu = [Meal] ##### (I can't write this in Python, but the spirit is still there)

#simple sums of conveniences and nutritions
menu_nutrition = lambda menu : sum(map(lambda m: m.nutrition, menu))
menu_convenience = lambda menu : sum(map(lambda m: m.convenience, menu))

class MealPenalizer:
    """
    A class for computing the penalty of a Menu.  requires a budget and
    coefficients of each part of the penalty (b_pen,c_pen,n_pen), so one
    can choose to prioritze health, convenience or cost.  The attribute
    base_prices_fun :: (Ingredient,Amount) -> Price
    """
    def __init__(self, budget, b_pen=10000, c_pen=1, n_pen=1800):
        # b_pen: penalty per dollar over budget
        # c_pen: penalty per second of cooking time
        # n_pen: penalty for going from best healthy recipe to median
        self.budget = budget
        self.budget_penalty = b_pen
        self.nutrition_penalty = n_pen
        self.convenience_penalty = c_pen

    def penalty(self, menu):
        b_pen = self.budget_penalty * max(0, recipe.get_menu_price(menu) - self.budget)
        n_pen = self.nutrition_penalty * menu_nutrition(menu)
        c_pen = self.convenience_penalty * menu_convenience(menu)
        return b_pen - n_pen + c_pen


class SelectionDriver:
    """
    SelectionDriver takes a list of menus and a penalty function and
    picks a 'good' menu based on Trey's randomized hill-climbing
    algorithm.

    penalty_fun :: Menu -> Double
    The function pick_menu is really the only 'public' one.
    It takes a list of meals and returns a 'good' menu.

    usage:
       my_menu = SelectionDriver(mp.penalty).pick_menu(meals)

    where meals :: [Meal], mp :: MealPenalizer
    """

    num_iters = DEFAULT_NUM_ITERS
    num_episodes = DEFAULT_NUM_EPISODES
    menu_size = DEFAULT_DAYS_PER_WEEK

    def __init__(self, penalty_fun)
        self.penalty = penalty_fun

    def random_menu(self,meals):
        return map(lambda x:random.choice(meals),range(self.menu_size))

    def optimize_episode(self,menu,meals):
        pen = self.penalty(menu)
        for i in xrange(self.num_iters):
            newMenu = map(lambda x: x, menu)
            newMenu[random.randint(0, len(menu) - 1)] = random.choice(meals)
            p = self.penalty(newMenu)
            if p < pen:
                pen  = p
                menu = newMenu
        return menu

    def pick_menu(self,meals):
        return min(map(lambda menu: self.optimize_episode(self.random_menu(meals),meals),
                       range(self.num_episodes)),
                   key=self.penalty)
