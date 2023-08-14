""" 
Ask user if want to gen a random pass
if yes
    ask for pass length
    generate pass
    print pass
if no
    exit program
"""

import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%¨&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be?"))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


option = input("Do you want to generate a password? (Yes/no)")

if option == "yes":
    generate_password()
elif option == "no":
    print('Program ended')
    quit()
else:
    print("Invalid input. Please input yes or no")
    quit()