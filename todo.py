import os
if not os.path.exists("Tasks.txt"):
    with open("Tasks.txt" , "w"):
        pass

def addtask(Task):
    with open("Tasks.txt" , "a")as f:
        f.write(Task + "\n")
        print("Task successfuly added..")

def dlttask(Task):
    task = []
    found = False
    with open("Tasks.txt","r")as f:
        for line in f:
            line = line.strip()
            if(line == ""):
                continue
            if(Task == line):
                found = True
                continue
            task.append(line)
    if(found == False):
        print("Task not found.....")
    elif(found == True):
        with open("Tasks.txt" , "w")as f:
            for i in task:
                f.write(i + "\n")
        print("Task successfuly deleted....")
while True:
    a = input("What do you want to do ?[Add tasks(n) , delete task(d) , clear whole task list(c) , view tasks(v) , exit(e)]\n -> ").lower().strip()
    if(a == "n"):
        while True:
            b = input("If you want to exit(e) or \nEnter the task you want to add here :").upper()
            if(b == "E"):
                break
            else:
                addtask(b)
    elif(a == "d"):
        while True:
            c = input("If you want to exit(e) or \nEnter the task you want to delete here: ").upper()
            if(c == "E"):
                break
            else:
                dlttask(c)
    elif(a == "c"):
        with open("Tasks.txt" , "w")as f:
            pass
            print("All tasks cleared....")
    elif(a == "v"):
        with open("Tasks.txt" , "r")as f:
            v = f.read()
            if(v == ""):
                print("You have no tasks yet......")
            else:
                print(v)
    elif(a == "e"):
        print("Thank you...")
        break
    else:
        print("Invalid input....")