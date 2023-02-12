# demo file to show basic mechanics of db.py file
# used in place of file with actual db logic, schema, etc

import sqlite3
import os
from dotenv import load_dotenv


load_dotenv()

DB_NAME = os.getenv("DB_NAME")



class TSDb:
    def __init__(self):
        self.conn = sqlite3.connect(DB_NAME)
        self.cursor = self.conn.cursor()
    
    def get_items(self):
        result = []
        sql = "SELECT * FROM items"
        self.cursor.execute(sql)
        for r in self.cursor.fetchall():
            result.append({"ID": r[0], "name": r[1]})
        
        return result