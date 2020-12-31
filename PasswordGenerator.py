from random import randrange
from random import choice

length = 0
while(True):
    try:
        length = int(input("Please enter the length of your password: "))
        if length < 5: 
            raise ValueError
        break
    except ValueError:
        print("The password must be at least 5 characters in length and an integer!!!")

password = ""

for i in range(int(length)):
    password = password + (chr(choice([randrange(33,58),randrange(65,91),randrange(97,123)])))


print("Your password is: " + password)
