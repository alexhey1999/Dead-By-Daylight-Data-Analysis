import pytest
import os
from os import listdir
from screen_capping import Screen
from screeninfo import get_monitors
from dotenv import load_dotenv, find_dotenv

from perks import Perks


@pytest.fixture
def resources():
    load_dotenv(find_dotenv())
    monitor = get_monitors()[int(os.getenv("DEFAULT_MONITOR"))]
    ScreenTaker = Screen(monitor.width, monitor.height)
    PerkAnalyser = Perks(None)
    return ScreenTaker, PerkAnalyser


@pytest.mark.parametrize(
    "file_location,survivor_perks_actual,killer_perks_actual",
    [
        (
            "./Tests/test_full.png",
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
            [
                "Brutal Strength",
                "Lethal Pursuer",
                "Enduring",
                "Spirit Fury",
            ],
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
        ),
        (
            "./Tests/test_mori.png",
            ["Botany Knowledge", "Lucky Break", "Inner Focus", "Poised"],
            ["Call Of Brine", "Predator", "Spirit Fury", "Mind Breaker"],
        ),
        (
            "./Tests/test_difficult_survivor_perks.png",
            ["Deja Vu", "Kindred", "Object Of Obsession", "Dark Sense"],
            ["Stridor", "Beast Of Prey", "Hex Plaything", "Deathbound"],
        ),
        (
            "./Tests/test_disconnected.png",
            ["Appraisal", "Desperate Measures", "Resilience", "Smash Hit"],
            ["Save The Best For Last", "Bamboozle", "Devour Hope", "Furtive Chase"],
        ),
    ],
)
class Tests:
    def test_survivor(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual
    ):
        ScreenTaker, PerkAnalyser = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        
        PerkAnalyser.set_image(image)
        survivor_perks_used, _ = PerkAnalyser.run()
        assert (
            survivor_perks_used == survivor_perks_actual
        ), f"Survivor Perk Not Found: f{file_location}"

    def test_killer(
        self, resources, file_location, survivor_perks_actual, killer_perks_actual
    ):
        ScreenTaker, PerkAnalyser = resources
        image, _ = ScreenTaker.get_image_from_filename(file_location)
        image = ScreenTaker.process_screen_image(image)
        PerkAnalyser.set_image(image)
        _, killer_perks_used = PerkAnalyser.run()
        assert killer_perks_used == killer_perks_actual
