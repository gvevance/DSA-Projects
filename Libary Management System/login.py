# login methods
import pickle

def admin_login():
    # assuming there are 1000 admins at max, and each admin's profile needs at max 1kB memory, a dictionary 
    # stored in a pickle file is feasible. Cross check as you use the program if this is feasible. Maybe
    # use flags to use both methods and compare speed and memory differences

    admin_pkl = "admins.pkl"
    adminID = input("Enter admin ID : ")
    
    #! FIGURE OUT CACHING OF ADMIN INFO
    
    with open(admin_pkl,'rb') as pfile :
        while (True) :
            try :
                admin = pickle.load(pfile)
                if admin.getID() == adminID :
                    count = 0
                    while (count < 3) :
                        username = input("Enter username : ")
                        password = input("Enter password : ")

                        if username != admin.get_username() or password != admin.get_pw() :
                            count += 1
                            print("\nWrong username or password entered.\n")

                        else :
                            break
                        
                    if count >= 3 :
                        print("Aborting login ... ")
                        return

            except EOFError:
                print("Admin ID incorrect.\n")
                break
    

    return True

def user_login():
    
    return True