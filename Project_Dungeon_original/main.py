from dungeon import Dungeon
import subprocess
import pickle
from datetime import datetime
from map_entities import Goblin
import os

if __name__ == "__main__":
    load = input("Press any key to start or press Y to load a map: ")
    if load == "Y" or load == "y":
        existing_file = False
        while existing_file == False:
            filename = input("Input your saved file in format hero_name_DMY_HMS.dng: ")
            if os.path.exists(filename):
                existing_file = True
                with open(filename, "rb") as f:
                    dungeon = pickle.load(f)
                    hero_name = filename.split('_')[0] # cool advice from chatGPT
                    print("Game loaded")
            else:
                print("Loading failed. File does not exist")
    else:
        hero_name = input("What is your name hero?")
        dungeon = Dungeon(size=(10, 10), tunnel_number=40, hero_name=hero_name)
    while True:
        subprocess.Popen("cls", shell=True).communicate()
        print(dungeon)
        print(dungeon.message)
        action = input(f"Select an action {hero_name}: (L)EFT, (R)IGHT, (D)OWN, (U)P, (A)TTACK, (S)AVE , (Q)UIT")
        dungeon.message = ""
        if action == "S" or action == "s":
            timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
            with open(f"{hero_name}_{timestamp}.dng", "wb") as f:
                pickle.dump(dungeon, f)
            dungeon.message = "Your progress has been saved"
        if action == "Q" or action == "q":
            print("You coward!")
            exit(0)
        else:
            dungeon.hero_action(action)
        if dungeon.hero.hp < 1:
            print(dungeon.message)
            exit(0)
