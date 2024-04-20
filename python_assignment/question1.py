def check_for_password_length(password):
    password_length = len(password)
    if password_length < 8:
        print("Password should be atleast 8 character long")
        return False
    return True

def check_uppercase(password):
    is_contains_upper  = False
    for ch in password:
        if ch.isupper():
            is_contains_upper = True
            break

    if is_contains_upper == False:
            print("Password must contain aleast one uppercase letter")
            return False
    return True

def check_lowercase(password):
    is_contains_lower  = False
    for ch in password:
        if ch.islower():
            is_contains_lower = True
            break

    if is_contains_lower == False:
            print("Password must contain aleast one lowercase letter")
            return False
    return True

def check_digit(password):
        is_contains_digit  = False
        for ch in password:
            if ch.isdigit():
                is_contains_digit = True
                break
        if is_contains_digit == False:
            print("Password must contain aleast one digit")
            return False
        
def check_specialcharacter(password):
        special_character = ",!@#$%"

        is_contains_special_characters  = False
        for ch in password:
            if ch in special_character:
                is_contains_special_characters = True
                break


        if is_contains_special_characters == False:
            print("Password must contain atleast one special characters from:",special_character)
            return False


def check_password_strength(password):
    ret = check_for_password_length(password)
    if ret == False:
        return ret
    
    ret = check_uppercase(password)
    if ret == False:
        return ret
    
    ret = check_lowercase(password) 
    if ret ==False:
        return ret
    
    ret = check_digit(password) 
    if ret ==False:
        return ret
    
    ret = check_specialcharacter(password)
    if ret ==False:
        return ret
    
    return True

while True:
     password = input("Enter your password")
     is_valid_password = check_password_strength(password)
     if is_valid_password == False:
          print("The password you entered does not match the criteria.")
          print("Enter the password again")
     else:
          print("Your password is accepted")
          break



