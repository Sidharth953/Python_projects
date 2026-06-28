while True:
    a = float(input("Enter your maths marks here : "))
    b = float(input("Enter your physics marks here : "))
    c = float(input("Enter your chemistry marks here : "))

    total = a + b + c
    avg = total / 3

    print("Your total marks are:", total)
    print("Your average marks are:", avg)

    if avg >= 90:
        print("Grade : A+")
    elif avg >= 80:
        print("Grade : A")
    elif avg >= 70:
        print("Grade : B+")
    elif avg >= 60:
        print("Grade : B")
    elif avg >= 50:
        print("Grade : C")
    elif avg >= 34:
        print("Grade : D")
    else:
        print("Grade : F")

    if avg >= 34:
        print("You pass ✅")
    else:
        print("You fail ❌")