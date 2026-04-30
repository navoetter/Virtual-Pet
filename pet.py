# pet.py
class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 20      # 0 = satt, 100 = verhungert
        self.energy = 80      # 0 = erschöpft, 100 = voll
        self.happiness = 80   # 0 = traurig, 100 = glücklich
        self.alive = True

    # --- Zeitverlauf ---
    def tick(self):
        if not self.alive:
            return

        self.hunger += 5
        self.energy -= 5
        self.happiness -= 3

        self._clamp()
        self._check_alive()

    # --- Aktionen ---
    def feed(self):
        if not self.alive:
            return
        self.hunger -= 30
        self._clamp()

    def sleep(self):
        if not self.alive:
            return
        self.energy = 100

    def play(self, won: bool):
        if not self.alive:
            return

        if won:
            self.happiness += 20
        else:
            self.happiness -= 5

        self.energy -= 10
        self._clamp()

    # --- Hilfsmethoden ---
    def _clamp(self):
        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

    def _check_alive(self):
        if self.hunger >= 100 or self.energy <= 0 or self.happiness <= 0:
            self.alive = False

    def __str__(self):
        return (f"{self.name} | Hunger: {self.hunger} | Energie: {self.energy} "
                f"| Glück: {self.happiness} | Lebendig: {self.alive}")