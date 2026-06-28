import random
import string
import os

if not os.path.exists("password.txt"):
    with open("password.txt" , "w") as f:
        pass

val = (string.ascii_letters + string.punctuation + string.digits)

password = ("")
while True:
    try:
        pass_len = int(input("Enter the length of password you need: "))
        break
    except ValueError:
        print("Invalid input")
    

for i in range(pass_len):
    password += (random.choice(val))
    
print("Your password is " , password)

while True:
    user = input("What do you want to do ?[exit(e) , get another password(g) , save password(s) , get passwords(p) , clear your password file(c)]: ").lower()
    
    if(user == "e"):
        break
    elif(user == "g"):
        try:
            password = ("")
            pass_len2 =int(input("Enter the length of password you need: "))
            for i in range(pass_len2):
             password += (random.choice(val))
    
            print("Your password is " , password)
        except ValueError:
            print("Invalid input")
            
    elif(user == "s"):
        with open("password.txt" , "a") as f:
            f.write(password + "\n")
            print("Saved!")
    elif(user == "p"):
        with open("password.txt" , "r")as f:
            print(f.read())

    elif(user == "c"):
        with open("password.txt" , "w")as f:
            pass