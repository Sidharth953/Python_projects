import random

a = random.randint(1,10)

while True:
    b = (input("Guess a number from 1 to 10 (or if u want to quit press[Q]):  " ))
    
    if(b == "Q"):
        break
    b = int(b)
    if(b == a):
        print("Congratulations you guessed it right....")
        break
    elif(b > a):
        print("The number you guessed is bigger than the answer....")
    elif(b < a):
        print("The number you guesses is smaller than the answer....")
print("Game over")