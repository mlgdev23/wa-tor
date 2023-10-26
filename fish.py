from creature import Creature

FISH_BREED_INTERVAL = 10 #eventually set by user

class Fish(Creature):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.breed_interval = FISH_BREED_INTERVAL
        self.breed_counter = 0
        Creature.all_creatures.append(self)