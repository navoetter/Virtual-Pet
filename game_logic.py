class Pet:
    def __init__(self, name):
        self.name = name

        self.hunger = 90
        self.energy = 100
        self.happiness = 100

        self.alive = True
        self.sleeping = False

        self.level = 1
        self.level_timer = 0

    def feed(self):
        if self.sleeping:
            return
        self.hunger += 10
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

        self.level_timer += 1

        if self.sleeping:
            self.energy += 3

            if self.energy >= 100:
                self.energy = 100
                self.sleeping = False

            return

        self.hunger -= 1
        self.energy -= 1
        self.happiness -= 0.5

        self.hunger = max(0, min(self.hunger, 100))
        self.energy = max(0, min(self.energy, 100))
        self.happiness = max(0, min(self.happiness, 100))

        if self.hunger <= 0 or self.energy <= 0:
            self.alive = False