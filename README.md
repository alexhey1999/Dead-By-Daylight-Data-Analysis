# Dead-By-Daylight-Data-Analysis

Python based program that analyses a scoreboard screenshot using image recognition using opencv to determine what perks and other items have been used have been used. This way removes the need for someone to manually analyse these games.

## Example
![image](https://user-images.githubusercontent.com/64182587/205755914-b2fbb06d-a2ea-497b-8ab7-b43e4caa17dd.png)

Source: [Otzdarva](https://discord.gg/otzdarva)

Killer:  Nemesis
```
Survivor Perks Used: 
{
  'player_1': 
  {
    'perk_1': 'Windows Of Opportunity', 
    'perk_2': 'Prove Thyself', 
    'perk_3': 'Off The Record',
    'perk_4': 'Unbreakable'
  },
  'player_2': 
  {
    'perk_1': 'Off The Record', 
    'perk_2': 'Boon Circle Of Healing', 
    'perk_3': 'Unbreakable', 
    'perk_4': 'Sprint Burst'
  }, 
  'player_3': 
  {
    'perk_1': 'Prove Thyself', 
    'perk_2': 'Lithe', 
    'perk_3': 'Boon Circle Of Healing', 
    'perk_4': 'Off The Record'
  }, 
  'player_4': {
    'perk_1': 'Borrowed Time', 
    'perk_2': 'Sprint Burst', 
    'perk_3': 'Boon Circle Of Healing', 
    'perk_4': 'Unbreakable'
  }
}

Killer Perks Used: 
{
  'perk_1': 'Eruption', 
  'perk_2': 'The Third Seal', 
  'perk_3': 'Trail Of Torment', 
  'perk_4': 'Deadlock'
}

Items Used: 
  {
    'player_1': 'Medkit', 
    'player_2': 'No Item', 
    'player_3': 'No Item',
    'player_4': 'Toolbox'
  }

Scores: 
  {
    'player_1': 27095, 
    'player_2': 21810, 
    'player_3': 21230, 
    'player_4': 19242, 
    'killer': 28471
  }

Outcomes: ('Escape', 'Escape', 'Escape', 'Sacrificed', 'No Outcome')
Offerings: 
{
  'player_1': 'Sixth Anniversary', 
  'player_2': 'No Offering', 
  'player_3': 'Escape Cake', 
  'player_4': 'Escape Cake', 
  'killer': 'Shiny Coin'
}

Grades: 
{
  'player_1': 43, 
  'player_2': 24, 
  'player_3': 4, 
  'player_4': 14, 
  'killer': 10
}

Crossplay: 
{
  'character_1_crossplay': False,
  'character_2_crossplay': False,
  'character_3_crossplay': False,
  'character_4_crossplay': False,
  'killer_crossplay': False
}

Characters: 
{
  'player_1': 'Elodie Rakoto',
  'player_2': 'Claudette Morel',
  'player_3': 'Kate Denson',
  'player_4': 'Jill Valentine'
}

Addons:
{
  'player_1': 
    {
      'addon_1': 'Gel Dressings',
      'addon_2': 'Self Adherent Wrap'
    },
  'player_2': 
    {
      'addon_1': 'No Addon',
      'addon_2': 'No Addon'
    },
  'player_3': 
    {
      'addon_1': 'No Addon', 
      'addon_2': 'No Addon'
    },
  'player_4': 
    {
      'addon_1': 'Clean Rag', 
      'addon_2': 'Scraps'
    },
  'killer': 
    {
      'addon_1': 'Nea Parasite',
      'addon_2': 'Plant43 Vines'
    }
  } 
```
## Stats

Data Captured  | Implemented |
-------------- |-------------| 
Games Played   |:heavy_check_mark:|
Game Outcomes  |:heavy_check_mark:|
Killer         |:heavy_check_mark:|
Characters     |:heavy_check_mark:|
Survivor Perks |:heavy_check_mark:|
Killer Perks   |:heavy_check_mark:|
Items          |:heavy_check_mark:|
Item Addons    |:heavy_check_mark:|
Killer Addons  |:heavy_check_mark:|
Score          |:heavy_check_mark:|
Crossplay      |:heavy_check_mark:|
Grades         |:heavy_check_mark:|
Offerings      |:heavy_check_mark:|

![image](https://user-images.githubusercontent.com/64182587/205756242-02f06bc7-9719-4cda-81b4-076a51a27a35.png)
![image](https://user-images.githubusercontent.com/64182587/205756258-f0388a8a-3360-46f0-943e-05305b523494.png)

