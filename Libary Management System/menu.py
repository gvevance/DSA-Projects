# menus at each screen
from login import admin_login
from login import user_login

def admin_console_menu():
    print("Entered Admin Console Menu")


def user_console_menu():
    print("Entered User Console Menu")


def new_user_signup_menu():
    print("Entered New User Signup Menu")


def main_menu():
    
    while (True) :

        print("\n\tLibMan - the Advanced Library Management System\n")
        print("1. Admin login \n2. User login \n3. New user? Sign up here. \n4. Exit \n")
        
        count = 0
        while (count < 3 ):
            option = input("Enter option : ").strip()

            if option not in ['1','2','3','4'] :
                count += 1
                print("Wrong option entered. ",end='')

            else :
                break

        if count >= 3 :
            print("Aborting ... ")
            exit()

        if option == '1' :
            if admin_login():
                admin_console_menu()

        elif option == '2' :
            if user_login() :
                user_console_menu()

        elif option == '3' :
            new_user_signup_menu()

        elif option == '4' :
            exit()