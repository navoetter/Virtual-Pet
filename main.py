import os
import json
from game_engine import GameEngine
from start_screen import start_screen

SAVE_FILE = "pet_data.json"

def main():
    pet_name = None

    if os.path.exists(SAVE_FILE):
        try:
            #Data File opening
            with open(SAVE_FILE, "r") as f:
                data = json.load(f)
            if data.get("alive", True):
                pet_name = data.get("name", "Slime")
        except Exception:
            pass
    
    #If no game data / name go to start screen
    
    if not pet_name:
        pet_name = start_screen()

    if not pet_name:
        return  

    print("Pet Name:", pet_name)

    #Run game
    
    game = GameEngine(pet_name)
    game.run()

if __name__ == "__main__":
    main()  