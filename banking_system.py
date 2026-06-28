import os
if not os.path.exists("balance.txt"):
    with open("balance.txt" , "w")as f:
        f.write("0")
if not os.path.exists("banking_system.txt"):
    with open("banking_system.txt" , "w") as f:
        pass

class Account:
    def __init__(self , balance , acc_no):
        self.balance = balance
        self.acc_no = acc_no

    def credit(self , amount):
        self.balance += amount
        print("Rs" , amount , "has been successfully credited to  your account number" , self.acc_no)
        entry = (f"Rs {amount} was added.")
        with open("banking_system.txt" , "a") as f :
            f.write(entry + "\n")
        with open("balance.txt" , "w")as f:
            f.write(str(self.balance))

    def debit(self , amount):
        self.balance -= amount
        print("Rs" , amount , "has been successfully debited from your account number" , self.acc_no)
        entry = (f"Rs {amount} was debited.")
        with open("banking_system.txt" , "a") as f :
            f.write(entry + "\n")
        with open("balance.txt" , "w")as f:
            f.write(str(self.balance))

    def bal(self):
        with open("balance.txt" , "r")as f:
            c = float(f.read())
        print("Your account balance is " , c , "\naccount number:" , self.acc_no)
            
    def transac(self):
        with open("banking_system.txt" , "r") as f :
           print(f.read())

acc1 = Account(0 , 123456)
while True:
    a = input("What action do you want to perform ? [check balance(B) , check transaction history(T), deposit money(D) , withdraw money(W) , or exit(E)]:   ").upper()
    if(a == "E"):
        break
    elif(a == "D"):
        try:
            b = float(input("Enter the amount you want to deposit: "))
            acc1.credit(b)
        except:
            print("Invalid input...")
        
    elif(a == "W"):
        try:
            b = float(input("Enter the amount you want to withdraw: "))
            if(acc1.balance < b ):
                print("Insufficient balance")
            else:
                acc1.debit(b)
        except:
            print("Invalid input.....")
        
    elif(a == "T"):
        acc1.transac()
    elif(a == "B"):
        acc1.bal()
    else:
        print("Invalid input.....Try again.")