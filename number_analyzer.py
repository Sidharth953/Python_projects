def analyzer(n):
    if(n % 2 == 0):
        print("The number you provided is even...")
    else:
        print("The number you provided is odd...")

while True:


    n = int(input("Enter the number here: "))

    analyzer(n)

    cont = input("If u want to continue press enter otherwise type 'exit' ")
    if(cont == "exit"):
        confirm = input("Are you sure you want to exit ?")
        if(confirm == "no"):
             continue
        else:
         break
        
    else:
        continue