import sqlite3
from dotenv import load_dotenv,find_dotenv
import os
import time

class Database:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.database_name = os.getenv("DATABASE_NAME")
        self.con = sqlite3.connect(self.database_name)
        self.db = self.con.cursor()
    
    def write_game_data(self, image_name):
        data = self.db.execute("INSERT INTO Games VALUES (?,?,?) RETURNING GameID;",[None,image_name, time.time()])
        game_id = data.fetchone()[0]
        return game_id

    def write_player_data(self, game_id, position, score, character, grade, crossplay, item, addon1, addon2):
        data = self.db.execute("INSERT INTO Players VALUES (?,?,?,?,?,?,?,?,?,?) RETURNING PlayerID;",[None,game_id,position,score,character,grade,crossplay,item,addon1,addon2])
        player_id = data.fetchone()[0]
        self.con.commit()
        return player_id
    
    
    def write_killer_data(self, player_id, killer, addon_1, addon_2):
        self.db.execute("INSERT INTO Killers VALUES (?,?,?,?,?);",[None,player_id,killer,addon_1,addon_2])
        self.con.commit()

    def write_offering_data(self, player_id, offering):
        self.db.execute("INSERT INTO Offerings VALUES (?,?,?);",[None,player_id,offering])
        self.con.commit()
        
    def write_outcome_data(self, player_id, outcome):
        self.db.execute("INSERT INTO Outcomes VALUES (?,?,?);",[None,player_id,outcome])
        self.con.commit()
        
    def write_score_data(self, player_id, score):
        self.db.execute("INSERT INTO Scores VALUES (?,?,?);",[None,player_id,score])
        self.con.commit()
    
    def write_survivor_perks_data(self, player_id, perk):
        self.db.execute("INSERT INTO SurvivorPerks VALUES (?,?,?);",[None,player_id,perk])
        self.con.commit()
    
    def write_killer_perks_data(self, player_id, perk):
        self.db.execute("INSERT INTO KillerPerks VALUES (?,?,?);",[None,player_id,perk])
        self.con.commit()
    
    def store_data(self,filename,killer,survivor_perks_used,killer_perks_used,items_used,scores,outcomes,offerings,grades,crossplay,characters,addons):
        # Game Data
        game_id = self.write_game_data(filename)
        
        # Players
        player_1_id = self.write_player_data(game_id, "1", scores["player_1"],characters["player_1"],grades["player_1"],str(crossplay["character_1_crossplay"]),items_used["player_1"],addons["player_1"]["addon_1"],addons["player_1"]["addon_2"])
        player_2_id = self.write_player_data(game_id, "2", scores["player_2"],characters["player_2"],grades["player_2"],str(crossplay["character_2_crossplay"]),items_used["player_2"],addons["player_2"]["addon_1"],addons["player_2"]["addon_2"])
        player_3_id = self.write_player_data(game_id, "3", scores["player_3"],characters["player_3"],grades["player_3"],str(crossplay["character_3_crossplay"]),items_used["player_3"],addons["player_3"]["addon_1"],addons["player_3"]["addon_2"])
        player_4_id = self.write_player_data(game_id, "4", scores["player_4"],characters["player_4"],grades["player_4"],str(crossplay["character_4_crossplay"]),items_used["player_4"],addons["player_4"]["addon_1"],addons["player_4"]["addon_2"])
        player_killer_id = self.write_player_data(game_id, "Killer" , scores["killer"],killer,grades["killer"],str(crossplay["killer_crossplay"]),"N/A",addons["killer"]["addon_1"],addons["killer"]["addon_2"])
        
        # # Killer
        self.write_killer_data(player_killer_id, killer, addons["killer"]["addon_1"], addons["killer"]["addon_2"])
        
        # # Offerings
        self.write_offering_data(player_1_id, offerings["player_1"])
        self.write_offering_data(player_2_id, offerings["player_2"])
        self.write_offering_data(player_3_id, offerings["player_3"])
        self.write_offering_data(player_4_id, offerings["player_4"])
        self.write_offering_data(player_killer_id, offerings["killer"])
        
        # # Outcomes
        self.write_outcome_data(player_1_id, outcomes[0])
        self.write_outcome_data(player_2_id, outcomes[1])
        self.write_outcome_data(player_3_id, outcomes[2])
        self.write_outcome_data(player_4_id, outcomes[3])
        self.write_outcome_data(player_killer_id, outcomes[4])
        
        # Scores
        self.write_score_data(player_1_id, scores["player_1"])
        self.write_score_data(player_2_id, scores["player_2"])
        self.write_score_data(player_3_id, scores["player_3"])
        self.write_score_data(player_4_id, scores["player_4"])
        self.write_score_data(player_killer_id, scores["killer"])
        
        # Survivor Perks
        self.write_survivor_perks_data(player_1_id, survivor_perks_used["player_1"]["perk_1"])
        self.write_survivor_perks_data(player_1_id, survivor_perks_used["player_1"]["perk_2"])
        self.write_survivor_perks_data(player_1_id, survivor_perks_used["player_1"]["perk_3"])
        self.write_survivor_perks_data(player_1_id, survivor_perks_used["player_1"]["perk_4"])
    
        self.write_survivor_perks_data(player_2_id, survivor_perks_used["player_2"]["perk_1"])
        self.write_survivor_perks_data(player_2_id, survivor_perks_used["player_2"]["perk_2"])
        self.write_survivor_perks_data(player_2_id, survivor_perks_used["player_2"]["perk_3"])
        self.write_survivor_perks_data(player_2_id, survivor_perks_used["player_2"]["perk_4"])
    
        self.write_survivor_perks_data(player_3_id, survivor_perks_used["player_3"]["perk_1"])
        self.write_survivor_perks_data(player_3_id, survivor_perks_used["player_3"]["perk_2"])
        self.write_survivor_perks_data(player_3_id, survivor_perks_used["player_3"]["perk_3"])
        self.write_survivor_perks_data(player_3_id, survivor_perks_used["player_3"]["perk_4"])
    
        self.write_survivor_perks_data(player_4_id, survivor_perks_used["player_4"]["perk_1"])
        self.write_survivor_perks_data(player_4_id, survivor_perks_used["player_4"]["perk_2"])
        self.write_survivor_perks_data(player_4_id, survivor_perks_used["player_4"]["perk_3"])
        self.write_survivor_perks_data(player_4_id, survivor_perks_used["player_4"]["perk_4"])
        
        # Killer Perks
        self.write_killer_perks_data(player_killer_id, killer_perks_used["perk_1"])
        self.write_killer_perks_data(player_killer_id, killer_perks_used["perk_2"])
        self.write_killer_perks_data(player_killer_id, killer_perks_used["perk_3"])
        self.write_killer_perks_data(player_killer_id, killer_perks_used["perk_4"])        
        
        self.con.commit()
    
    def create_tables(self):    
        commands = [
            'CREATE TABLE "Games" ("GameID" INTEGER,"ImageUUID" TEXT,"CreatedOn" INTEGER, PRIMARY KEY("GameID" AUTOINCREMENT))',
            'CREATE TABLE "Players" ( "PlayerID" INTEGER, "GameID" INTEGER, "Position" TEXT, "Score" INTEGER, "Character" TEXT, "Grade" TEXT, "Crossplay" TEXT, "Item" TEXT, "Addon1" TEXT, "Addon2" TEXT, PRIMARY KEY("PlayerID" AUTOINCREMENT) )',
            'CREATE TABLE "KillerPerks" ("PerkID" INTEGER, "PersonID" INTEGER,"Perk" TEXT, PRIMARY KEY("PerkID" AUTOINCREMENT))',
            'CREATE TABLE "Killers" ( "KillerID" INTEGER, "PlayerID" INTEGER, "Killer" TEXT, "Addon1" TEXT, "Addon2" TEXT, PRIMARY KEY("KillerID" AUTOINCREMENT))',
            'CREATE TABLE "Offerings" ( "OfferingID" INTEGER, "PersonID" INTEGER, "Offering" TEXT, PRIMARY KEY("OfferingID" AUTOINCREMENT), FOREIGN KEY("PersonID") REFERENCES "Games"("GameID"))',
            'CREATE TABLE "Outcomes" ( "OutcomeID" INTEGER, "PlayerID" INTEGER, "Outcome" TEXT, PRIMARY KEY("OutcomeID" AUTOINCREMENT))',
            'CREATE TABLE "Scores" ( "ScoreID" INTEGER, "PlayerID" INTEGER, "Score" INTEGER, FOREIGN KEY("PlayerID") REFERENCES "Players"("PlayerID"), PRIMARY KEY("ScoreID" AUTOINCREMENT) )',
            'CREATE TABLE "SurvivorPerks" ( "PerkID" INTEGER, "PersonID" INTEGER, "Perk" TEXT, PRIMARY KEY("PerkID" AUTOINCREMENT) )'
        ]
        
        for i in commands:
            self.db.execute(i)
            self.con.commit()
        
    def drop_tables(self):
        commands = [
            'DROP TABLE "Games"',
            'DROP TABLE "Players"',
            'DROP TABLE "KillerPerks"',
            'DROP TABLE "Killers"',
            'DROP TABLE "Offerings"',
            'DROP TABLE "Outcomes"',
            'DROP TABLE "Scores"',
            'DROP TABLE "SurvivorPerks"'
        ]
        
        for i in commands:
            self.db.execute(i)
            self.con.commit()
        

if __name__ == "__main__":
    database = Database()