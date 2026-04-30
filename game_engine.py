# game_engine.py
from pet import Pet
from minigame import MiniGame

class GameEngine:
    def __init__(self, pet_name: str):
        self.pet = Pet(pet_name)
        self.minigame = MiniGame()

    def game_tick(self):
        self.pet.tick()

    def feed_pet(self):
        self.pet.feed()

    def let_pet_sleep(self):
        self.pet.sleep()

    def play_with_pet(self):
        won = self.minigame.play()
        self.pet.play(won)
        print(f"Minigame gewonnen: {won}")

    def print_status(self):
        print(self.pet)

    def is_game_over(self) -> bool:
        return not self.pet.alive