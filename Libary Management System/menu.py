# menus at each screen

def admin_console_menu():
    pass


def user_console_menu():
    pass


def new_user_signup_menu():
    pass


def main_menu():
    
    print("\n\tLibMan - the Advanced Library Management System\n")
    print("1. Admin login \n2. User login \n3. New user? Sign up here. \n4. Exit \n")
    
    count = 0
    while (count < 3 ):
        option = input("Enter option (1/2/3/4) : ").strip()

        if option not in ['1','2','3','4'] :
            count += 1
            print("Wrong option entered. ",end='')

        else :
            break

    if count >= 3 :
        print("Aborting ... ")
        exit()

    if option == '1' :
        admin_console_menu()

    elif option == '2' :
        user_console_menu()

    elif option == '3' :
        new_user_signup_menu()

    elif option == '4' :
        exit()