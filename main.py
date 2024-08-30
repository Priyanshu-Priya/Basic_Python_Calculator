print('This is a Calculator')
x = "y"
while x == "y":
    a = int(input('Enter the First No. You Want To Operate: '))
    c = str(input('Enter Your Operator: '))
    b = int(input('Enter the Second No. You Want To Operate: '))

    if c == '+':
        print(f"The Addition of your Numbers {a} and {b}  is :  {a + b}")

    elif c == '-':
        print(f"The Subtraction of your Numbers {a} and {b} is : {a - b}")

    elif c == '*':
        print(f"The Multiplication of your Numbers {a} and {b} is : {a * b}")
    elif c == '/':
        if b != 0:  # Check to prevent division by zero
            print(f"The Quotient when {a} is dividesd by {b} is :  {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    elif c == '//':
        if b != 0:  # Check to prevent division by zero
            print(f"The Division of your Numbers is :  {a // b}")
        else:
            print("Error: Division by zero is not allowed.")
    elif c == '%':
        if b != 0:  # Check to prevent division by zero
            print(f"The Reminder of your Numbers when {a} is divides by {b} is :  {a % b}")
        else:
            print("Error: Division by zero is not allowed.")

    else:
        print("Invalid Operator")

    x = input("Enter 'y' if you want to use this for further Calcualtion or Else Press any other key to exit ")
    if x != "y":
        print("Thank You For Using Our Calculator")