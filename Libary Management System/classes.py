# classes

from helper import generate_random_password

class Book :
    
    ''' Every book has a unique bookID, name, author, genre, price and summary. Some books are included in a 
    particular user membership type, some are not. Can include a sample of the book if needed.
    '''

    def __init__(self) :
        self._bookID = 123
        self._title = "Dummy title"
        self._authors = ["Dummy author 1","Dummy author 2"]
        self._genre = "Romance"
        self._credits = 100
        self._summary = "Dummy summary"
    
    def get_id(self) :
        return self._bookID
    
    def get_title(self) :
        return self._title

    def get_authors(self) :
        return self._authors

    def get_credits(self) :
        return self._credits

    def get_summary(self) :
        return self._summary

    def edit_details(self) :
        abort = False
        buffer = {}

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
            print("Aborting ... ")
            abort = True
        
        # enter authors
        

        # enter MRP
        count = 0
        if not abort :
            while (count < 3 ) :
                try :
                    buffer['credits'] = float(input("Enter credits of this book : "))

                except :
                    count += 1
                    print("Invalid credits entered. ",end="")
                
            if count >= 3 :
                print("Aborting ... ")
                abort = True

        # get summary later

        if not abort :
            self._title = buffer['title']
            self._authors = buffer['authors']
            self._credits = buffer["credits"]
    



class User :

    ''' User has a unique userID, a unique username, and a strong password. The usual details are also stored. Each 
    user belongs to one of 3 tiers. Each tier has a different credit limit - howmany credits worth of books a member 
    of that tier can borrow at a time. '''

    def __init__(self) :
        self._userID = 123
        self._username = "Dummy username"
        self._password = generate_random_password()
        self._name = "Dummy name"
        self._phone_number = '8542041960'
        self._member_type = 1       # 1 or 2 or 3

    