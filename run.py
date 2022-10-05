#Handle Imports
import sys
from screen_capping import Screen
import os
from os import listdir

from dotenv import load_dotenv,find_dotenv
from screeninfo import get_monitors

# Import Analyser Classes
from perks import Perks
from killer import Killer
from offerings import Offerings
from items import Items
from scores import Scores
from outcomes import Outcomes
from grades import Grades
from crossplay import Crossplay
from characters import Characters
from addons import Addons
from database_handling import Database

image = None
    
def main(image, filename):
    pre_processed_image = image
    image = ScreenTaker.process_screen_image(image)
    
    PerkAnalyser = Perks(image)
    KillerAnalyser = Killer(image)
    OfferingAnalyser = Offerings(image)
    ItemAnalyser = Items(image)
    AddonAnalyser = Addons(image)
    OutcomeAnalyser = Outcomes(image)
    DatabaseHandler = Database()
    
    GradeAnalyser = Grades(pre_processed_image)
    ScoreAnalyser = Scores(pre_processed_image)
    CrossplayAnalyser = Crossplay(pre_processed_image)
    CharacterAnalyser = Characters(pre_processed_image)
    
    ScoreAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    GradeAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    CrossplayAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)
    CharacterAnalyser.set_lower_white(ScreenTaker.lower_white,pre_processed_image)

    killer = KillerAnalyser.run()
    survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    items_used = ItemAnalyser.run()
    scores = ScoreAnalyser.run()
    outcomes = OutcomeAnalyser.run()
    offerings = OfferingAnalyser.run()
    grades = GradeAnalyser.run()
    crossplay = CrossplayAnalyser.run()
    characters = CharacterAnalyser.run(crossplay)
    addons = AddonAnalyser.run(killer)
    
    DatabaseHandler.store_data(
        filename,
        killer,
        survivor_perks_used,
        killer_perks_used,
        items_used,
        scores,
        outcomes,
        offerings,
        grades,
        crossplay,
        characters,
        addons
        )
    
if __name__ == "__main__":
    load_dotenv(find_dotenv())
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
    ScreenTaker = Screen(monitor.width, monitor.height)
    
    
    try:
        if sys.argv[1].lower() == "passive":
            while True:
                print("==========================")
                print("Looking for endgame screen")
                print("==========================")
                image, filename = ScreenTaker.test_endscreen()
                print("Endgame Screen Found!")
                print("==========================")
                main(image, filename)
                print("Looking for Lobby Screen")
                print("==========================")
                ScreenTaker.test_lobby()
                print("Lobby Screen Found!")
        
        elif sys.argv[1].lower() == "folder":
            path = os.getenv("SCREENSHOT_LOCATIONS")
            for i in listdir(path):
                image, filename = ScreenTaker.get_image_from_filename(f"{path}/{i}")
                print(f"Image at: {i}")
                main(image, filename)
                print("Added Data!")
                print("==========================")
                
        elif sys.argv[1].lower() == "file":
            image, filename = ScreenTaker.get_image_from_filename(f'./Screenshots/{sys.argv[2]}')
            main(image, filename)
                
        elif sys.argv[1].lower() == "create_db":
            DatabaseHandler = Database()
            DatabaseHandler.create_tables()
            
        elif sys.argv[1].lower() == "drop_db":
            DatabaseHandler = Database()
            DatabaseHandler.drop_tables()
            
        else:
            print("Error")
    except:
        Exception("Error Booting Up Script")