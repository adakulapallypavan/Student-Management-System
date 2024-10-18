from insert import insertdata
from update import updatedata
from delete import deletedate
from read import ReadData

obj = insertdata()

obj1 = updatedata()

obj2 = deletedate()
obj3 = ReadData()

print('------------------------------STUDENT DATABASE MANAGEMENT SYSTEM-------------------------------')
print('For \nInsertion Press 1 \nUpdation Press 2 \nDeletion Press 3 \nReading Press 4' )

num = int(input('Please Enter Your Option: '))

if num==1:
    print('Choose 1 for Student:\nChoose 2 for Course: \nChoose 3 for transactions')
    n = int(input('Please Enter your Option:'))

    if n==1:
        sid = int(input('Please Enter Your ID:'))
        sname = input('Please Enter Your SNAME:')
        email = input('Please Enter Your EMAIL:')
        city = input('Please Enter Your CITY:')

        obj.insertstudent(sid,sname,email,city) 

    if n==2:
        cid = input('Please Enter CID NO:')
        coursename = input('Please Enter COURSENAME:')
        sid = int(input('Please Enter SID NO:'))
        price = input('Please Enter PRICE:')
        obj.insertcourses(cid,coursename,sid,price)

    if n==3:
        tid = input('Enter Your Transaction ID(TID):')
        sid = int(input('Enter Your Student ID(sid) :'))
        method = input('Enter Your Payment Method(cash/card/check/UPI):')
        obj.inserttransactions(tid,sid,method)
########################################################################################

elif num == 2:

    print('Choose 1 for Student:\nChoose 2 for Course: \nChoose 3 for transactions')
    n = int(input('Please Enter your Option:'))

    if n==1:
        current_sid = int(input('Please Enter Your Current ID: '))
        print('Choose the field to update:\n1. SID\n2. Name\n3. Email\n4. City')
        update_option = int(input('Please Enter Your Option: '))

        if update_option == 1:
            new_sid = int(input('Please Enter New SID: '))
            obj1.update_sid(current_sid, new_sid)
        elif update_option == 2:
            new_name = input('Please Enter New Name: ')
            obj1.update_name(current_sid, new_name)
        elif update_option == 3:
            new_email = input('Please Enter New Email: ')
            obj1.update_email(current_sid, new_email)
        elif update_option == 4:
            new_city = input('Please Enter New City: ')
            obj1.update_city(current_sid, new_city)
        else:
            print('Invalid option')

    elif n == 2:

        current_cid = int(input('Please Enter Your Current ID: '))
        print('Choose the field to update:\n1. CID\n2. CourseName\n3. SID\n4. Price')
        update_option = int(input('Please Enter Your Option: '))

        if update_option == 1:
            new_cid = int(input('Please Enter New CID: '))
            obj1.update_cid(current_cid, new_cid)
        elif update_option == 2:
            new_coursename = input('Please Enter New CourseName: ')
            obj1.update_coursename(current_cid, new_coursename)
        elif update_option == 3:
            new_sid = int(input('Please Enter New SID NO: '))
            obj1.update_sid(current_cid, new_sid)
        elif update_option == 4:
            new_price = input('Please Enter New Price: ')
            obj1.update_price(current_cid, new_price)
        else:
            print('Invalid option')
    
    elif n==3:

        current_tid = input('Please Enter the Your Current Transaction ID :')
        print('Choose the field to update:\n1. TID\n2. SID\n3. Method')
        update_option = int(input('Please Enter Your Option: '))

        if update_option==1:
            new_tid=input('Please Enter New TID :')
            obj1.update_tid(current_tid,new_tid)
        elif update_option==2:
            new_sid = int(input('Please Enter New SID NO :'))
            obj1.update_sid(current_tid,new_sid)
        elif update_option==3:
            new_method = input('Please Enter New Method :') 
            obj1.update_method(current_tid,new_method)
######################################################################

elif num==3:

    print('Choose 1 for Student:\nChoose 2 for Course: \nChoose 3 for transactions')
    n = int(input('Please Enter your Option:'))

    if n==1:
        print('Choose the field to delete:\n1. SID\n2. Name\n3. Email\n4. City')
        delete_option = int(input('Please Enter Your Option: '))
        if delete_option==1:
            sid_no = int(input('Please Enter Your SID NO:'))
            obj2.delete_sid(sid_no)
        elif delete_option==2:
            name = input('Please Enter Your Name:')
            obj2.delete_name(name)
        elif delete_option==3:
            email = input('Please Enter Your Email:')
            obj2.delete_email(email)
        elif delete_option==4:
            city = input('Please Enter Your City:')
            obj2.delete_city(city)
    ########################################################
    elif n==2:
        print('Choose the field to delete:\n1. CID\n2. CourseName\n3. SID\n4. Price')
        delete_option = int(input('Please Enter Your Option: '))
        if delete_option==1:
            cid = int(input('Please Enter Your CID NO:'))
            obj2.delete_cid(cid)
        elif delete_option==2:
            coursename = input('Please Enter Your CourseName:')
            obj2.delete_coursename(coursename)
        elif delete_option==3:
            sid = int(input('Please Enter Your SID NO:'))
            obj2.delete_sid(sid)
        elif delete_option==4:
            price = input('Please Enter Your SID NO:')
            obj2.delete_price(price)
    ########################################################
    elif n==3:
        print('Choose the field to delete:\n1. TID\n2. SID\n3. Method')
        delete_option = int(input('Please Enter Your Option: '))

        if delete_option==1:
            tid = input('Please Enter Your TID:')
            obj2.delete_tid(tid)
        elif delete_option==2:
            sid = int(input('Please Enter Your SID:'))
            obj2.delete_sid(sid)
        elif delete_option==3:
            method = input('Please Enter Your Method:')
            obj2.delete_method(method)

#####################################################################3

elif num==4:

    print('Choose the Table to read the date : \n1. STUDENT\n2. COURSES\n3. TRANS')
    n = int(input('Please Ente Your Table Option :'))

    if n==1:
        obj3.read_student()
    
    elif n==2:
        obj3.read_courses()
    
    elif n==3:
        obj3.read_transactions()
        



       

    
        


