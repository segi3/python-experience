import random

class Spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type
    
    def generate_damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low, high)
    
    def get_name(self):
        return self.name
    
    def get_cost(self):
        return self.cost
    
    def get_type(self):
        return self.type