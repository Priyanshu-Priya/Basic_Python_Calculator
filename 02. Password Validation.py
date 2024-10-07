#Password Validation 
def ask_password():
    password = input("Enter Your Password ")
    if len(password) >=8:
        check_password(password)
    else:
        print("Invalid Password\n")
        print("Your Password Should not be less than 8 Characters")
         


def check_password(check_pass):
    flag_upper = 0
    flag_lower = 0
    flag_num = 0
    flag_symbol = 0
    for char in check_pass:
        if  char.isupper():
            flag_upper += 1
        elif char.islower():
            flag_lower += 1
        elif char.isdigit():
            flag_num += 1
        else:
            flag_symbol += 1
    validate(flag_upper,flag_lower,flag_num,flag_symbol)
   
        

def validate(a,b,c,d):
    if a >= 1 and b >=1 and c>= 1 and d >= 1:
        print("Valid Password")
    if a == 0:
        print("Invalid Password\n")
        print("One Uppercase Character is Missing in the Password")
    if b == 0:
        print("Invalid Password\n")
        print("One Lowercase Character is Missing in the Password")
    if c == 0:
        print("Invalid Password\n")
        print("One Number  is Missing in the Password")
    if d == 0:
        print("Invalid Password\n")
        print("One Symbol  is Missing in the Password")
        
ask_password()