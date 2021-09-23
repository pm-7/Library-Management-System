________________________________________________________________________________________________________________________________________________
                                         WELCOME TO  THE INFORMATION SECTION

GENERAL INFORMATION:-
       *THE LIBRARY CONTAINS 5 BOOKS AND 6 STUDENT DETAILS.
       *IT IS PASSWORD PROTECTED.
    (note: read the "read_me" file present in the zip file after extracting.)                                                                                    


STEPS TO START :
        1.EXTRACT ALL THE FILES PRESENT IN THE "SITGR13_PROJECT" zip FILE.
        2.RUN THE "my_lib" IN POWERSHELL (hint: python my_lib.py)
        3.THE PROGRAM WILL START AND WILL ASK FOR ID AND PASSWORD.
         
                .................................................................
                . !!! ... IMPORTANT CREDENTIALS FOR THE FIRST TIME USER ... !!! .
                . ADMIN USERNAME/ID : SITBBSR5678                               .
                . ADMIN PASSWORD : SITbbsr@456                                  .
                . LIBRARIAN USERNAME/ID : SITBBSR1234                           .
                . LIBRARIAN PASSWORD : SITbbsr@123                              .
                ................................................................. 
                  
                 (note: also mentioned in "read_me" file) 

HOW TO RUN:
        AFTER RUNNING THE PROGRAM IF YOU CHOOSE [1]:
            *YOU WOULD LOG IN TO ADMIN SECTION
            *THE ADMIN SECTION CONTAINS [1]BOOKS
                                        [2]STUDENT
            *DO THE OPERATIONS ACCORDING TO YOUR NEED.
            *RETURN IF YOU DONT WANT TO USE.

  BOOKS SECTION:
  -------------
                1. DETAILS OF OPERATIONS WILL BE DISPLAYED TO YOU. 
                2. CHOOSE YOUR OPTION ACCORDINGLY.
                3. YOU CAN DISPLAY BOOK LIST THE AVAILABLE BOOKS .
                4. RETURN BY USING SUITABLE OPTION.
        # ADD BOOKS:
             1.PRESS [2] TO ADD BOOKS.
             2.ENTER THE CREDENTIALS REQUIRED.
             3.BOOK HAS BEEN ADDED AND RETURN BACK BY USING SUITABLE OPTIONS.
        # DELETE BOOKS:
             1.PRESS [3] TO DELETE BOOKS.
             2.ENTER THE BOOK ID OR BOOK NAME TO DELETE.
             3.RETURN BACK.
        # MODIFY BOOK:
             1.PRESS [4] TO MODIFY BOOKS.
             2.ENTER TO SEARCH BOOK BY BOOK ID OR NAME.
             3.MODIFY BY ENTERING THE NEW CREDENTIALS AND RETURN.
   
   
   
   STUDENT SECTION:
   ---------------
                1. DETAILS OF OPERATIONS WILL BE DISPLAYED TO YOU. 
                2. CHOOSE YOUR OPTION ACCORDINGLY.
                3. YOU CAN DISPLAY STUDENT LIST THE AVAILABLE STUDENTS .
                4. RETURN BY USING SUITABLE OPTION. 
        #ADD STUDENTS:
             1.PRESS [1] TO ADD STUDENTS.
             2.ENTER THE REQUIRED CREDENTIALS CORRECTLY.
             3.STUDENT WILL BE ADDED.
        #DELETE STUDENTS:
             1.PRESS [2] TO DELETE STUDENTS.
             2.SEARCH THE STUDENT BY NAME OR ID AND DELETE THE STUDENT.
             3.RETURN BACK.
        #MODIFY STUDENTS LIST:
             1.PRESS [3] TO MODIFY STUDENT LIST.
             2.SEARCH THE STUDENTBY ID OR NAME AND UPDATE HIS/HER ACCOUNT.
             3.RETURN BACK.
 NOTE- TO MODIFY STUDENT ACCOUNT(PASSWORD) USE THEIR PASSWORD PROPERLY PRESENT IN "read_me" file.



                             FUNCTIONS USED IN THE ADMIN SECTION
                            ______________________________________
   
   *sign_up_admin()   - used to login into admin section 
   
   *check_password()  - used to check PASSWORD is correct or not.

   *b_id_val()        - used to verify whether book id is valid or not.

   *add_books()       - used to add books.

   *check_bname()     - used to check book name.

   *valid_bname()     - used to check validity book name.

   *check_bid()       - used to check presence of same book ID.

   *check_author()    - used to check the author name.

   *check_number()    - used to check the phone number.

   *delete_books()    - used to delete books.

   *display_books()   - used to display book.

   *modify_books()    - used to modify books.

   *find_book()       - used to find book in the book list.

   *new_bid()         - used to add new book id.

   *new_bname()       - used to add new book name.

   *new_subject()     - used to add new subject.

   *new_amount()      - used to add no of books.

   *new_author()      - used to add new author name.

   *display()         - used to display STUDENT list.

   *add_students()   - used to add students.

   *find_student()   - used to find student in student list.

   *check_sname()    - used to check student name.

   *check_phn()      - used to verify phone no.

   *checkname()      - used to verify name.

   *check_sic()      - used to verify sic no.

   *check_mail()     - used to check the mail id.

   *delete_students()- used to delete students.

   *modify_student_interface()-used to modify student list.





HOW TO RUN LIBRARIAN SECTION:
        1. PRESS [2] FOR LIBRARIAN SECTION IN HOME.
        2. YOU WILL BE DISPLAYED CERTAIN OPTIONS .
        3. USE ACCORDINGLY.
        4. RETURN AT ANY MOMENT YOU WANT.
        5. YOU CAN DISPLAY BOOK LIST.
 
     LIBRARIAN SECTION:
     -----------------
                #ISSUE BOOKS:
                    1.PRESS [2] TO ISSUE A BOOK.
                    2.SELECT STUDENT SIC TO ISSUE A BOOK.
                    3.RETURN
                #RETURN BOOK:
                    1.PRESS [3] TO RETURN A BOOK.
                    2.SELECT THE SIC/NAME TO RETURN THE BOOK. 
                    3.RETURN
                #DISPLAY BOOK HOLDERS:
                    1.PRESS [4] TO DISPLAY .


                  FUNCTIONS USED IN LIBRARIAN SECTION
                  ___________________________________
      
      *sign_up_librarian()  - used to login LIBRARIAN section.

      *book_issue()         - used to issue the book.

      *return_book()        - used to return book.

      *book_issue_confirm() - used to confirm book issue.

      *display_student_list()-used to display the student having books.

warning: IF problem occurs while issuing ... return back and again issue book.
_______________________________________________________________________________________________________________________________________________