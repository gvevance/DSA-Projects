# helper functions
import random
import string

def generate_random_password ( letters_count=10 , digits_count=4 , specials_count=3 ) :
    
    alphabets = list(string.ascii_letters)
    digits = list(string.digits)
    special_characters = list("!@#$%^&*()")

    password = []
    for _ in range(letters_count):
        password.append(random.choice(alphabets))

    for _ in range(digits_count):
        password.append(random.choice(digits))

    for _ in range(specials_count):
        password.append(random.choice(special_characters))

    random.shuffle(password)
    return "".join(password)