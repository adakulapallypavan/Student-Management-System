import sqlite3

class deletedate():

    def __init__(self):
        self.conn = sqlite3.connect('sms.db')
        self.cur = self.conn.cursor()

    def delete_sid(self,sid):
        self.conn.execute(f'''
                          DELETE FROM STUDENT
                          WHERE SID={sid}
                        ''')
        self.conn.commit()
        print('---------------Deleted Data Succesfully-------------------')
    
    def delete_name(self,name):
        self.conn.execute(f'''
                          DELETE FROM STUDENT
                          WHERE Name='{name}'
                        ''')
        self.conn.commit()
        print('---------------Deleted Data Succesfully-------------------')
    def delete_email(self,email):
        self.conn.execute(f'''
                          DELETE FROM STUDENT
                          WHERE Email='{email}'
                        ''')
        self.conn.commit()
        print('---------------Deleted Data Succesfully-------------------')
    
    def delete_city(self,city):
        self.conn.execute(f'''
                          DELETE FROM STUDENT
                          WHERE City='{city}'
                        ''')
        self.conn.commit()
        print('---------------Deleted SID Data Succesfully-------------------')
    #############################################################################

    def delete_cid(self,cid):
        self.conn.execute(f'''
DELETE FROM COURSES WHERE CID= '{cid}' ''')
        self.conn.commit()
        print('-------Data Deleted Succesfully-------------------')

    def delete_coursename(self,coursename):
        self.conn.execute(f'''
DELETE FROM COURSES WHERE CourseName= '{coursename}' ''')
        self.conn.commit()
        print('-------Data Deleted Succesfully-------------------')

    def delete_sid(self,sid):
        self.conn.execute(f'''
DELETE FROM COURSES WHERE SID={sid}''')
        self.conn.commit()
        print('-------Data Deleted Succesfully-------------------')

    def delete_price(self,price):
        self.conn.execute(f'''
DELETE FROM COURSES WHERE PRICE={price}''')
        self.conn.commit()
        print('-------Data Deleted Succesfully-------------------')    

#########################################################

    def delete_tid(self,tid):
        self.conn.execute(f'''
DELETE FROM TRANS WHERE TID='{tid}' ''')
        self.conn.commit()
        print('--------------Data Deleted Successfully-----------------------')

    def delete_sid(self,sid):
        self.conn.execute(f'''
DELETE FROM TRANS WHERE SID='{sid}' ''')
        self.conn.commit()
        print('--------------Data Deleted Successfully-----------------------')
    
    def delete_method(self,method):
        self.conn.execute(f'''
DELETE FROM TRANS WHERE Method='{method}' ''')
        self.conn.commit()
        print('--------------Data Deleted Successfully-----------------------')
