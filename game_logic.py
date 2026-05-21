import time


class Pet:
    def __init__(self, name):
        self.name = name

        self.hunger = 50
        self.energy = 100
        self.happiness = 100

        self.alive = True

        self.sleeping = False

    def feed(self):
        if self.sleeping:
            return
        self.hunger -= 10
        self.happiness += 2

    def play(self, score):
        if self.sleeping:
            return
        self.happiness += score * 2
        self.energy -= 5

    def sleep(self):
        self.sleeping = True

    def tick(self):

        if not self.alive:
            return

        # SLEEP MODE
        if self.sleeping:
            self.energy += 3

            if self.energy >= 100:
                self.energy = 100
                self.sleeping = False

            return

        # NORMAL MODE
        self.hunger += 1
        self.energy -= 1
        self.happiness -= 0.5

        self.hunger = min(self.hunger, 100)
        self.energy = max(self.energy, 0)
        self.happiness = max(self.happiness, 0)

        if self.hunger >= 100 or self.energy <= 0:
            self.alive = False