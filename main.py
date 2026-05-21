from game_engine import GameEngine
from start_screen import start_screen


def main():
    pet_name = start_screen()

    if not pet_name:
        return  

    print("Pet Name:", pet_name)

    game = GameEngine(pet_name)
    game.run()


if __name__ == "__main__":
    main()