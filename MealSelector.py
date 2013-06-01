import random

DEFAULT_NUM_ITERS = 100
DEFAULT_NUM_EPISODES = 100
DEFAULT_DAYS_PER_WEEK = 7
DEFAULT_NUM_MEALS = 100


class Meal:
    price = 0
    nutrition = 0
    convinience = 0
    tags = []
    def __init__(self, price, nutrition, convinience,tags=[]):
        self.price = price
        self.nutrition = nutrition
        self.convinience = convinience
        self.tags = tags
        
def random_meals():
    return map(lambda x:Meal(random.randint(10,30),
                             random.uniform(-1,1),
                             random.random()),
               range(DEFAULT_NUM_MEALS))

class MealSelector:
    budget =0
    budget_penalty=0
    nutrition_penalty=0
    convinience_penalty=0
    tag_reqs=[]
    num_iters=DEFAULT_NUM_ITERS
    num_episodes=DEFAULT_NUM_EPISODES
    menu_size=DEFAULT_DAYS_PER_WEEK
    def __init__(self,budget,b_pen,c_pen,n_pen):
        self.budget = budget
        self.budget_penalty=b_pen
        self.nutrition_penalty=n_pen
        self.convinience_penalty=c_pen
    def penalty(self,menu):
        b_pen = self.budget_penalty*max(0,sum(map(lambda m: m.price,menu))-self.budget)
        n_pen = self.nutrition_penalty*sum(map(lambda m: m.nutrition,menu))
        c_pen = self.convinience_penalty*sum(map(lambda m: m.convinience,menu))
        return b_pen-n_pen+c_pen
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
            
    
