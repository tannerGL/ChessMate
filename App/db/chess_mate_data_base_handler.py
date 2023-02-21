import sqlite3
import bcrypt

class DBHandler:
    def __init__(self):
        pass

    def get_db_connection(self):
        try:
            self.conn = sqlite3.connect('/home/cillian/tannerGL/ChessMate/App/db/database.db')
        except:
            print("db connection failed")
        self.conn.row_factory = sqlite3.Row
        self.conn.text_factory = str
        self.cur = self.conn.cursor()

    def create_account(self, user, email, pwd):
        self.get_db_connection()
        hashable_pass = bytes(pwd, encoding='utf-8')
        print(hashable_pass)

        hashed_pass = bcrypt.hashpw(hashable_pass, bcrypt.gensalt())

        db_check = self.cur.execute('SELECT * FROM accounts WHERE username=?', (user,)).fetchall()

        if user in db_check:
            return ('user', False)
        elif email in db_check:
            return('email', False)

        self.cur.execute('INSERT INTO accounts (username, email, pwd) VALUES(?,?,?)', (user, email, hashed_pass))

        self.conn.commit()
        return ('pwd', True)

    def login(self, account, pwd):
        self.get_db_connection()
        if '@' in account:
            try:
                fetch = self.cur.execute("SELECT * FROM accounts WHERE email=?", (account,)).fetchall()
            except:
                return (False, "account")
        else:
            try:
                fetch = self.cur.execute("SELECT * FROM accounts where username=?", (account,)).fetchall()
            except:
                return (False, "account")

        db_hash = fetch[0][4]
        salt = bytes(db_hash[:30])
    
        hashable_pass = bytes(pwd, encoding='utf-8')
        hashed_pass = bcrypt.hashpw(hashable_pass, salt)

        if hashed_pass == db_hash:
            return (True, "success")
        
        return (False, "account")
        