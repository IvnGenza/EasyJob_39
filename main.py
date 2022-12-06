import database.authentication
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

class Signup(QMainWindow):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("ui/signup.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons



    def CreateNewAccFunc(self):
        count=0

        ##confirm

        if self.checkEmail() :
            email = self.Email_text_box.text()
            count+=1


        if self.checkPasswordKey():
            count+=1
            PasswordKey=self.password_text_box.text()


        if self.checkFullName():
            count+=1
            FullName=self.full_name_text_box.text()


        if self.checkAge():
            count+=1
            Age=self.age_text_box.text()


        if self.checkUserName():
            count+=1
            serName=self.username_text_box.text()


        if self.checkPerson():
            count+=1
            UserType=self.user_type_text_box.text()


        if count==6 :

            try:

                self.change_login()
                database.authentication.auth.create_user_with_email_and_password(email,PasswordKey)

            except:
                self.wrong_data_label.setVisible(True)


# help func`s for signup class.


    def checkPasswordKey(passkey):
        return True

    def checkEmail(email):
        return True

    def checkAge(age):
        return True

    def checkFullName(fullname):
        return True

    def checkUserName(username):
        return True

    def checkePerson(person):
        return True


    def change_to_login(self): # just a test function
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # -1 also works?

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.CreateNewAccFunc)
        self.existing_account_button.clicked.connect(self.change_to_login)
        self.wrong_data_label.setVisible(False)
        self.wrong_input.setVisible(False)

#------------------------------------help func`s------------------------------------

    def testInput(self):
        #checking the the username is valid:
 
        #helper functions:
        def checkuser(username): #the username needs to have al alpha-numeric values, cant have numbers
            if username == '':
                return False
            if username.isalpha():
                return True 
            return False

        def checkpass(password): #the password needs to have atleast 1 capital letter and atleast 1 number
            if password == '':
                return False
            elif password.islower() or password.isalpha():
                return False #returns false if there are no uppercase letters or no numbers
            return True


        if checkuser(self.username_text_box.text()): #this is how to check the input field's text
            print('you inputed the correct username\n') #need to check if the same username already exists in the database
        else:
            print('the username cant have numbers')

        if checkpass(self.password_text_box.text()):
            print('you inputed a correct password\n')
        else: 
            print('the password need to have atleast one Capitl letter and atleast one number')
        
        #if self.full_name_text_box.text() == "john doe":
        #    print('you inputed a correct full name\n')
        
        #if self.age_text_box.text() >= 18 and self.age_text_box.text() <= 120: #need to add a test that there are no letters in there
        #    print('you inputed a correct age\n')

        #if self.email_text_box.text() == "johndoe@mail.com":#need to check that the is @ and .com
        #    print('you inputed a correct email\n')

# This is a Login window object
class Login(QMainWindow):
    def __init__(self):
        super(Login, self).__init__()
        loadUi("ui/login.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on the signup button

    def logging(self):

        if checkPasswordKey() and checkEmail:

            email=self.username_lable.text()
            passwordKey=self.password_lable.text()

        try:
            database.authentication.auth.sign_in_with_email_and_password(email,passwordKey)
            print(">> Welcome! <<")

        except:
            self.wrong_input.setVisible(True)







#       help func`s for login class.

        def checkPasswordKey(passkey):
            return True

        def checkEmail(email):
            return True


    def change_to_signup(self): # just a test function
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.change_to_signup)

#--------------------------------help func`s--------------------------------


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # creates a Stack of widgets(windows)

login = Login()
widget.addWidget(login) # adding the first window to the stack

widget.show() # showing the stack of widgets, first window will be showen first

try:
    sys.exit(app.exec_()) # tring to run the app
except:
    print("Exiting")

