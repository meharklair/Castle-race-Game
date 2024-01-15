'''
Diamond object for the players to collect throughout the castle
Author: Mehar Klair
Date: 2023-04-06
'''

class Diamond:
    ''' represents a diamond object'''
    def __init__(self, diamonds:int = 1):
        ''' initializes the diamond class'''
        self.diamonds = diamonds
    def __str__(self):
        ''' returns a string repr of diamonds'''
        return f'Number of diamonds {self.diamonds}'
    def get_diamonds(self):
        ''' returns the number of diamonds'''
        return self.diamonds
    def set_diamonds(self, diamonds: int):
        ''' sets the number of diamonds'''
        if diamonds < 0:
            raise Exception('cannot have negative diamonds')
        self.diamonds = diamonds