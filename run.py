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
    
def main(image, filename, ScreenTaker, DatabaseHandler):
    pre_processed_image = image
    image = ScreenTaker.process_screen_image(image)
    
    PerkAnalyser = Perks(image)
    KillerAnalyser = Killer(image)
    OfferingAnalyser = Offerings(image)
    ItemAnalyser = Items(image)
    AddonAnalyser = Addons(image)
    OutcomeAnalyser = Outcomes(image)
    
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
    
    # DatabaseHandler.store_data(
    #     filename,
    #     killer,
    #     survivor_perks_used,
    #     killer_perks_used,
    #     items_used,
    #     scores,
    #     outcomes,
    #     offerings,
    #     grades,
    #     crossplay,
    #     characters,
    #     addons
    #     )
    
    print("Killer: ",killer)
    print("Survivor Perks Used: " + str(survivor_perks_used))
    print("Killer Perks Used: " + str(killer_perks_used))
    print("Items Used: " + str(items_used))
    print("Scores: " + str(scores))
    print("Outcomes: ", str(outcomes))
    print("Offerings: ", offerings)
    print("Grades: ", str(grades))
    print("Crossplay: ", crossplay)
    print("Characters: ", characters)
    print("Addons: ", addons)
    
    del PerkAnalyser
    del KillerAnalyser
    del OfferingAnalyser
    del ItemAnalyser
    del AddonAnalyser
    del OutcomeAnalyser
    del GradeAnalyser
    del ScoreAnalyser
    del CrossplayAnalyser
    del CharacterAnalyser
    
if __name__ == "__main__":
    load_dotenv(find_dotenv())
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
    ScreenTaker = Screen(monitor.width, monitor.height)
    
    DatabaseHandler = Database()
    
    try:
        if sys.argv[1].lower() == "passive":
            while True:
                ScreenTaker = Screen(monitor.width, monitor.height)    
                print("==========================")
                print("Looking for endgame screen")
                print("==========================")
                image, filename = ScreenTaker.test_endscreen()
                print("Endgame Screen Found!")
                print("==========================")
                main(image, filename, ScreenTaker, DatabaseHandler)
                print("Looking for Lobby Screen")
                print("==========================")
                ScreenTaker.test_lobby()
                print("Lobby Screen Found!")
                del ScreenTaker
        
        elif sys.argv[1].lower() == "folder":
            path = os.getenv("SCREENSHOT_LOCATIONS")
            for i in listdir(path):
                ScreenTaker = Screen(monitor.width, monitor.height)    
                image, filename = ScreenTaker.get_image_from_filename(f"{path}/{i}")
                print(f"Image at: {i}")
                main(image, filename, ScreenTaker, DatabaseHandler)
                print("Added Data!")
                print("===========")
                del ScreenTaker
                
                
        elif sys.argv[1].lower() == "file":
            ScreenTaker = Screen(monitor.width, monitor.height)    
            image, filename = ScreenTaker.get_image_from_filename(f'./Screenshots/{sys.argv[2]}')
            main(image, filename, ScreenTaker, DatabaseHandler)
            del ScreenTaker
                
        elif sys.argv[1].lower() == "create_db":
            DatabaseHandler.create_tables()
            
        elif sys.argv[1].lower() == "drop_db":
            DatabaseHandler.drop_tables()
            
        else:
            print("Error")
    except:
        Exception("Error Booting Up Script")