
import random
import math
import copy

from ehfl import recipe

#### WARNING: I've not really written python, so please yell at me about style!! -Joseph

DEFAULT_NUM_ITERS = 200
DEFAULT_NUM_EPISODES = 10
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
def menu_nutrition(menu):
    return sum((m.nutrition for m in menu))


def menu_convenience(menu):
    return sum((m.convenience for m in menu))


def counts(vals):
    cnt = {}
    for val in vals:
        if val in cnt:
            cnt[val] += 1
        else:
            cnt[val] = 1
    return cnt


class MealPenalizer:
    """
    A class for computing the penalty of a Menu.  requires a budget and
    coefficients of each part of the penalty (b_pen,c_pen,n_pen), so one
    can choose to prioritze health, convenience or cost.  The attribute
    base_prices_fun :: (Ingredient,Amount) -> Price
    """
    def __init__(self, budget, calories_per_meal, b_pen=10000, c_pen=1, n_pen=1800, s_pen=1e+9):
        # b_pen: penalty per dollar over budget
        # c_pen: penalty per second of cooking time
        # n_pen: penalty for going from best healthy recipe to median
        # s_pen: penalty for having the same meal twice
        self.budget = budget
        self.calories_per_meal = calories_per_meal
        self.budget_penalty = b_pen
        self.nutrition_penalty = n_pen
        self.convenience_penalty = c_pen
        self.same_penalty = s_pen

    def penalty(self, menu):
        b_pen = (self.budget_penalty
                 * max(0,
                       recipe.get_menu_price(menu, self.calories_per_meal)
                       - self.budget))
        n_pen = self.nutrition_penalty * menu_nutrition(menu)
        c_pen = self.convenience_penalty * menu_convenience(menu)

        # calculate same-recipe penalty
        recipe_names = [r.name for r in menu]
        max_count = max(counts(recipe_names).itervalues())
        s_pen = self.same_penalty * (max_count - 1)

        return b_pen - n_pen + c_pen + s_pen


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

    def __init__(self, penalty_fun):
        self.penalty = penalty_fun

    def random_menu(self, recipes):
        return [random.choice(recipes) for _ in xrange(self.menu_size)]

    def optimize_episode(self, menu, recipes):
        pen = self.penalty(menu)
        for i in xrange(self.num_iters):
            newMenu = copy.copy(menu)
            newMenu[random.randint(0, len(menu) - 1)] = random.choice(recipes)
            p = self.penalty(newMenu)
            if p < pen:
                pen  = p
                menu = newMenu
        return menu

    def pick_menu(self, recipes):
        episodes = [self.optimize_episode(self.random_menu(recipes), recipes)
                    for i in xrange(self.num_episodes)]
        return min(episodes, key=self.penalty)


def select_optimal_menu(recipes, budget, calories_per_meal):
    penalizer = MealPenalizer(budget, calories_per_meal)
    driver = SelectionDriver(penalizer.penalty)
    menu = driver.pick_menu(recipes)
    return menu
