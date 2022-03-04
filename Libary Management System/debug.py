from classes import *
import pickle

def add_admin():
    obj = Admin()
    print(obj.get_password())
    obj.edit_password()

    with open("admins.pkl",'ab+') as pfile :
        pickle.dump(obj,pfile)

