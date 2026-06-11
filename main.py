import os
import json
from game_engine import GameEngine
from start_screen import start_screen

SAVE_FILE = "pet_data.json"

def main():
    pet_name = None

    # Falls eine Save-Datei existiert und das Pet lebt, überspringen wir den Startscreen
    if os.path.exists(SAVE_FILE):
        try:
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
            if data.get("alive", True):
                pet_name = data.get("name", "Slime")
        except Exception:
            pass

    # Wenn kein lebendes Pet gespeichert ist, Namen abfragen
    if not pet_name:
        pet_name = start_screen()

    if not pet_name:
        return  

    print("Pet Name:", pet_name)

    game = GameEngine(pet_name)
    game.run()


if __name__ == "__main__":
    main() 