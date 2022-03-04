# classes

from helper import generate_random_password
from helper import valid_bookID
from helper import valid_adminID
from helper import valid_password
from helper import valid_phone_number
class Book :
    
    ''' Every book has a unique bookID, name, author, genre, price and summary. Some books are included in a 
    particular user membership type, some are not. Can include a sample of the book if needed.
    '''

    def __init__(self) :
        self._bookID = 123
        self._title = "Dummy title"
        self._authors = ["Dummy author 1","Dummy author 2"]
        self._genres = ["Romance"]
        self._credits = 100
        self._summary = "Dummy summary"
    
    def get_bookID(self) :
        return self._bookID
    
    def get_title(self) :
        return self._title

    def get_authors(self) :
        return self._authors

    def get_genres(self) :
        return self._genres

    def get_credits(self) :
        return self._credits

    def get_summary(self) :
        return self._summary

    def edit_details(self,verbose=False) :
        abort = False
        buffer = {}

        # enter bookID
        count = 0
        while (count < 3) :
            buffer['bookID'] = input("Enter bookID of book : ")
            
            if buffer["bookID"].strip() == '' :
                count += 1
                print("Empty bookID entered. ",end='')

            else :
                break

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True
        
        # enter title
        count = 0
        while (count < 3) :
            buffer['title'] = input("Enter title of book : ")
            
            if buffer["title"].strip() == '' :
                count += 1
                print("Empty book name entered. ",end='')

            else :
                break

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True
        
        # enter authors
        count = 0
        abort = False
        buffer["authors"] = []

        while (count < 3) :
            temp = input("Enter author name (0 to finish) : ")
            
            if temp.strip() == '' :
                count += 1
                print("Empty author name entered. ",end='')

            elif temp.strip() == '0' :
                break
            
            else :
                buffer["authors"].append(temp)

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True
            
        # enter genres
        count = 0
        abort = False
        buffer["genres"] = []

        while (count < 3) :
            temp = input("Enter genre name (0 to finish) : ")
            
            if temp.strip() == '' :
                count += 1
                print("Empty genre name entered. ",end='')

            elif temp.strip() == '0' :
                break
            
            else :
                buffer["genres"].append(temp)

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True

        # enter credits
        count = 0
        if not abort :
            while (count < 3 ) :
                try :
                    buffer['credits'] = float(input("Enter credits of this book : "))

                except :
                    count += 1
                    print("Invalid credits entered. ",end="")
                
            if count >= 3 :
                print("Aborting book details editing ... ")
                abort = True

        # get summary later

        if not abort :
            self._bookID = buffer["bookID"]
            self._title = buffer['title']
            self._authors = buffer['authors']
            self._genres = buffer['genres']
            self._credits = buffer["credits"]

            if verbose :
                print("Book details edited.")
                print(f"Title - {self._title}")
                
                print(f"Author(s) - ",end='')
                for i in range(len(self._authors)) :
                    if i == 0 :
                        print(self._authors[i],end='')
                    else :
                        print(f", {self._authors[i]}",end='')
                print()
                
                print("Genre(s) - ",end='')
                for i in range(len(self._genres)) :
                    if i == 0 :
                        print(self._genres[i],end='')
                    else :
                        print(f", {self._genres[i]}",end='')
                print()

                print(f"Credits -",self._credits)
    
    def edit_bookID(self,verbose=False) :
        abort = False

        # enter bookID
        count = 0
        while (count < 3) :
            buffer = input("Enter bookID : ")

            if not valid_bookID(buffer) :
                count += 1
                print("Invalid bookID entered. ",end='')

            else :
                break

        if count >= 3 :
            print("Aborting bookID editing ... ")
            abort = True

        if not abort :
            self._bookID = buffer

            if verbose :
                print("Book ID edited.\nBook ID -",self._bookID)

    def edit_title(self,verbose=False) :
        abort = False

        # enter title
        count = 0
        while (count < 3) :
            buffer = input("Enter title of book : ")
            
            if buffer.strip() == '' :
                count += 1
                print("Empty book name entered. ",end='')

            else :
                break

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True
        
        if not abort :
            self._title = buffer

            if verbose :
                print("Title edited.\nTitle -",self._title)

    def edit_authors(self,verbose=False) :
        count = 0
        abort = False
        buffer = []

        # enter authors
        while (count < 3) :
            temp = input("Enter author name (0 to finish) : ")
            
            if temp.strip() == '' :
                count += 1
                print("Empty author name entered. ",end='')

            elif temp.strip() == '0' :
                break
            
            else :
                buffer.append(temp)

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True

        if not abort :
            self._authors = buffer

            if verbose :
                print("Author(s) edited.\nAuthor(s) - ",end='')
                for i in range(len(self._authors)) :
                    if i == 0 :
                        print(self._authors[i],end='')
                    else :
                        print(f", {self._authors[i]}",end='')
                print()

    def edit_genres(self,verbose=False) :
        count = 0
        abort = False
        buffer = []

        while (count < 3) :
            temp = input("Enter genre name (0 to finish) : ")
            
            if temp.strip() == '' :
                count += 1
                print("Empty genre name entered. ",end='')

            elif temp.strip() == '0' :
                break
            
            else :
                buffer.append(temp)

        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True

        if not abort :
            self._genres = buffer

            if verbose :
                print("Genre(s) editied. Genre(s) - ",end='')
                for i in range(len(self._genres)) :
                    if i == 0 :
                        print(self._genres[i],end='')
                    else :
                        print(f", {self._genres[i]}",end='')
                print()

    def edit_credits(self,verbose=False) :
        abort = False

        while (count < 3 ) :
            try :
                buffer = float(input("Enter credits of this book : "))

            except :
                count += 1
                print("Invalid credits entered. ",end="")
            
        if count >= 3 :
            print("Aborting book details editing ... ")
            abort = True

        if not abort :
            self._credits = buffer

            if verbose :
                print("Credits edited. Credits -",self._credits)





class Account :
    ''' Parent class for various types of accounts - User, Admin. '''
    
    def __init__(self) :
        self._ID = 123
        self._username = "Dummy username"
        self._password = generate_random_password()
        self._name = "Dummy name"
        self._phone_number = '8542041960'        # 0 for user level clearance.

    def get_ID(self) :
        return self._ID

    def get_username(self) :
        return self._username

    def get_pw(self) :
        return self._password
    
    def get_name(self) :
        return self._name

    def get_phone_num(self) :
        return self._phone_number

    def edit_name(self,verbose=False) :
        self._name = input("Enter new name : ")

        if verbose :
            print("Name edited. Name - ",self._name)


    def edit_password(self,verbose=False) :

        oldpassword = input("Enter old password : ")
        if self._password != oldpassword :
            print("Wrong password entered. Aborting password edit ... ")
            return

        print("Password should have at least 8 characters, and must contain at least 2 special characters")
        abort = False
        count = 0
        while (count < 3) :
            buffer = input("Enter new password : ")
            
            if not valid_password(buffer) :
                count += 1
                print("Password too weak. ",end='')
            
            else :
                break

        if count >= 3 :
            print("Aborting password editing ... ")
            abort = True

        if not abort :
            self._password = buffer

            if verbose :
                print("Password edited. \nPassword - ",self._name)


    def edit_phone_number(self,verbose=False) :
        abort = False

        count = 0
        while (count < 3) :
            buffer = input("Enter new phone number : ")
            
            if not valid_phone_number(buffer) :
                count += 1
                print("Invalid phone number entered. ",end='')
            
            else :
                break

        if count >= 3 :
            print("Aborting phone number editing ... ")
            abort = True

        if not abort :
            self._phone_number = buffer

            if verbose :
                print("Phone number edited. \nPhone number - ",self._ID)


class User(Account) :
    ''' User has a unique userID, a unique username, and a strong password. The usual details are also stored. Each 
    user belongs to one of 3 tiers. Each tier has a different credit limit - howmany credits worth of books a member 
    of that tier can borrow at a time. '''
    
    pass


class Admin(Account) :
    
    def edit_adminID(self,verbose=False) :
        abort = False

        count = 0
        while (count < 3) :
            buffer = input("Enter new ID : ")
            
            if not valid_adminID(buffer) :
                count += 1
                print("Invalid admin ID entered. ",end='')
            
            else :
                break

        if count >= 3 :
            print("Aborting admin ID editing ... ")
            abort = True

        if not abort :
            self._ID = buffer

            if verbose :
                print("Admin ID edited. \nAdmin ID - ",self._ID)







