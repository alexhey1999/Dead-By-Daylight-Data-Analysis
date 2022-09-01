import pytest
import os
from os import listdir
from screen_capping import Screen
from screeninfo import get_monitors
from dotenv import load_dotenv,find_dotenv

from perks import Perks


load_dotenv(find_dotenv())

monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
ScreenTaker = Screen(monitor.width, monitor.height)
PerkAnalyser = Perks(None,None)


# def test_random_1():
#     image, filename = ScreenTaker.get_image_from_filename('./Tests/test_random_1.png')
#     PerkAnalyser.set_image(image)
#     survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    
    

def test_full():
    image, filename = ScreenTaker.get_image_from_filename('./Tests/test_full.png')
    PerkAnalyser.set_image(image)
    survivor_perks_used, killer_perks_used = PerkAnalyser.run()
    assert survivor_perks_used == ['Power Struggle', 'Unbreakable', 'Flip Flop', 'Soul Guard', 'Head On', 'Quick And Quiet', 'Off The Record', 'Iron Will', 'Vigil', 'Head On', 'Off The Record', 'Resilience', 'Lithe', 'Empathy', 'Windows Of Opportunity', 'Solidarity']
    assert killer_perks_used == ['Brutal Strength', 'Lethal Pursuer', 'Enduring', 'Spirit Fury']
    
    