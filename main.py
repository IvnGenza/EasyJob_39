import database.authentication
import sys
import re
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import *

#------------------------------------Signup class------------------------------------

class Signup(QMainWindow):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("ui/signup.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons


    def CreateNewAccFunc(self):
        flag=0

        email = self.Email_text_box.text()
        PasswordKey=self.password_text_box.text()
        FullName=self.full_name_text_box.text()
        Age=self.age_text_box.text()
        UserName=self.username_text_box.text()
        UserType=self.user_type_text_box.currentText()
        ErrorString = ''
        
        if self.checkEmail(email)==False:
             ErrorString+='Invalid Email '
             flag = 1

        if self.checkPasswordKey(PasswordKey)==False:
            ErrorString+='Invalid Password '
            flag = 1
           
        if self.checkFullName(FullName)==False:
            ErrorString+='Invalid Name '
            flag = 1
    
        #if self.checkAge(Age)==False:
        #    ErrorString+='Invalid Age '
        #    flag = 1
           
        if self.checkUserName(UserName)==False:
            ErrorString+='Invalid UserName '
            flag = 1
            
        if flag == 0:
            self.change_login()
            database.authentication.auth.create_user_with_email_and_password(email,PasswordKey)
        else:
            self.wrong_data_label.setVisible(True)
            self.wrong_data_label.setText(ErrorString)

# help func`s for signup class.


    def checkPasswordKey(self, passkey):
        if passkey == '':
            return False
        elif passkey.islower() or passkey.isalpha():
            return False #returns false if there are no uppercase letters or no numbers
        return True

    def checkEmail(self, email):  #checks email validation
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #regular expression
        if(re.fullmatch(regex, email)):
             print("Valid Email")
             return True 
 
        else:
            print("Invalid Email")
            return False

    #def checkAge(self, age):
    #    return True

    def checkFullName(self, fullname):
       if fullname == '':
           return False
       temp = fullname.split(' ')
       if temp[0].isalpha and temp[1].isalpha():
           return True

    def checkUserName(self, username):
        if username == '':
            return False
        if username.isalpha():
            return True 
        return False



    def change_to_login(self): # just a test function
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # -1 also works?

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.CreateNewAccFunc)
        self.existing_account_button.clicked.connect(self.change_to_login)
        self.wrong_data_label.setVisible(False)
        #self.wrong_input.setVisible(False)

#------------------------------------Login class------------------------------------
 

# This is a Login window object
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/login.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on the signup button

    def logging(self):

        email=self.username_lable.text()
        passwordKey=self.password_lable.text()

        if self.checkPasswordKey(passwordKey) and self.checkEmail(email):
             database.authentication.auth.sign_in_with_email_and_password(email,passwordKey)
             print(">> Welcome! <<")

        else:   
             self.wrong_data_label_2.setVisible(True)
    

     
#       help func`s for login class.

    def checkPasswordKey(self, passkey):
        if passkey == '':
            return False
        elif passkey.islower() or passkey.isalpha():
            return False #returns false if there are no uppercase letters or no numbers
        return True

    def checkEmail(self, email):
        regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b' #regular expression
        if(re.fullmatch(regex, email)):
             print("Valid Email")
             return True 
 
        else:
            print("Invalid Email")
            return False

    def change_to_signup(self): # just a test function
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.change_to_signup)
        self.wrong_data_label_2.setVisible(False)
        self.login_button.clicked.connect(self.logging)

#----------------------------------------Main----------------------------------


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # creates a Stack of widgets(windows)

login = Login()
widget.addWidget(login) # adding the first window to the stack
widget.setFixedHeight(900)
widget.setFixedWidth(1500)
widget.show() # showing the stack of widgets, first window will be showen first

try:
    sys.exit(app.exec_()) # tring to run the app
except:
    print("Exiting")
