import sqlite3
from dotenv import load_dotenv,find_dotenv
import os


class Database:
    def __init__(self):
        load_dotenv(find_dotenv())
        self.database_name = os.getenv("DATABASE_NAME")
        self.con = sqlite3.connect(self.database_name)
        self.db = self.con.cursor()
        
    def testing(self):
        query = """
        CREATE TABLE Games
        (    
            GameID INTEGER PRIMARY KEY,
            ImageID varchar(255) NOT NULL,
            Platform varchar(255)
        )
        """
        self.db.execute(query)

if __name__ == "__main__":
    database = Database()
    database.testing()