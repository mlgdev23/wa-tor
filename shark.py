from creature import Creature

SHARK_BREED_INTERVAL = 5 #eventually user-defined - move to wator.py
SHARK_ENERGY = 10 #eventually user-defined - move to wator.py

class Shark(Creature):
    def __init__(self, x, y): #eventually add user-defined command-line data.
        self.x = x
        self.y = y
        self.breed_interval = SHARK_BREED_INTERVAL
        self.breed_counter = 0
        self.energy = SHARK_ENERGY
        Creature.all_creatures.append(self)
