import pytest
import os
from os import listdir
from screen_capping import Screen
from screeninfo import get_monitors
from dotenv import load_dotenv, find_dotenv

from perks import Perks
from killer import Killer
from offerings import Offerings
from items import Items


@pytest.fixture
def resources():
    load_dotenv(find_dotenv())
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
    ScreenTaker = Screen(monitor.width, monitor.height)
    PerkAnalyser = Perks(None)
    KillerAnalyser = Killer(None)
    OfferingAnalyser = Offerings(None)
    ItemAnalyser = Items(None)
    return ScreenTaker, PerkAnalyser, KillerAnalyser, OfferingAnalyser, ItemAnalyser


@pytest.mark.parametrize(
    "file_location,survivor_perks_actual,killer_perks_actual,killer,offerings,items",
    [
        (
            # File Name
            "./Tests/test_full.png",
            # Survivor Perks
            [
                "Power Struggle",
                "Unbreakable",
                "Flip Flop",
                "Soul Guard",
                "Head On",
                "Quick And Quiet",
                "Off The Record",
                "Iron Will",
                "Vigil",
                "Head On",
                "Off The Record",
                "Resilience",
                "Lithe",
                "Empathy",
                "Windows Of Opportunity",
                "Solidarity",
            ],
            # Killer Perks
            [
                "Brutal Strength",
                "Lethal Pursuer",
                "Enduring",
                "Spirit Fury",
            ],
            # Killer
            "Wraith",
            # Offerings
            [
                'Murky Reagent',
                'Bound Envelope',
                'Shroud Of Union',
            ],
            # Items
            ['Rundown Aid Kit']
        ),
        (
            "./Tests/test_random_1.png",
            ["Boon Exponential", "Left Behind", "Power Struggle", "Decisive Strike"],
            [
                "Brutal Strength",
                "Deathbound",
                "Spies From The Shadows",
                "Dead Man Switch",
            ],
            "Hag",
            ['Murky Reagent'],
            ['Flashlight Utility']
        ),
        (
            "./Tests/test_mori.png",
            ["Botany Knowledge", "Lucky Break", "Inner Focus", "Poised"],
            ["Call Of Brine", "Predator", "Spirit Fury", "Mind Breaker"],
            "Huntress",
            ['Momento Mori Cypress'],
            ['Rangers Aid Kit']
        ),
        (
            "./Tests/test_difficult_survivor_perks.png",
            ["Deja Vu", "Kindred", "Object Of Obsession", "Dark Sense"],
            ["Stridor", "Beast Of Prey", "Hex Plaything", "Deathbound"],
            "Demogorgon",
            [],
            ['Flashlight Utility']
        ),
        (
            "./Tests/test_disconnected.png",
            ["Appraisal", "Desperate Measures", "Resilience", "Smash Hit"],
            ["Save The Best For Last", "Bamboozle", "Devour Hope", "Furtive Chase"],
            "Nemesis",
            ['Macmillians Phalanx Bone'],
            []
        ),
    ],
)


class Tests:
    def test_survivor_perks(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual, killer, offerings, items
    ):
        ScreenTaker, PerkAnalyser, _, _, _ = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        
        PerkAnalyser.set_image(image)
        survivor_perks_used, _ = PerkAnalyser.run()
        assert (
            survivor_perks_used == survivor_perks_actual
        ), f"Survivor Perk Not Found: f{file_location}"


    def test_killer_perks(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual, killer, offerings, items
    ):
        ScreenTaker, PerkAnalyser, _, _, _ = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        PerkAnalyser.set_image(image)
        _, killer_perks_used = PerkAnalyser.run()
        assert (
            killer_perks_used == killer_perks_actual
        ), f"Killer Perk Not Found: f{file_location}"


    def test_killer(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual, killer, offerings, items
    ):
        ScreenTaker, _ , KillerAnalyser, _, _ = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        KillerAnalyser.set_image(image)
        killer_determined = KillerAnalyser.run()
        assert (
            killer_determined == killer
        ), f"Killer Non Matching: f{file_location}"
        
    def test_offerings(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual, killer, offerings, items
    ):
        ScreenTaker, _ , _, OfferingAnalyser, _ = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        OfferingAnalyser.set_image(image)
        offerings_determined = OfferingAnalyser.run()
        assert (
            offerings_determined == offerings
        ), f"Offerings Non Matching: f{file_location}"
    
    def test_items(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual, killer, offerings, items
    ):
        ScreenTaker, _ , _, _, ItemAnalyser = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        ItemAnalyser.set_image(image)
        items_determined = ItemAnalyser.run()
        assert (
            items_determined == items
        ), f"Offerings Non Matching: f{file_location}"
        
        
        
        