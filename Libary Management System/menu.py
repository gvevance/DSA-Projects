# menus at each screen
from login import admin_login
from login import user_login

import os

def admin_console_menu():
    os.system('clear')
    print("Entered Admin Console Menu")
    input()
    


def user_console_menu():
    os.system('clear')
    print("Entered User Console Menu")
    input()


def new_user_signup_menu():
    os.system('clear')
    print("Entered New User Signup Menu")
    input()


def main_menu():

    while (True) :
        os.system('clear')

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
            while ( count < 3 ) :
                if admin_login():
                    admin_console_menu()
                    break
                else :
                    count += 1

            if count >= 3 :
                input("\nLogin unsuccessful. Press a key to go back. ")

        elif option == '2' :
            if user_login() :
                user_console_menu()

        elif option == '3' :
            new_user_signup_menu()

        elif option == '4' :
            exit()