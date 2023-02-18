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
        self.cur = self.conn.cursor()

    def create_account(self, user, email, pwd):
        hashable_user = bytes(user, encoding='utf-8')
        hashable_email = bytes(email, encoding='utf-8')
        hashable_pass = bytes(pwd, encoding='utf-8')

        hashed_user = bcrypt.hashpw(hashable_user, bcrypt.gensalt())
        hashed_email = bcrypt.hashpw(hashable_email, bcrypt.gensalt())
        hashed_pass = bcrypt.hashpw(hashable_pass, bcrypt.gensalt())
        
        db_check = self.cur.execute('SELECT * FROM accounts WHERE username=?', (hashed_user,))

        if hashed_user in db_check:
            return ('user', False)
        elif hashed_email in db_check:
            return('email', False)

        self.cur.execute('INSERT INTO accounts (username, email, pwd) VALUES(?,?,?)', (hashed_user, hashed_email, hashed_pass))

        return ('pwd', True)

    def login(self, account, pwd):
        hashable_account = bytes(account, encoding='uft-8')
        hashable_pass = bytes(pwd, encoding='utf-8')

        hashed_account = bcrypt.hashpw(hashable_account, bcrypt.gensalt())
        hashed_pass = bcrypt.hashpw(hashable_pass, bcrypt.gensalt())

        if '@' in account:
            try:
                db_check = self.cur.execute('SELECT * FROM accounts WHERE email="?"', hashed_account)
            except:
                return False
        else:
            try:
                db_check = self.cur.execute('SELECT * FROM accounts where username="?"', hashed_account)
            except:
                return False

        if hashed_pass in db_check:
            return True
        
        return False
        