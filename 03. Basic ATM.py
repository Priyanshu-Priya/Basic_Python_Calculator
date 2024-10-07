# Features
# ATM pin 
# check balance
# change pin 
# debit
# credit
def main():
    global amount
    global Password
    Password = 4089
    amount = 100000000
    # return Password

def initial():
    pin = int(input("Enter Yor Pin "))
    if pin == Password:
        print(" Press 1 for Check balance\n Press 2 for Change Password\n Press 3 for  Withdraw\n Press 4 for Credit\n Press 5 for Exit\n")
        choice = int(input("Enter Your Choice: "))
        if choice == 1:
            checkbalance()
        elif choice == 2:
            ChangePassword()
        elif choice == 3:
            Withdraw()
        elif choice == 4:
            Credit()
        else:
            print("Thank You")
    else:
        print("Your Passwrd is Worng")


def checkbalance():
    print("Your Current Balance is " , amount)
    initial()
def Withdraw():
    global amount
    Withdraw_amount = int(input("Enter the amount you want to Withdraw: "))
    if Withdraw_amount > amount:
        print("Insufficient Amount")
    else:
        amount -= Withdraw_amount
        checkbalance()
    initial()
def Credit():
    global amount
    credit_amount = int(input("Enter the the amount"))
    amount += credit_amount
    checkbalance()
    initial()

def ChangePassword():
    global Password
    old_pass = int(input("Enter Your Old Password"))
    
    if old_pass == Password:
        new_Password = int(input(("Enter Your New Password")))
        Password = new_Password
        print("Your Password Has Been Updated")
    else:
        print("Your Entered Wrong Password")
    initial()


main()    
initial()
