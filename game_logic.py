class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 20
        self.energy = 80
        self.happiness = 80
        self.alive = True

        self._tick_counter = 0
        self._tick_rate = 30  

    def tick(self):
        if not self.alive:
            return

        self._tick_counter += 1

        if self._tick_counter < self._tick_rate:
            return

        self._tick_counter = 0

        self.hunger += 1
        self.energy -= 1
        self.happiness -= 0.5

        self._clamp()
        self._check_alive()

    # --- Aktionen ---
    def feed(self):
        if not self.alive:
            return
        self.hunger -= 15
        self._clamp()

    def sleep(self):
        if not self.alive:
            return
        self.energy = 100

    def play(self, won: bool):
        if not self.alive:
            return

        if won:
            self.happiness += 10
        else:
            self.happiness -= 2

        self.energy -= 5
        self._clamp()

    def _clamp(self):
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

    def _check_alive(self):
        if self.hunger >= 100 or self.energy <= 0 or self.happiness <= 0:
            self.alive = False

    def __str__(self):
        return (f"{self.name} | Hunger: {self.hunger} | Energy: {self.energy} "
                f"| Happiness: {self.happiness} | Alive: {self.alive}")