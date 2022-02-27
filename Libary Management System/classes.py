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
                
                print("Genre(s) - ")
                for i in range(len(self._genres)) :
                    if i == 0 :
                        print(self._genres[i],end='')
                    else :
                        print(f", {self._genres[i]}",end='')
                print()

                print(f"Credits -",self._credits)
    

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
        pass

    def edit_genres(self,verbose=False) :
        pass

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

    