TEST_CASES = [
    (
        (  # File Name
            "./Screenshots/test_full.png",
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
            {'character_1_crossplay': False, 'character_2_crossplay': False, 'character_3_crossplay': False, 'character_4_crossplay': False, 'killer_crossplay': False}
        )
    ),
    (
        (
            "./Screenshots/test_random_1.png",
            ["Boon Exponential", "Left Behind", "Power Struggle", "Decisive Strike"],
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
            {'character_1_crossplay': False, 'character_2_crossplay': False, 'character_3_crossplay': False, 'character_4_crossplay': False, 'killer_crossplay': False}
        )
    ),
    (
        (
            "./Screenshots/test_mori.png",
            ["Botany Knowledge", "Lucky Break", "Inner Focus", "Poised"],
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
            {'character_1_crossplay': False, 'character_2_crossplay': False, 'character_3_crossplay': False, 'character_4_crossplay': False, 'killer_crossplay': False}
        )
    ),
    (
        (
            "./Screenshots/test_difficult_survivor_perks.png",
            ["Deja Vu", "Kindred", "Object Of Obsession", "Dark Sense"],
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
            {'character_1_crossplay': False, 'character_2_crossplay': False, 'character_3_crossplay': False, 'character_4_crossplay': False, 'killer_crossplay': False}
        )
    ),
    (
        (
            "./Screenshots/test_disconnected.png",
            ["Appraisal", "Desperate Measures", "Resilience", "Smash Hit"],
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
            {'character_1_crossplay': False, 'character_2_crossplay': False, 'character_3_crossplay': False, 'character_4_crossplay': False, 'killer_crossplay': False}
        )
    ),
    (
        (
            "./Screenshots/test_crossplay.png",
            ['Prove Thyself', 'Adrenaline', 'Boon Circle Of Healing', 'Lithe', 'Lithe', 'Prove Thyself', 'Second Wind', 'Adrenaline', 'Resilience', 'Kindred', 'Small Game', 'Spine Chill', 'Dead Hard', 'Fixated', 'Resilience', 'Off The Record'],
            ['Lethal Pursuer', 'B B Q And Chili', 'Scourge Hook Gift Of Pain', 'Thatanophobia'],
            "Legion",
            ['Escape Cake', 'Dusty Noose', 'Fresh Crispleaf Amaranth', 'Rotten Oak'],
            ['Medkit', 'Rangers Aid Kit', 'Rainbow Map', 'Flashlight'],
            {'player_1': 29373, 'player_2': 27615, 'player_3': 19913, 'player_4': 0, 'killer': 21073},
            ('Escape', 'Escape', 'Escape', 'Disconnected', 'No Outcome'),
            {'player_1': 29, 'player_2': 24, 'player_3': 10, 'player_4': 1, 'killer': 3},
            {'character_1_crossplay': True, 'character_2_crossplay': True, 'character_3_crossplay': True, 'character_4_crossplay': False, 'killer_crossplay': True}
        )
    )
]
