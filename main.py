
# Test for creating a window with PyQt5
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

# This is a Signup window object
class Signup(QMainWindow):
    def __init__(self):
        super(Signup, self).__init__()
        loadUi("ui/signup.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons

    def printTest(self): # just a test function
        self.testInput()
        print('this is a test\n')

    def change(self): # just a test function
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # -1 also works?

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.printTest)
        self.existing_account_button.clicked.connect(self.change)

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

    def change(self): # just a test function
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.change)




app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # creates a Stack of widgets(windows)

login = Login()
widget.addWidget(login) # adding the first window to the stack

widget.show() # showing the stack of widgets, first window will be showen first

try:
    sys.exit(app.exec_()) # tring to run the app
except:
    print("Exiting")

