TEST_CASES = [
    (
        (  # File Name
            "./Screenshots/test_full.png",
            # Survivor Perks
            {
                "player_1": {
                    "perk_1": "Power Struggle",
                    "perk_2": "Unbreakable",
                    "perk_3": "Flip Flop",
                    "perk_4": "Soul Guard",
                },
                "player_2": {
                    "perk_1": "Head On",
                    "perk_2": "Quick And Quiet",
                    "perk_3": "Off The Record",
                    "perk_4": "Iron Will",
                },
                "player_3": {
                    "perk_1": "Vigil",
                    "perk_2": "Head On",
                    "perk_3": "Off The Record",
                    "perk_4": "Resilience",
                },
                "player_4": {
                    "perk_1": "Lithe",
                    "perk_2": "Empathy",
                    "perk_3": "Windows Of Opportunity",
                    "perk_4": "Solidarity",
                },
            },
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
                "Murky Reagent",
                "Bound Envelope",
                "Shroud Of Union",
            ],
            # Items
            ["Rundown Aid Kit"],
            # Scores
            {
                "player_1": 11949,
                "player_2": 9233,
                "player_3": 8864,
                "player_4": 8096,
                "killer": 0,
            },
            ("Escape", "Escape", "Escape", "Escape", "Disconnected"),
            {
                "player_1": 12,
                "player_2": 11,
                "player_3": 12,
                "player_4": 1,
                "killer": 3,
            },
            {
                "character_1_crossplay": False,
                "character_2_crossplay": False,
                "character_3_crossplay": False,
                "character_4_crossplay": False,
                "killer_crossplay": False,
            },
            {
                "player_1": {"addon_1": "Syringe", "addon_2": "Bandages"},
                "player_2": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_3": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "No Addon", "addon_2": "No Addon"},
            },
            {
                "player_1": "Ashley J. Williams",
                "player_2": "Elodie Rakoto",
                "player_3": "Steve Harrington",
                "player_4": "Haddie Kaur",
            },
        )
    ),
    (
        (
            "./Screenshots/test_random_1.png",
            {
                "player_1": {
                    "perk_1": "Boon Exponential",
                    "perk_2": "Left Behind",
                    "perk_3": "Power Struggle",
                    "perk_4": "Decisive Strike",
                },
                "player_2": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_3": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_4": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
            },
            [
                "Brutal Strength",
                "Deathbound",
                "Spies From The Shadows",
                "Dead Man Switch",
            ],
            "Hag",
            ["Murky Reagent"],
            ["Flashlight Utility"],
            {
                "player_1": 23750,
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": 6413,
            },
            ("Escape", "No Outcome", "No Outcome", "No Outcome", "No Outcome"),
            {
                "player_1": "NAN",
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": "NAN",
            },
            {
                "character_1_crossplay": False,
                "character_2_crossplay": False,
                "character_3_crossplay": False,
                "character_4_crossplay": False,
                "killer_crossplay": False,
            },
            {
                "player_1": {
                    "addon_1": "Long Life Battery",
                    "addon_2": "Threaded Filament",
                },
                "player_2": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_3": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "Granmas Heart", "addon_2": "Bloodied Water"},
            },
            {
                "player_1": "Meg Thomas",
                "player_2": "No Character Found",
                "player_3": "No Character Found",
                "player_4": "No Character Found",
            },
        )
    ),
    (
        (
            "./Screenshots/test_mori.png",
            {
                "player_1": {
                    "perk_1": "Botany Knowledge",
                    "perk_2": "Lucky Break",
                    "perk_3": "Inner Focus",
                    "perk_4": "Poised",
                },
                "player_2": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_3": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_4": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
            },
            ["Call Of Brine", "Predator", "Spirit Fury", "Mind Breaker"],
            "Huntress",
            ["Momento Mori Cypress"],
            ["Rangers Aid Kit"],
            {
                "player_1": 11292,
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": 10875,
            },
            ("Death", "No Outcome", "No Outcome", "No Outcome", "No Outcome"),
            {
                "player_1": "NAN",
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": "NAN",
            },
            {
                "character_1_crossplay": False,
                "character_2_crossplay": False,
                "character_3_crossplay": False,
                "character_4_crossplay": False,
                "killer_crossplay": False,
            },
            {
                "player_1": {
                    "addon_1": "Abdominal Dressing",
                    "addon_2": "Gel Dressings",
                },
                "player_2": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_3": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "Iridescent Head", "addon_2": "Deerskin Gloves"},
            },
            {
                "player_1": "Nea Karlsson",
                "player_2": "No Character Found",
                "player_3": "No Character Found",
                "player_4": "No Character Found",
            },
        )
    ),
    (
        (
            "./Screenshots/test_difficult_survivor_perks.png",
            {
                "player_1": {
                    "perk_1": "Deja Vu",
                    "perk_2": "Kindred",
                    "perk_3": "Object Of Obsession",
                    "perk_4": "Dark Sense",
                },
                "player_2": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_3": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_4": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
            },
            ["Stridor", "Beast Of Prey", "Hex Plaything", "Deathbound"],
            "Demogorgon",
            [],
            ["Flashlight Utility"],
            {
                "player_1": 4025,
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": 5784,
            },
            ("Sacrificed", "No Outcome", "No Outcome", "No Outcome", "No Outcome"),
            {
                "player_1": "NAN",
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": "NAN",
            },
            {
                "character_1_crossplay": False,
                "character_2_crossplay": False,
                "character_3_crossplay": False,
                "character_4_crossplay": False,
                "killer_crossplay": False,
            },
            {
                "player_1": {
                    "addon_1": "Long Life Battery",
                    "addon_2": "Threaded Filament",
                },
                "player_2": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_3": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "Deer Lung", "addon_2": "Sticky Lining"},
            },
            {
                "player_1": "Meg Thomas",
                "player_2": "No Character Found",
                "player_3": "No Character Found",
                "player_4": "No Character Found",
            },
        )
    ),
    (
        (
            "./Screenshots/test_disconnected.png",
            {
                "player_1": {
                    "perk_1": "Appraisal",
                    "perk_2": "Desperate Measures",
                    "perk_3": "Resilience",
                    "perk_4": "Smash Hit",
                },
                "player_2": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_3": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
                "player_4": {
                    "perk_1": "No Perk",
                    "perk_2": "No Perk",
                    "perk_3": "No Perk",
                    "perk_4": "No Perk",
                },
            },
            ["Save The Best For Last", "Bamboozle", "Devour Hope", "Furtive Chase"],
            "Nemesis",
            ["Macmillians Phalanx Bone"],
            [],
            {
                "player_1": 14688,
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": 0,
            },
            ("Sacrificed", "No Outcome", "No Outcome", "No Outcome", "Disconnected"),
            {
                "player_1": "NAN",
                "player_2": "NAN",
                "player_3": "NAN",
                "player_4": "NAN",
                "killer": "NAN",
            },
            {
                "character_1_crossplay": False,
                "character_2_crossplay": False,
                "character_3_crossplay": False,
                "character_4_crossplay": False,
                "killer_crossplay": False,
            },
            {
                "player_1": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_2": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_3": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "Serotonin Injector", "addon_2": "Jill Sandwich"},
            },
            {
                "player_1": "David King",
                "player_2": "No Character Found",
                "player_3": "No Character Found",
                "player_4": "No Character Found",
            },
        )
    ),
    (
        (
            "./Screenshots/test_crossplay.png",
            {
                "player_1": {
                    "perk_1": "Prove Thyself",
                    "perk_2": "Adrenaline",
                    "perk_3": "Boon Circle Of Healing",
                    "perk_4": "Lithe",
                },
                "player_2": {
                    "perk_1": "Lithe",
                    "perk_2": "Prove Thyself",
                    "perk_3": "Second Wind",
                    "perk_4": "Adrenaline",
                },
                "player_3": {
                    "perk_1": "Resilience",
                    "perk_2": "Kindred",
                    "perk_3": "Small Game",
                    "perk_4": "Spine Chill",
                },
                "player_4": {
                    "perk_1": "Dead Hard",
                    "perk_2": "Fixated",
                    "perk_3": "Resilience",
                    "perk_4": "Off The Record",
                },
            },
            [
                "Lethal Pursuer",
                "B B Q And Chili",
                "Scourge Hook Gift Of Pain",
                "Thatanophobia",
            ],
            "Legion",
            ["Escape Cake", "Dusty Noose", "Fresh Crispleaf Amaranth", "Rotten Oak"],
            ["Medkit", "Rangers Aid Kit", "Rainbow Map", "Flashlight"],
            {
                "player_1": 29373,
                "player_2": 27615,
                "player_3": 19913,
                "player_4": 0,
                "killer": 21073,
            },
            ("Escape", "Escape", "Escape", "Disconnected", "No Outcome"),
            {
                "player_1": 29,
                "player_2": 24,
                "player_3": 10,
                "player_4": 1,
                "killer": 3,
            },
            {
                "character_1_crossplay": True,
                "character_2_crossplay": True,
                "character_3_crossplay": True,
                "character_4_crossplay": False,
                "killer_crossplay": True,
            },
            {
                "player_1": {"addon_1": "Self Adherent Wrap", "addon_2": "Gause Roll"},
                "player_2": {"addon_1": "Gel Dressings", "addon_2": "Gause Roll"},
                "player_3": {"addon_1": "Stamp Unusual", "addon_2": "Retardant Jelly"},
                "player_4": {"addon_1": "No Addon", "addon_2": "No Addon"},
                "killer": {"addon_1": "Etched Ruler", "addon_2": "The Legion Button"},
            },
            {
                "player_1": "Jane Romero",
                "player_2": "Ashley J. Williams",
                "player_3": "Ace Visconti",
                "player_4": "David King",
            },
        )
    ),
]
