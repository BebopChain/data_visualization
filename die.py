from random import randint

class Die():
    """class to represent a dice"""
    def __init__(self, num_sides=6):
        """dice are set to six sides by default"""
        self.num_sides = num_sides
        
    def roll(self):
        """return a random value between 1 and dice sides"""
        return randint(1, self.num_sides)
    