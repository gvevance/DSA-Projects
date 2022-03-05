# login methods
import pickle

def admin_login():
    # assuming there are 1000 admins at max, and each admin's profile needs at max 1kB memory, a dictionary 
    # stored in a pickle file is feasible. Cross check as you use the program if this is feasible. Maybe
    # use flags to use both methods and compare speed and memory differences

    admin_pkl = "admins.pkl"
    adminID = input("\nEnter admin ID : ")
    
    #! FIGURE OUT CACHING OF ADMIN INFO
    
    try :
        found = False
        with open(admin_pkl,'rb') as pfile :
            while (True) :
                try :
                    admin = pickle.load(pfile)
                    if admin.get_ID() == adminID :
                        found = True
                        break    

                except EOFError:
                    break

        if not found :
            print("Incorrect User ID entered.")
            return False

        count = 0
        while (count < 3) :
            username = input("Enter username : ")
            password = input("Enter password : ")

            if username != admin.get_username() or password != admin.get_password() :
                count += 1
                print("\nWrong username or password entered.\n")

            else :
                return True
            
        if count >= 3 :
            print("Too many incorrect logins. Aborting ... ")
            return False

    except FileNotFoundError :
        print(f"{admin_pkl} does not exist.")
        return False

    except :
        return False    


def user_login():
    
    return True