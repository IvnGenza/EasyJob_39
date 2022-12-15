
# this is a helper functions file, all of the functions here will be tested and used in the other files of our program

import re #used in the email test function


def checkPasswordKey(passkey):
    print(passkey)
    '''gets a string. checks that the given password has atleast one capital letter and atleast one number.'''
    if passkey == '':
        return False

    elif (passkey.islower() or passkey.isalpha() or passkey.isnumeric()):
        return False #returns false if there are no uppercase letters or no numbers
    return True


def checkEmail(email):  #checks email validation
    '''gets a string. checks that the given email is correct in-terms of its build. must have "@" and "."something.'''
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #regular expression
    if(re.fullmatch(regex, email)):
            #print("Valid Email")
            return True
    else:
        #print("Invalid Email")
        return False


def checkFullName(fullname):
    '''gets a string. checks that the given full name is correct. it must have a first and a last name.'''
    if fullname == '':
        return False
    temp = fullname.split(' ')
    if len(temp) > 1: #checks if the name is valid 
        if temp[0].isalpha and temp[1].isalpha():
            return True
    else:
        #print('Invalid FullName')
        return False


def checkUserName(username):
    '''gets a string. checks that the given username is correct. a user name must have only letters and canot have any other sign.'''
    if username == '':
        return False
    if username.isalpha():
        return True 
    return False




def checkTitle(title):
    '''gets a string and checks if its length is too long.'''
    if len(title)>40:
        return False
    return True



def checkPhoneNumber(number):
    
    regex = '051/054/052/050/055/056/057/058/059'

    if re.match(str(number)[:3],regex) != True:         #regular expression
        return False
    
    if len(str(number)) != 10:      # Check if number have a correct length.
        return False

    return True





