import sqlite3

class insertdata:

    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def insertstudent(self,sid,sname,email,city):
        self.cur.execute(f'''
                        insert into STUDENT VALUES(
                        {sid},
                         '{sname}',
                         '{email}',
                         '{city}' )
                        ''')
        self.conn.commit()
        print('-----------------Inserted Data Successfully------------------------')

    def insertcourses(self,cid,coursename,sid,price):

        self.cur.execute(f'''
                        insert into COURSES VALUES(
                         '{cid}',
                         '{coursename}',
                         {sid},
                         {price}) 
                        ''')
        self.conn.commit()

        print('-------------------------Courses Data Added Successfully-------------------------')

    def inserttransactions(self,tid,sid,method):
        self.cur.execute(f'''
                        insert into TRANS VALUES(
                        '{tid}',
                         {sid},
                         '{method}')
                        ''')
        self.conn.commit()
        print('--------------------------Transaction Data Added Successfully------------------------')