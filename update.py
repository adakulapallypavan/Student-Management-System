import sqlite3

class updatedata():

    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

########################################################################################
    def update_sid(self, current_sid, new_sid):
        self.cur.execute(f'''
            UPDATE STUDENT
            SET SID = {new_sid}
            WHERE SID = {current_sid}
        ''')
        self.conn.commit()
        print('---------------------Updated Data of Student Successfully------------------------')

    def update_name(self, sid, name):
        self.cur.execute(f'''
            UPDATE STUDENT
            SET Name = '{name}'
            WHERE SID = {sid}
        ''')
        self.conn.commit()
        print('---------------------Updated Data of Student Successfully------------------------')

    def update_email(self, sid, email):
        self.cur.execute(f'''
            UPDATE STUDENT
            SET Email = '{email}'
            WHERE SID = {sid}
        ''')
        self.conn.commit()
        print('---------------------Updated Data of Student Successfully------------------------')

    def update_city(self, sid, city):
        self.cur.execute(f'''
            UPDATE STUDENT
            SET City = '{city}'
            WHERE SID = {sid}
        ''')     
        self.conn.commit()
        print('---------------------Updated Data of Student Successfully------------------------')

######################################################################################################
    def update_cid(self,new_cid,current_cid):
        self.conn.execute(f'''
            UPDATE COURSES 
            SET CID={new_cid}
            WHERE CID={current_cid}
        ''')
        self.conn.commit()
        print('--------------------- Updated CID NO Successfully-------------------------')
    
    def update_coursename(self,cid,new_coursename):
        self.conn.execute(f'''
                          UPDATE COURSES
                          SET CourseName='{new_coursename}'
                          WHERE CID={cid}
''')
        self.conn.commit()
        print('-----------Updated CourseName Successfully---------')

    def update_sid(self,cid,new_sid):
        self.conn.execute(f'''
                          UPDATE COURSES
                          SET SID={new_sid}
                          WHERE CID={cid}
''')
        self.conn.commit()
        print('-----------Updated SID NO Successfully---------')

    def update_coursename(self,cid,new_price):
        self.conn.execute(f'''
                          UPDATE COURSES
                          SET PRICE={new_price}
                          WHERE CID={cid}
''')
        self.conn.commit()
        print('-----------Updated Price Successfully---------')
#############################################################################

    def update_tid(self,current_tid,new_tid):
        self.conn.execute(f'''
                          UPDATE TRANS
                          SET TID= '{new_tid}',
                          WHERE TID= '{current_tid}'
''')
        self.conn.commit()
        print('-----------Updated Transaction ID Successfully---------')

    def update_sid(self,tid,new_sid):
        self.conn.execute(f'''
UPDATE TRANS SET SID = {new_sid} WHERE TID='{tid}'
''')
        self.conn.commit()
        print('-----------Updated SID Successfully---------')
    
    def update_method(self,tid,new_method):
        self.conn.execute(f'''
UPDATE TRANS SET Method='{new_method}' WHERE TID='{tid}'
''')
        self.conn.commit()
        print('-----------Updated Method Successfully---------')




                
