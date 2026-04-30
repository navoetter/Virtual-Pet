# main.py
import time
from game_engine import GameEngine

def main():
    game = GameEngine("Fluffy")

    while not game.is_game_over():
        game.game_tick()
        game.print_status()

        # Beispielaktionen (später durch GUI ersetzen)
        game.feed_pet()
        game.play_with_pet()

        time.sleep(2)

    print("Game Over!")

if __name__ == "__main__":
    main()