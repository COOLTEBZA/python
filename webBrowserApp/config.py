import sqlite3
from datetime import datetime

class Users:
    def __init__(self, v, w, x, y, dt):
        self.id = v
        self.username = w
        self.password = x
        self.access = y
        self.dt = dt
    def id_(self):
        return self.id
    def username(self):
        return self.username
    def password(self):
        return self.password
    def access(self):
        return self.access
    def dt(self):
        return self.dt

    def insertData(self):
        
        self.countInfo = 1
        matchData = 'false'
        textId = ''
        matchData = [False, False]
        talLength0 = ''
        user_info = [self.username, self.password, self.access, self.dt]
        conn1 = sqlite3.connect("database.db")
        cur1 = conn1.cursor()
        for row in cur1.execute("SELECT * FROM users"):
            if row[1] == user_info[0] :
                textId = len(str(row[0]))
                matchData[0] = True
                
            if row[2] == user_info[1] :
                textId = len(str(row[0]))
                matchData[1] = True

        conn1.commit()
        conn1.close()

        if matchData[0] == True and matchData[1] == True:
            print(str("Already taken, Try another"))
        else:
            conn0 = sqlite3.connect("database.db")
            cur0 = conn0.cursor()
            cur0.execute('INSERT INTO users(uname, upwd, uaccess, udate) VALUES (?, ?, ?, ?)', user_info)
            conn0.commit()
            conn0.close()
            print('success')

dt_ = datetime.now()
u_ = Users(1, "uname", "upwd", "uaccess", dt_)
u_.insertData()



