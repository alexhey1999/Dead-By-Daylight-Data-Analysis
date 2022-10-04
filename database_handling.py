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
        return player_id
    
    
    
    def store_data(self,image_name):

        # Game Data
        game_id = self.write_game_data(image_name)
        
        # Players

        
    
        self.con.commit()

if __name__ == "__main__":
    database = Database()