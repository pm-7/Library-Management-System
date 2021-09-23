def return_book(w):
        print('_'*100)
        print('                           BOOK RETURN SECTION ')
        print('_'*100)
        if w=='lbrn':
                student_id=input('PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT: ')
                while is_sic(student_id)!=True:
                        print('... INVALID SIC ... ')
                        student_id=input('PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT: ')
                while check_sic(student_id)!=False:
                        print('..... STUDENT ACCOUNT NOT FOUND ....')
                        student_id=input('PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT: ')
                for student_account in stu:
                        if student_account['sic']==student_id:
                                break
        elif is_sic(w)==True:
                for student_account in stu:
                        if student_account['sic']==w:
                                break
        else:
                print('.... ERROR ... CANT LOGIN .... ')
                return False
        print('_'*100)
        print('                            BOOKS IN THE ACCOUNT : ')
        if student_account['book_1_name']!=None:
                print('BOOK[1]:',student_account['book_1_name'],'(',student_account['book_1_subject'],')')
        if student_account['book_2_name']!=None:
                print('BOOK[2]:',student_account['book_2_name'],'(',student_account['book_2_subject'],')')
        if student_account['book_with_student']==0:
                print(' ... NO BOOKS FOUND ...')
        print('_'*100)
        while(1):
                if student_account['book_with_student']==2:
                        which=input('ENTER (1) TO RETURN FIRST BOOK || (2) TO RETURN SECOND BOOK || ANY KEY TO EXIT:')
                elif student_account['book_with_student']==0:
                        print('NO BOOKS ISSUED...')
                        break
                else:
                        which='1'
                if which=='1':
                        for vals in book_list:
                                if vals['book_name']==student_account['book_1_name']:
                                        vals['amount']+=1
                                        student_account['book_1_name']=None
                                        student_account['book_1_subject']=None
                                        student_account['book_with_student']-=1
                                        print(' .. BOOK1 RETURNED SUCCESSFULLY ... ')
                                        break
                        if student_account['book_2_name']!=None:
                                student_account['book_1_name']=student_account['book_2_name']
                                student_account['book_2_name']=None
                                student_account['book_1_subject']=student_account['book_1_subject']
                                student_account['book_2_subject']=None

                elif which=='2':
                        for vals in book_list:
                                if vals['book_name']==student_account['book_2_name']:
                                        vals['amount']+=1
                                        student_account['book_2_name']=None
                                        student_account['book_2_subject']=None
                                        student_account['book_with_student']-=1
                                        print('.. BOOK2 RETURNED SUCCESSFULLY ....')
                                        break
                else:
                        break
                if student_account['book_with_student']>0:
                        want=input('DO YOU WANT TO RETURN ANOTHER BOOK(Y/N)?')
                        if want=='Y' or want=='y':
                                continue
                        else:
                                break
                else:
                        break
        print('_'*100)
        json.dump(stu, open('student.json', 'w'))
        json.dump(book_list,open('book_list.json','w'))
        print('_'*100)

def Book_issue_confirm(b_issue,student_account):
    issue_sucess=False
    while issue_sucess!=True:
        for book_to_be_issued in book_list:
            if (book_to_be_issued['book_name']==b_issue) or (book_to_be_issued['book_id']==b_issue):
                if book_to_be_issued['amount']>=1:
                    issue_sucess=True
                    
                    break
                else:
                    print(' ... BOOK NOT AVAILABLE ... ')
                    break
        if issue_sucess==False:
            print('                         ... BOOK NOT FOUND ...')
            decider=input('                         DO YOU WANT TO TRY AGAIN (Y/N): ')
            if decider=='Y':
                if input('                         Press  (1) to search by name || (2) to search by id:')=='1':
                    b_issue=input('                         ENTER THE NAME OF THE BOOK: ')
                else: 
                    b_issue=input('                         ENTER THE ID OF THE BOOK: ')
                
            else:
                return False
    if student_account['book_with_student']<2:
        if student_account['book_with_student']==0:
            student_account['book_1_name']=book_to_be_issued['book_name']
            student_account['book_1_subject']=book_to_be_issued['subject']
            book_to_be_issued['amount']-=1
            student_account['book_with_student']=1
            issue_sucess=True
        else:
            if book_to_be_issued['subject']!=student_account['book_1_subject']:
                student_account['book_2_name']=book_to_be_issued['book_name']
                student_account['book_2_subject']=book_to_be_issued['subject']
                book_to_be_issued['amount']-=1
                student_account['book_with_student']=2
                issue_sucess=True
            else:
                issue_sucess=False
                print('YOU ALREADY HAVE THIS BOOK ... ')
    else:
        print('..ERROR... YOU HAVE REACHED YOUR ISSUING LIMITS ... ')
        print('PLEASE RETURN A BOOK TO ISSUE')
        return False
    return issue_sucess

def book_issue(w):
    print('_'*100)
    print('                           BOOK ISSUE SECTION  ')
    print('_'*100)
    if w=='lbrn':
        student_id=input(' PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT : ')
        while is_sic(student_id)!=True:
            print('.... INVALID SIC ....')
            student_id=input('PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT: ')
        while check_sic(student_id)!=False:
            print('... STUDENT ACCOUNT NOT FOUND ...')
            student_id=input('PLEASE ENTER STUDENT SIC TO SEARCH ACCOUNT: ')
        for student_account in stu:
            if student_account['sic']==student_id:
                break
    elif is_sic(w)==True:
        for student_account in stu:
            if student_account['sic']==w:
                break
    else:
        print('SORRY .... INCORRECT CREDENTIALS .... ')
        return
    if input('Press  (1) TO SEARCH BY NAME || (2) TO SEARCH BY ID: ')=='1':
        b_issue=input('                         PLEASE ENTER THE NAME OF THE BOOK: ')
    else:
        b_issue=input('                         PLEASE ENTER THE ID OF THE BOOK: ')
    print('_'*100)
    if Book_issue_confirm(b_issue,student_account)==True:
        print('                         CONGRATS ... THE BOOK HAS BEEN SUCCESFULLY ISSUED ')
    else:
        print('                           SORRY ... TRY AGAIN LATER ...')
    print('_'*100)    
    json.dump(stu, open('student.json', 'w'))
    json.dump(book_list,open('book_list.json','w'))
    if input('                         DO YOU WANT TO ISSUE ANOTHER BOOK(Y/N): ')=='Y':
        if input('                         Press  (1) to search by name || (2) to search by id:')=='1':
            b_issue=input('                         ENTER THE NAME OF THE BOOK: ')
        else:
            b_issue=input('                         ENTER THE BOOK ID: ')
        if Book_issue_confirm(book_issue,student_account)==True:
            print('                         CONGRATULATIONS ... THE BOOK IS ISSUED .. ')
        else:
            print('                         SORRY FOR THE INCONVINIENCE ....')    
    print('_'*100)
    json.dump(stu, open('student.json', 'w'))
    json.dump(book_list,open('book_list.json','w'))
    print('_'*100)



def modify_student_interface():
        student_to_be_modified=None
        print('_'*100)
        print('                 STUDENT MODIFICATION INTERFACE ')
        print('_'*100)
        while(1):
                dec=input('PRESS (1) TO SEE STUDENT LIST || (2) TO SEARCH STUDENT FOR MODIFICATION || (3) RETURN BACK : ')
                if dec=='2':
                        while student_to_be_modified==None:
                                student_to_be_modified=find_student()
                        print('_'*100)
                        print('DETAILS :')
                        print(student_to_be_modified)
                        print('_'*100)
                        want=True
                        while want!='N':
                                print('         SELECT FROM WHAT TO MODIFY')
                                print('                (1) STUDENT SIC')
                                print('                (2) STUDENT NAME')
                                print('                (3) STUDENT PHONE NUMBER')
                                print('                (4) STUDENT PASSWORD')
                                print('                (5) STUDENT EMAIL ID')
                                print('                (6) RETURN ')
                                choice=input('PLEASE ENTER YOUR CHOICE : ')
                                print('_'*100)
                                if choice=='1':
                                        print('THE CURRENT SIC IS: ',student_to_be_modified['sic'])
                                        student_to_be_modified['sic']=input('PLEASE ENTER THE NEW SIC:')
                                        print(' NEW SIC STORED  ...  DATA STORED SUCCESFUL')
                                elif choice=='2':
                                        print('THE CURRENT STUDENT NAME IS :',student_to_be_modified['name'])
                                        student_to_be_modified['name']=input('ENTER NEW NAME OF STUDENT:')
                                        print('NEW NAME STORED  ...  DATA STORED SUCCESFUL')
                                elif choice=='3':
                                        print('THE CURRENT CURRENT PHONE NUMBER IS:',student_to_be_modified['phone number'])
                                        new_number=input('ENTER NEW PHONE NUMBER:')
                                        while is_number(new_number)!=True:
                                                print('... ERROR .. NOT A NUMBER ... ')
                                                new_number=input('ENTER NUMBER AGAIN:')
                                        while check_phn(new_number)!=True:
                                                print(' .. PHONE NUMBER EXIST ..')
                                                new_number=input('ENTER NUMBER AGAIN:')
                                        student_to_be_modified['phone number']=new_number
                                        print('NEW NUMBER SAVED  ..  DATA STORED SUCCESFUL')
                                elif choice=='4':
                                        flag=True
                                        i=0
                                        curr_pwd=input('ENTER CURRENT PASSWORD:')
                                        while curr_pwd!=student_to_be_modified['password']:
                                                print('PASSWORD MISMATCH')
                                                curr_pwd=input('ENTER PASSWORD AGAIN:')
                                                i+=1
                                                if i==3:
                                                        flag=False
                                                        break
                                        if flag==False:
                                                print('INVALID CREDENTIALS .... EXITING ...')
                                                break
                                        else:
                                                new_pwd=input('PLEASE ENTER NEW PASSWORD:')
                                                while check_password(new_pwd)!=True:
                                                        print('... INVALID PASSWORD ...')
                                                        new_pwd=input('PLEASE ENTER PASSWORD AGAIN:')
                                                new_pwd1=input('RE-ENTER PASSWORD :')
                                                while new_pwd1!=new_pwd:
                                                        print(' .... PASSWORD MISMATCH ... ')
                                                        new_pwd1=('RE-ENTER PASSWORD:')
                                                student_to_be_modified['password']=new_pwd
                                                print('PASSWORD SUCCESSFULLY CHANGED')
                                elif choice=='5':
                                        new_email=input('PLEASE ENTER NEW EMAIL ID :')
                                        while is_mail(new_email)!=True:
                                                print('.... INVALID EMAIL ID ....')
                                                new_email=input('ENTER NEW EMAIL ID :')
                                        while check_mail(new_email)!=True:
                                                print('... EMAIL ID ALREADY TAKEN ....')
                                                new_email=input('PLEASE ENTER EMAIL AGAIN :')
                                        student_to_be_modified['email id']=new_email
                                        print('EMAIL ID SUCCESFULLY CHANGED')
                                else:
                                        print('EXITING .... ')
                                        break
                                print('_'*100)
                        json.dump(stu,open('student.json','w'))  
                        want=input('DO YOU WANT TO MODIFY SOMETHING ELSE(Y/N) : ')
                        print('_'*100)
                elif dec=='1':
                        display_student_list()
                else:
                        print('EXITING .... ')
                        break

def display_student_list():
        print('_'*100)
        print('STUDENT NAME',' '*9,'NUMBER',' '*15,'EMAIL ID',' '*17,'SIC NO',' '*9,'NO OF BOOKS ')
        print('_'*100)
        

        for val in stu:
                print(val['name'],' '*(21-len(val['name'])),val['phone number'],' '*(15-len(val['phone number'])),val['email id'],' '*(30-len(val['email id'])),val['sic'],' '*(18-len(val['sic'])),val['book_with_student'])
                print('_'*100)
                
def delete_students():

        print('_'*100)
        print('              WELCOME TO STUDENT DELETION INTERFACE                              ')        
        print('_'*100)
        while(1):
                dec=input('PRESS (1) TO SHOW STUDENT LIST || (2) TO DELETE A STUDENT ACCOUNT || (3) TO EXIT : ')
                if dec=='1':
                        display_student_list()
                elif dec=='2':
                        wat=input('PRESS (1) TO SEARCH BY NAME || (2) TO SEARCH BY SIC || (3) TO EXIT : ')
                        if wat=='1':
                                delete_name=input('PLEASE ENTER NAME TO DELETE:')
                                while checkname(delete_name)!=True:
                                        print('.... INVALID NAME ....')
                                        delete_name=input('PLEASE ENTER NAME AGAIN:')
                                while check_sname(delete_name)!=False:
                                        print('ERROR .. STUDENT NOT FOUND ...')
                                        delete_name=input('PLEASE ENTER NAME AGAIN:')
                                for vals in stu:
                                        if vals['name']==delete_name:
                                                stu.remove(vals)
                                                break
                        elif wat=='2':
                                delete_id=input('PLEASE ENTER SIC TO DELETE:')
                                while is_sic(delete_id)!=True:
                                        print('ERROR ... WRONG SIC ')
                                        delete_id=input('PLEASE ENTER SIC AGAIN:')
                                while check_sic(delete_id)!=False:
                                        print('.. SIC NOT FOUND ..')
                                        delete_id=input('PLEASE ENTER SIC AGAIN:')
                                for vals in stu:
                                        if vals['sic']==delete_id:
                                                stu.remove(vals)
                                                break
                        else:
                                print('EXITING .......')
                else:
                        print('EXITING .... ')
                        break
        json.dump(stu,open('student.json','w'))        
        print('                                     STUDENT DELETED SUCCESSFULLY ')     
        print('_______________________________________________________________________________________')
    
def is_mail(email):
        i=0               
        dot_2=0
        na='\'?/|%^&(){|}+-*'
        while i<len(email):
                if email[i] in na:
                        return False
                elif email[i]=='@':
                        i+=1
                        break
                else:
                        i+=1
                        continue
        if email[i]=='.':
                return False
        while i<len(email):
                if email[i]=='.':
                        i+=1
                        dot_2+=1
                        continue
                elif email[i].isalpha()==True:
                        i+=1
                        continue
                else:
                        return False
        if dot_2==1:
                return True
        else:
                return False

def check_mail(arg):
        for vals in stu:
                if arg==vals['email id']:
                        return False
        return True

def is_sic(sic):
        sic_flag=False
        if len(sic)==9:
                sic_flag=True
                for val in sic:        
                        if int(val)>=0 and int(val)<=9:
                                sic_flag=True
                                continue
                        else:
                                print('!!!Invalid SIC!!!')
                                sic_flag=False
                                break
                
        else:
                sic_flag=False
        return sic_flag             

def check_sic(arg):
        for vals in stu:
                if arg==vals['sic']:
                        return False
        return True

def is_number(n):
        l='1234567890'
        c=0
        for val in n:
                c+=1
                if val in l:
                        flag=True
                else:
                        return False
        if c!=10:
                flag=False
        return flag

def check_phn(arg):
        for vals in stu:
                if arg==vals['phone number']:
                        return False
        return True

def checkname(name):
        name_flag=False
        for val in name:
                if (ord(val)>=97 and ord(val)<=122) or (ord(val)>=65 and ord(val)<=90):
                        name_flag=True
                        continue
                else:
                        name_flag=False
                        break
        if name in stu:
                name_flag=False
        return name_flag     

def check_sname(arg):

        for vals in stu:
                if arg==vals['name']:
                        return False
        return True

def add_students():
    print('_'*100)
    print('              WELCOME TO STUDENT ADDING INTERFACE                           ')        
    print('_'*100)
        
    name=input('             PLEASE ENTER THE STUDENT NAME:')         
    while check_sname(name)!=True:
            print('...NAME ALREADY TAKEN ...')
            name=input('             PLEASE ENTER THE NAME:')         

    while checkname(name)!=True:
            print(' ... INVALID NAME... ')
            name=input('             PLEASE ENTER THE NAME AGAIN:')
    print('_'*100)

    pn=input('             PLEASE ENTER THE PHONE NUMBER:')

    while check_phn(pn)!=True:
            print(' .. NUMBER ALREADY ASSIGNED .. ')
            pn=input('             PLEASE ENTER THE PHONE NUMBER:')

    while is_number(pn)!=True:
            print('ERROR .... NOT A VALID MOBILE NUMBER')
            pn=input('             PLEASE ENTER THE PHONE NUMBER:')

    print('_'*100)


    sic=input('             PLEASE ENTER THE SIC NUMBER OF THE STUDENT: ')

    while check_sic(sic)!=True:
            print('.... SIC IS ALREADY ASSIGNED TO ANOTHER ACCOUNT ...')
            sic=input('             PLEASE ENTER THE SIC NUMBER:')


    while is_sic(sic)!=True:
            print(' ....INVALID SIC....')
            sic=input('             PLEASE ENTER THE SIC NUMBER:')              
    print('_'*100)

    email=input('             PLEASE ENTER THE EMAIL ID:')
    while check_mail(email)!=True:
            print('..... EMAIL ID ASSIGNED TO ANOTHER ACCOUNT .....')
            email=input('             PLAESE ENTER THE EMAIL ID:')
                
    while is_mail(email)!=True:
            print(' ... INVALID EMAIL ID .... ')
            print('             TRY AGAIN FROM BEGINNING .... ')
            return
    print('_'*100)

    p=input('             PLEASE ENTER THE PASSWORD:')
    while check_password(p)!=True:
            p=input('             PLEASE ENTER THE PASSWORD:')
    print('_'*100)
        

    student={'name':name,
           'phone number':pn,
            'sic':sic,
            'email id':email,
            'password':p,
            'book_with_student':0,
            'book_1_name':'', 
            'book_2_name':'',
            'book_1_subject':'',
            'book_2_subject':'',}
    stu.append(student)
    json.dump(stu,open('student.json','w'))
    print('                     STUDENT DETAILS UPLOADED SUCCESSFUL ')
    print('_'*100)

def find_student():
        wat=input('PRESS (1) TO SEARCH BY NAME || (2) TO SEARCH BY SIC || ANY OTHER KEY TO EXIT : ')
        if wat=='1':
                modify_name=input('PLEASE ENTER STUDENT NAME TO FIND:')
                while checkname(modify_name)!=True:
                        print(' ...  INVALID NAME ... ')
                        modify_name=input('PLEASE ENTER NAME AGAIN:')
                while check_sname(modify_name)!=False:
                        print(' .... STUDENT NOT FOUND .... ')
                        modify_name=input('PLEASE ENTER NAME AGAIN:')
                for vals in stu:
                        if modify_name==vals['name']:
                                return vals
        elif wat=='2':
                modify_id=input('PLEASE ENTER SIC TO FIND:')
                while is_sic(modify_id)!=True:
                        print('... INVALID SIC ...')
                        modify_id=input('PLEASE ENTER SIC AGAIN:')
                while check_sic(modify_id)!=False:
                        print('.... Oops SIC NOT FOUND ....') 
                        modify_id=input('PLEASE ENTER SIC AGAIN:')
                for vals in stu:
                        if modify_id==vals['sic']:
                                return vals
        else:
                print('EXITTING ...... ')
                return None
        return None


def display():
        which_book=input('ENTER NAME OF THE BOOK:')
        while valid_bname(which_book)!=True:
                which_book=input('ENTER NAME OF THE BOOK AGAIN :')
        while check_bname(which_book)!=False:
                which_book=input('ENTER NAME OF THE BOOK AGAIN :')
        print('_'*100)
        print('STUDENT NAME',' '*9,'NUMBER',' '*9,'EMAIL ADDRESS',' '*15,'SIC',' '*9,'NO OF BOOKS')
        print('_'*100)
        for val in stu:
                if val['book_1_name']==which_book or val['book_2_name']==which_book:
                        print(val['name'],' '*(21-len(val['name'])),val['phone number'],' '*(15-len(val['phone number'])),val['email id'],' '*(22-len(val['email id'])),val['sic'],' '*(15-len(val['sic'])),val['book_with_student'])
                        print('_'*100)
                

def new_author():
    new_aname=input('PLEASE ENTER AUTHOR NAME:')
    return new_aname

def new_amount():
    new_av_amt=int(input('PLEASE ENTER NEW AMOUNT: '))
    return new_av_amt

def new_subject():
    new_sub=input('PLEASE ENTER NEW SUBJECT: ')
    return new_sub

def new_bname():
    new_bname=input('PLEASE ENTER BOOK NAME:')
    return new_bname

def new_bid():
    new_id=input('PLEASE ENTER NEW BOOK ID : ')
    return new_id

def find_book():
    decider=int(input('ENTER (1) TO PICK BOOK BY NAME  ||  (2) TO PICK BOOK BY ID : '))
    if decider==2:
        ID=input(' PLEASE ENTER SEARCH ID:')
        for vals in book_list:
            if vals['book_id']==ID:
                return vals
    elif decider==1:
        name=input('PLEASE ENTER BOOK SEARCH NAME :')
        for vals in book_list:
            if vals['book_name']==name:
                return vals
    print('ERROR .... BOOK NOT FOUND ... ')
    return None

def modify_books():
    flag=False
    print('_'*100)
    print('              WELCOME TO BOOK MODIFICATION INTERFACE SYSTEM ')
    print('_'*100)
    while flag==False:
        book_from_list=find_book()
        if book_from_list!=None:
            flag=True
        else:

            furt=input('DO YOU WANT TO SEARCH AGAIN (Y/N): ')
            if furt=='N':
                print('....ERROR....')
                return
    print('_'*100)
    want=True
    while want!='N':
        print('         SELECT OPTIONS TO MODIFY')
        print('               (1) BOOK ID')
        print('               (2) BOOK NAME')
        print('               (3) AMOUNT AVAILABLE')
        print('               (4) BOOK SUBJECT')
        print('               (5) AUTHOR NAME')
        choice=int(input('PLEASE ENTER YOUR CHOICE :'))
        print('______________________________________________________________________________________')
        if choice==1:
            print('THE CURRENT BOOK ID IS : ',book_from_list['book_id'])
            book_from_list['book_id']=new_bid()
        elif choice==2:
            print('THE CURRENT BOOK NAME IS : ',book_from_list['book_name'])
            book_from_list['book_name']=new_bname()        
        elif choice==3:
            print('NUMBERS OF BOOK AVAILABLE : ',book_from_list['amount'])
            dec=int(input('Press (1) TO CHANGE VALUE || (2) TO INCREASE OR DECREASE : '))
            if dec==1:
                book_from_list['amount']=new_amount()
            elif dec==2:
                dec_1=input('PLEASE ENTER (+) FOR INCREMENT and (-)FOR DECREMENT : ')
                if dec_1=='+':
                    increment_value=int(input('INCREASE BY:'))
                    book_from_list['amount']+=increment_value
                elif dec_1=='-':
                    decrement_value=int(input('DECREASE BY:'))
                    book_from_list['amount']-=decrement_value 
                else:
                    print('ERROR ... NOT ACCEPTED ...')
        elif choice==4:
            print('SUBJECT OF THE BOOK : ',book_from_list['subject'])
            book_from_list['subject']=new_subject()
        elif choice==5:
            print('AUTHOR OF THE BOOK : ',book_from_list['author name'])
            book_from_list['author name']=new_author()            
        else:    
            print('!!!oops INVALID CHOICE!!!')
            continue
        print('______________________________________________________________________________________')
        want=input('DO YOU WANT TO MODIFY SOMETHING ELSE(Y/N): ')
        print('______________________________________________________________________________________')
    json.dump(book_list,open('book_list.json','w'))

def display_books(book_list):
    print('________________________________________________________________________________________________________________________')
    print('  BOOK NAME',' '*9,'AUTHOR NAME',' '*9,'BOOK ID',' '*9,'SUBJECT',' '*9,'AMOUNT',' '*9)
    print('________________________________________________________________________________________________________________________')
    

    for val in book_list:
        print('  ',val['book_name'],' '*(18-len(val['book_name'])),val['author name'],' '*(20-len(val['author name'])),val['book_id'],' '*(16-len(val['book_id'])),val['subject'],' '*(16-len(val['subject'])),val['amount'])
        print('________________________________________________________________________________________________________________________')
        
def delete_books():
    print('_'*100)
    print('              WELCOME TO BOOK DELETION INTERFACE SYSTEM                              ')        
    print('_'*100)
    while(1):
        dec=input('ENTER (1) TO SHOW BOOK LIST || (2) TO DELETE A BOOK || (3) TO RETURN BACK ')
        if dec=='2':
            wat=input('ENTER (1) TO SEARCH BOOK BY NAME || (2) TO SEARCH BY ID || (3) TO EXIT ')
            if wat=='1':
                book_name=input('PLEASE ENTER NAME OF BOOK YOU WANT DELETE:')
                while valid_bname(book_name)!=True:
                    print(' ... INVALID NAME ... BOOK DOES NOT EXIST ')
                    book_name=input('PLEASE ENTER NAME OF BOOK TO DELETE:')
                while check_bname(book_name)!=False:
                    print(' .. BOOK NOT FOUND ..')
                    book_name=input('PLEASE ENTER NAME OF BOOK TO DELETE:')
                for vals in book_list:
                    if book_name==vals['book_name']:
                        book_list.remove(vals)
                        print('DELETED BOOK SUCCESSFULLY..')
                        break
            elif wat=='2':
                book_delete_id=input('PLEASE ENTER BOOK ID TO DELETE:')
                while valid_bid(book_delete_id)!=True:
                    print('.. ERROR ...  INVALID BOOK ID ')
                    book_delete_id=input('PLEASE ENTER BOOK ID AGAIN TO DELETE:')                            
                for vals in book_list:
                    if book_delete_id==vals['book_id']:
                        book_list.remove(vals)
                        print('BOOK SUCESSFULLY DELETED ... ')
                        return
                print('.. BOOK NOT FOUND ...')             
            else:
                print('LOADING ......... ')
        elif dec=='1':
            display_books(book_list)
        else:
            print(' EXITING...')
            break   
    json.dump(book_list,open('book_list.json','w'))
    print('_'*100)    

def check_number(num):
    for vals in num:
        if vals.isdigit()==True:
            continue
        else:
            return False
    return True

def check_author(name):
        for vals in name:
                if vals.isalpha()==True:
                        continue
                elif vals==' ':
                        continue
                else:
                        return False
        return True

def valid_bid(bid):
    for vals in bid:
        if vals.isupper()==True:
            continue
        elif vals.isdigit()==True:
            continue
        else:
            print('ID MUST ONLY CONTAIN UPPER CASE LETTERS AND DIGITS')
            return False
    return True

def check_bid(bid):
     if book_list==[]:
             return True   
     for vals in book_list:
        if vals['book_id']==bid:
                return False
        return True

def valid_bname(name):
    allspl=':()&@!+-*/,.?"'
    cntspc=0
    for vals in name:
        if vals.isalpha()==True:
            continue
        elif vals.isdigit()==True:
            continue
        elif vals==' ':
            cntspc+=1
            continue
        elif vals in allspl:
            continue
        else:
            return False
    if len(name)==cntspc:
        return False
    return True

def check_bname(name):
    for vals in book_list:
        if vals['book_name']==name:
            return False
    return True

def add_books():
    print('_'*100)
    print('              WELCOME TO BOOK ADDING INTERFACE SYSTEM                             ')        
    print('_'*100)
    while 1:
        dec=input('ENTER (1) TO ADD BOOK  ||  (2) TO DISPLAY LIST  ||  (3)  TO RETURN BACK   ')
        if dec=='1':
            name=input('PLEASE ENTER NAME OF THE BOOK:')
            while check_bname(name)!=True:
                print(' ERROR ... BOOK NAME ALREADY TAKEN...')
                name=input('PLEASE ENTER NAME OF THE BOOK:')
            while valid_bname(name)!=True:
                print(' INVALID BOOK NAME ')
                name=input('PLEASE ENTER NAME OF THE BOOK CORRECTLY :')
            print('_'*100)
            bid=input('PLEASE ENTER BOOK ID:')
            while check_bid(bid)!=True:
                print(' BOOK ID ALREADY TAKEN ... ')
                bid=input('PLEASE ENTER ANOTHER BOOK ID AGAIN:')
            while valid_bid(bid)!=True:
                print(' INVALID BOOK ID ')
                bid=input('PLEASE ENTER BOOK ID AGAIN:')
            print('_'*100)
            author=input('PLEASE ENTER THE AUTHOR NAME:')
            while check_author(author)!=True:
                print(' WRONG AUTHOR NAME SYNTAX ')
                author=input('PLEASE ENTER AUTHOR NAME AGAIN:')
            print('_'*100)
            subject=input('PLEASE ENTER SUBJECT:')
            while valid_bname(subject)!=True:
                print(' WRONG SUBJECT NAME SYNTAX')
                subject=input('PLEASE ENTER SUBJECT AGAIN:')
            print('_'*100)
            amount=input('ENTER NUMBER OF BOOKS AVAILABLE:')
            while check_number(amount)!=True:
                print(' INVALID AMOUNT ... ')
                amount=input('PLEASE ENTER NUMBER OF BOOKS AVAILABLE:')
            amount=int(amount)
            print('_'*100)
            b={ 'book_id':bid,
            'book_name':name,
            'amount':amount,
            'subject':subject,
            'author name':author,
            }
            book_list.append(b)
            json.dump(book_list,open('book_list.json','w'))
            print('_'*100)
            print('                       CREDENTIALS STORED SUCCESSFULLY ')
            print('_'*100)

        elif dec=='2':
            display_books(book_list)
        else:
            break

def b_id_val(bid):
    for vals in bid:
        if vals.isupper()==True:
            continue
        elif vals.isdigit()==True:
            continue
        else:
            print('ID MUST ONLY CONTAIN UPPER CASE LETTERS AND DIGITS')
            return False
    return True


def check_password(p):
        cnt_lower=0
        cnt_num=0
        cnt_upper=0
        cnt_spl=0
        pass_flag=False
        if len(p)<6 and len(p)>12:
                print('... PASSWORD SHOULD HAVE LENGTH 6 TO 12 .... ')
                return False
        l='!@#$%&'
        for vals in p:
                if (vals.islower())==True:
                        cnt_lower+=1
                if (vals.isupper())==True:
                        cnt_upper+=1
                if (vals.isdigit())==True:
                        cnt_num+=1
                if vals in l:
                        cnt_spl+=1
                if vals==' ':
                        break
        if cnt_num>0 and cnt_spl>0 and cnt_lower>0 and cnt_upper>0:
                pass_flag=True
        else:
                pass_flag=False
                print('YOUR PASS SHOULD CONTAIN ATLEAST A UPPER CASE LETTER, LOWER CASE LETTER , DIGIT , SPECIAL CHARACTER AND NO SPACES AND LENGTH MUST BE BETWEEN 6 TO 12')
        if vals==' ':
                pass_flag=False
                print('!!!INVALID .. NO SPACES PLEASE ..')
        if len(p)<8:
                pass_flag=False
        return pass_flag

def sign_up_librarian():
    print('_'*35)
    print(' WELCOME TO LIBRARIAN LOGIN ')
    print('_'*35)
    lbrn_id=input('PLEASE ENTER LIBRARIAN ID:')
    while (valid_bid(lbrn_id)!=True): 
        lbrn_id=input('PLEASE ENTER LIBRARIAN ID AGAIN:')
    while lbrn_id!=lbrn_ID:
        print(' ... LIBRARIAN ID MISMATCH ... ')
        return
    i=0
    lbrn_pwd=input('PLEASE ENTER PASSWORD:')
    #while check_password(lbrn_pwd)!=True:
    #    print('ERROR .... NOT A VALID PASSWORD')
    #    lbrn_pwd=input('PLEASE ENTER PASSWORD :')
    while lbrn_pwd!=pwd_lbrn:
        i+=1
        print('PASSWORD MISMATCH')
        lbrn_pwd=input('ENTER PASSWORD :')
        if i==3:
            print('... SECURITY BREACH DETECTED ... ')
            return False
    return True



def sign_up_admin():
    print('_'*100)
    print('           WELCOME TO THE ADMIN LOGIN .. ')
    print('_'*100)
    admin_id=input('PLEASE ENTER THE ADMIN ID: ')
    while(b_id_val(admin_id)!=True):
        admin_id=input('OOPS ..... !ERROR! ...  ENTER THE ADMIN ID AGAIN :')
    while admin_id!=admin_ID:
        print(' ID IS NOT MATCHIING !! ...  ') 
        return
    i=0
    admin_pwd=input('PLEASE ENTER THE PASSWORD: ')
    while admin_pwd!=admin_PWD:
        i=i+1
        print('PASSWORD INCORRECT !! ')
        admin_pwd=input('ENTER PASSWORD AGAIN :')
        if i==3:
            print('OOPS ... SECURITY BREACH DETECTED !!!')
            return False
    return True    






#############################################---MAIN FUNCTION---############################################
import json
stu=[]
book_list=json.load(open('book_list.json'))
stu=json.load(open('student.json'))

lbrn_ID='SITBBSR1234'
pwd_lbrn='SITbbsr@123'
admin_ID='SITBBSR5678'
admin_PWD='SITbbsr@456'

while(1):

    print('_'*100)
    print('                       WELCOME TO THE LIBRARY  ')
    print('_'*100)
    print('                     (1) ADMIN ')
    print('                     (2) LIBRARIAN')
    print('                     (3) EXIT')
    choice=input('              PLEASE ENTER YOUR CHOICE: ')
    if choice == '1':
            if sign_up_admin()!=True:
                    print('SORRY! ... ADMIN LOGIN FAILED ')
                    continue
            while(1):
                print('_'*100)
                print('             WELCOME TO ADMIN SECTION ')
                print('             (1) BOOKS SECTION ')
                print('             (2) STUDENT SECTION ')
                print('             (3) RETURN TO HOME ')
                opt=input('PLEASE ENTER YOUR CHOICE :')
                if opt =='1':
                    while(1):
                        print('_'*100)
                        print('                WELCOME TO BOOKS MANAGEMENT SECTION ')
                        print('                (1) DISPLAY BOOK LIST ')
                        print('                (2) ADD BOOKS ')
                        print('                (3) DELETE BOOKS ')
                        print('                (4) MODIFY BOOK LIST ')
                        print('                (5) RETURN BACK ')
                        opt_book=input('PLEASE ENTER YOUR CHOICE:')
                        if opt_book=='1':
                            display_books(book_list)
                            continue
                        elif opt_book=='2':
                            add_books()
                            continue
                        elif opt_book=='3':
                            delete_books()
                            continue
                        elif opt_book=='4':
                            modify_books()
                            continue
                        else:
                            print('... EXITING BOOK SECTION ....')
                            break
                elif opt =='2':

                    while(1):
                        print('_'*100)
                        print('                WELCOME TO STUDENT MANAGEMENT SECTION ')
                        print('                 PRESS (1) ADD A STUDENT ACCOUNT')
                        print('                 PRESS (2) DELETE A STUDENT ACCOUNT')
                        print('                 PRESS (3) MODIFY A STUDENT ACCOUNT')
                        print('                 PRESS (4) DISPLAY ALL STUDENT ACCOUNTS')
                        print('                 PRESS (5) RETURN BACK')
                        print('_'*100)
                        dec=input('PLEASE ENTER YOUR CHOICE: ')
                        if dec=='1':
                            add_students()
                            continue
                        elif dec=='2':
                            delete_students()
                            continue
                        elif dec =='3':
                            modify_student_interface()
                            continue
                        elif dec=='4':
                            display_student_list()
                            continue
                        else:
                            print('... EXITING STUDENT SECTION ....')    
                            break
                elif opt=='3':
                    break                
    elif choice=='2':
        if sign_up_librarian()!=True:
            print('LIBRARIAN LOGIN FAILED')
            continue
        while(1):
            print('_'*100)
            print('                      WELCOME TO LIBRARIAN SECTION ')
            print('_'*100)
            print('                      (1) DISPLAY BOOK LIST ')
            print('                      (2) ISSUES A BOOK     ')
            print('                      (3) RETURN A BOOK     ')
            print('                      (4) DISPLAY BOOK HOLDERS')
            print('                      (5) RETURN BACK       ')
            dec=input('PLEASE ENTER YOUR CHOICE: ')
            if dec=='1':
                display_books(book_list)
                continue
            elif dec=='2':
                book_issue('lbrn')
                continue
            elif dec=='3':
                return_book('lbrn')
                continue
            elif dec=='4':
                display()
                continue        
            elif dec=='5':
                print('.... EXITING LIBRARIAN SECTION ....')
                break
            else:
                print('INVALID CHOICE !')
                continue        
    elif choice=='3':

        print('... EXITING LIBRARY SYSTEM ...')    
        exit(0)        
    else:
        print('INVALID CHOICE .... ')
                








