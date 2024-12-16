# PJ VanDussen
# 12/16/2024
# Password Validation Project

def check_length(password):
    password_length = len(password)
    if password_length < 8:
        print('Password must have 8 charactristics')
    else:
        return 

def check_first_five(password):
    password_length = len(password)
    first_five = password[0:5]
    check_password = first_five.isalpha()
    if password_length >= 5 and check_password == False:
        return f'The first five characters must be letters only!'
    else:
        return 
    