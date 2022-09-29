import pytest
import os
from os import listdir
from pathlib import Path
import sys
path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))
from screen_capping import Screen
from screeninfo import get_monitors
from dotenv import load_dotenv, find_dotenv

from test_cases import TEST_CASES

from perks import Perks
from killer import Killer
from offerings import Offerings
from items import Items
from scores import Scores
from outcomes import Outcomes
from grades import Grades
from crossplay import Crossplay
from addons import Addons



@pytest.fixture
def ScreenTaker():
    load_dotenv(find_dotenv())
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
    return Screen(monitor.width, monitor.height)

@pytest.fixture
def PerkAnalyser():
    return Perks(None)

@pytest.fixture
def KillerAnalyser():
    return Killer(None)

@pytest.fixture
def OfferingAnalyser():
    return Offerings(None)

@pytest.fixture
def ItemAnalyser():
    return Items(None)

@pytest.fixture
def ScoreAnalyser():
    return Scores(None)

@pytest.fixture
def OutcomeAnalyser():
    return Outcomes(None)

@pytest.fixture
def GradeAnalyser():
    return Grades(None)

@pytest.fixture
def CrossplayAnalyser():
    return Crossplay(None)

@pytest.fixture
def AddonAnalyser():
    return Addons(None)

@pytest.mark.parametrize(
    "test_case",
    TEST_CASES
)

class Test:
    @classmethod
    def setup_class(self):
        pass
    
    # file_location,survivor_perks_actual,killer_perks_actual,killer,offerings,items,scores
    def test_survivor_perks(
        self, ScreenTaker, PerkAnalyser, test_case
    ):
        file_location,survivor_perks_actual = test_case[0], test_case[1]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)  
        PerkAnalyser.set_image(image)
        survivor_perks_used, _ = PerkAnalyser.run()
        assert (
            survivor_perks_used == survivor_perks_actual
        ), f"Survivor Perk Not Found: f{file_location}"


    def test_killer_perks(
        self, ScreenTaker, PerkAnalyser, test_case
    ):
        file_location,killer_perks_actual = test_case[0], test_case[2]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        PerkAnalyser.set_image(image)
        _, killer_perks_used = PerkAnalyser.run()
        assert (
            killer_perks_used == killer_perks_actual
        ), f"Killer Perk Not Found: f{file_location}"


    def test_killer(
        self, ScreenTaker, KillerAnalyser, test_case
    ):
        file_location,killer = test_case[0], test_case[3]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        KillerAnalyser.set_image(image)
        killer_determined = KillerAnalyser.run()
        assert (
            killer_determined == killer
        ), f"Killer Non Matching: f{file_location}"
        
    def test_offerings(
        self, ScreenTaker, OfferingAnalyser, test_case
    ):
        file_location,offerings = test_case[0], test_case[4]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        OfferingAnalyser.set_image(image)
        offerings_determined = OfferingAnalyser.run()
        assert (
            offerings_determined == offerings
        ), f"Offerings Non Matching: f{file_location}"
    
    def test_items(
        self, ScreenTaker, ItemAnalyser, test_case
    ):
        file_location,items = test_case[0], test_case[5]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        ItemAnalyser.set_image(image)
        items_determined = ItemAnalyser.run()
        assert (
            items_determined == items
        ), f"Offerings Non Matching: f{file_location}"
    
    def test_scores(
        self, ScreenTaker, ScoreAnalyser, test_case
    ):
        file_location,scores = test_case[0], test_case[6]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        # image = ScreenTaker.process_screen_image(image)
        ScoreAnalyser.set_image(image)
        scores_determined = ScoreAnalyser.run()
        assert (
            scores_determined == scores
        ), f"Scores Non Matching: f{file_location}"
    
    def test_outcomes(
        self, ScreenTaker, OutcomeAnalyser, test_case
    ):
        file_location, outcomes = test_case[0], test_case[7]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        OutcomeAnalyser.set_image(image)
        player_1_determined, player_2_determined, player_3_determined, player_4_determined, killer_determined = OutcomeAnalyser.run()
        
        assert player_1_determined == outcomes[0]
        assert player_2_determined == outcomes[1]
        assert player_3_determined == outcomes[2]
        assert player_4_determined == outcomes[3]
        assert killer_determined == outcomes[4]
        
    def test_grades(
        self, ScreenTaker, GradeAnalyser, test_case
    ):
        file_location,grades = test_case[0], test_case[8]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        GradeAnalyser.set_image(image)
        grades_determined = GradeAnalyser.run()
        # {'player_1': 'NAN', 'player_2': 'NAN', 'player_3': 'NAN', 'player_4': 'NAN', 'killer': 'NAN'}
        assert grades_determined["player_1"] == grades["player_1"]
        assert grades_determined["player_2"] == grades["player_2"]
        assert grades_determined["player_3"] == grades["player_3"]
        assert grades_determined["player_4"] == grades["player_4"]
        assert grades_determined["killer"] == grades["killer"]
            
    def test_crossplay(
        self, ScreenTaker, CrossplayAnalyser, test_case
    ):
        file_location,crossplay = test_case[0], test_case[9]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        CrossplayAnalyser.set_image(image)
        crossplay_determined = CrossplayAnalyser.run()
        # {'player_1': 'NAN', 'player_2': 'NAN', 'player_3': 'NAN', 'player_4': 'NAN', 'killer': 'NAN'}
        assert crossplay_determined["character_1_crossplay"] == crossplay["character_1_crossplay"]
        assert crossplay_determined["character_2_crossplay"] == crossplay["character_2_crossplay"]
        assert crossplay_determined["character_3_crossplay"] == crossplay["character_3_crossplay"]
        assert crossplay_determined["character_4_crossplay"] == crossplay["character_4_crossplay"]
        assert crossplay_determined["killer_crossplay"] == crossplay["killer_crossplay"]

    def test_addons(
        self, ScreenTaker,KillerAnalyser,AddonAnalyser, test_case
    ):
        file_location,addons = test_case[0], test_case[10]
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        KillerAnalyser.set_image(image)
        killer_determined = KillerAnalyser.run()
        
        AddonAnalyser.set_image(image)
        addons_determined = AddonAnalyser.run(killer_determined)
        assert addons_determined["player_1"] == addons["player_1"]
        assert addons_determined["player_2"] == addons["player_2"]
        assert addons_determined["player_3"] == addons["player_3"]
        assert addons_determined["player_4"] == addons["player_4"]
        assert addons_determined["killer"] == addons["killer"]