import sqlite3

class DBHandler:
    def __init__(self):
        pass

    def get_db_connection(self):
        try:
            self.conn = sqlite3.connect('database.db')
        except:
            print("db connection failed")
        self.conn.row_factory = sqlite3.Row