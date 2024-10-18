import sqlite3

class ReadData:

    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def read_student(self):
        self.cur.execute('SELECT * FROM STUDENT')
        rows = self.cur.fetchall()
        print('---------------Here is the Student Data-----------------------')
        for row in rows:
            print(row)
        return rows
    
    
    def read_courses(self):
        self.cur.execute('SELECT * FROM COURSES')
        rows = self.cur.fetchall()
        print('---------------Here is the COURSES Data-----------------------')
        for row in rows:
            print(row)
        return rows


    def read_transactions(self):
        self.cur.execute('SELECT * FROM TRANS')
        rows = self.cur.fetchall()
        print('---------------Here is the Transactions Data-----------------------')
        for row in rows:
            print(row)
        return rows
