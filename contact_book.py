import os

if not os.path.exists("Contact.txt"):
    with open("Contact.txt" , "w")as f:
        pass


def addc(name , number):
    entry = (f"{name}->{number}")
    
    with open("Contact.txt" , "a")as f:
        f.write(entry + "\n")
def dltc(name , number):
    
    contacts = []
    with open("Contact.txt" , "r")as f:
        for line in f:
            line = line.strip()
            if(line == ""):
                continue
            nam , numb = line.split("->")
            if(name == nam and number == numb):
                continue
            contacts.append(line)
            
    with open("Contact.txt" , "w")as f:
        for i in contacts:
            f.write(i +"\n")


while True:
    a = input("What do you want to do ? [View contacts(v) , Add new contact(n) , Delete contact(d) , delete all of your contacts(c) Exit(e)]\n").lower().strip()
    
    if(a == "e"):
        break
    elif(a == "v"):
        with open("Contact.txt" , "r")as f:
            view = (f.read())
            if(view == ""):
                print("You have no contacts yet....")
            else:
                print(view)
    elif(a == "n"):
        while True:
            want = input("If you want to add a number press enter , or if you want to exit(e)").lower().strip()
            if(want == "e"):
                break
           
            c = str(input("Write the name of contact you want to add: ")).upper().strip()
            if(c == ""):
                print("Invalid input")
                while True:
                    c = str(input("Write the name of contact you want to add: ")).upper()
                    c = c.strip()
                    if(c != ""):
                        break
            while True:
                d = (input("Enter the number you want to add here: ")).strip()
                if(d == ""):
                    print("Empty value cannot be saved.....Try again")
                    continue
                if not d.isdigit():
                    print("Number can only be in digit form.")
                    continue
                if(len(d) != 10):
                    print("Number must be 10 digits")
                    continue
                break
        addc(c , d)
    elif(a == "c"):
        confirmation_1 = input("Are you sure you want to delete all of your contacts ? [Yes(Y) or No(N)]").upper().strip()
        if(confirmation_1 == "Y"):
            with open("Contact.txt" , "w")as f:
                pass
        
    elif(a == "d"):
        nam = input("Enter the name you of the contact you want to delete here: ").upper()
        numb = input("Enter the number you of the contact you want to delete here: ")
        dltc(nam , numb)