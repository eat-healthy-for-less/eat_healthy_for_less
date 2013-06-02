class MealResult:

    def __init__(self):
        self.id = 1
        self.name = 'Mushroom Casserole'
        self.img = 'http://i.yummly.com/Mushroom-casserole-308810-272984.s.jpg'
        self.url = 'http://www.yummly.com/recipe/Mushroom-casserole-308810'
        self.est_price = 100 #dollars
        self.cook_time = 100 #mins
        # self.alterns = [MealResult()] * 5 # does not work bc recursion depth

    def get_alterns():
        """
        Return a list of alternatives for this MealResult,
        essentially all meals that match criteria, but are not this meal
        """
        return [MealResult()]*5