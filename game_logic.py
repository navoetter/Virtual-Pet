class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 90
        self.energy = 100
        self.happiness = 100
        self.alive = True
        self.sleeping = False
        self.level = 1

    def to_dict(self):
        return {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "alive": self.alive,
            "sleeping": self.sleeping,
            "level": self.level
        }

    @classmethod
    def from_dict(cls, data):
        pet = cls(data["name"])
        pet.hunger = data["hunger"]
        pet.energy = data["energy"]
        pet.happiness = data["happiness"]
        pet.alive = data["alive"]
        pet.sleeping = data["sleeping"]
        pet.level = data["level"]
        return pet

    def feed(self):
        if self.sleeping or not self.alive:
            return
        self.hunger += 10
        self.happiness += 2

    def play(self, score):
        if self.sleeping or not self.alive:
            return
        self.happiness += score * 2
        self.energy -= 5

    def sleep(self):
        if not self.alive:
            return
        self.sleeping = True

    def tick(self):
        if not self.alive:
            return

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