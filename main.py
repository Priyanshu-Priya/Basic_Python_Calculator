print('hello world')
a = int(input('Enter the First No. You Want To Operate: '))
c = str(input('Enter Your Operator: '))
b = int(input('Enter the Second No. You WantTo Operate: '))

if c == '+':
    print(f"The Addition of your Numbers are :  {a + b}")

elif c == '-':
    print(f"The Subtraction of your Numbers are : - {a - b}")

elif c == '*':
    print(f"The Multiplication of your Numbers are : - {a * b}")
elif c == '/':
    if b != 0:  # Check to prevent division by zero
        print(f"The Division of your Numbers are : - {a/b}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    print("Invalid Operator")