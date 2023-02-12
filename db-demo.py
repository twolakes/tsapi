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
    
    def get_item(self, id):
        sql = """
            SELECT * FROM items
            WHERE ID = %s
        """
        self.cursor.execute(sql % id)
        return self.cursor.fetchone()

    def add_item(self, item_name):
        sql = """
            INSERT INTO items (name)
            VALUES ('%s') RETURNING *
        """
        self.cursor.execute(sql % item_name)
        new_item = self.cursor.fetchone()
        self.conn.commit()

        return new_item
    
    def update_item(self, id, new_name):

        sql = """
            UPDATE items
            SET name = '%s' 
            WHERE ID = %s
            RETURNING *
        """
        self.cursor.execute(sql % (new_name, id))
        mod_item = self.cursor.fetchone()
        self.conn.commit()
        return mod_item

    def del_item(self, id):
        sql = """
            DELETE FROM items
            WHERE ID = %s RETURNING *
        """
        self.cursor.execute(sql % id)
        del_item = self.cursor.fetchone()
        self.conn.commit()
        return del_item
