
from database.authentication import auth,db
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox,QWidget,QCheckBox
from functools import *
from users import Employer
from helperFuncs import *
UserType = 'Student' #temporay global variable for testing usersettings class



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
        Age=self.age_spin_box.text() #age will always be a valid number, there for we dont need to test it
        UserName=self.username_text_box.text()
        UserType=self.user_type_text_box.currentText() #user type only has 2 options, and by default will be student, no need for tests
        ErrorString = '' #this string will show the error message when clicking signup, if there are no errors, this will stay empty
        
        if checkEmail(email)==False:
            ErrorString = ''.join((ErrorString,' Email,'))
            flag = 1

        if checkPasswordKey(PasswordKey)==False:
            ErrorString = ''.join((ErrorString,' Password,'))
            flag = 1
           
        if checkFullName(FullName)==False:
            ErrorString = ''.join((ErrorString,' Full Name,'))
            flag = 1
           
        if checkUserName(UserName)==False:
            ErrorString = ''.join((ErrorString,' User Name,'))
            flag = 1
            
        # formating the error string acording to the users input
        ErrorString = ''.join(('Invalid ',ErrorString))
        ErrorString = ErrorString[:-1] + '.' #removing the last ',' and adding a '.' instead 


        # this function shows label with error message.
        def showError(message):
            self.wrong_data_label.setVisible(True)
            self.wrong_data_label.setText(message)

        if flag == 0:

            #Putting data base funcs in try/except to prevent app crash on error.
            try:
                auth.create_user_with_email_and_password(email,PasswordKey) # Saving new user account in FireBase auth.
                db.child('Users').push({'username':UserName,'fullname':FullName,'age':Age,'usertype':UserType,'email':email, 'resume':''}) #Saving new user data in RealTime db.
                self.change_to_login()

            except:
                showError(">> Connection Error! <<")

        else:
            showError(ErrorString)


#--------------help funcs for signup class-----------------

    def change_to_login(self): # just a test function
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1) # -1 also works?

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.CreateNewAccFunc)
        self.existing_account_button.clicked.connect(self.change_to_login)
        #self.wrong_data_label.setVisible(False) #not needed beacause the inner text is already blank, there is no text.
        

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

        # this function shows label with error message.
        def showError(message):
            self.wrong_data_label_2.setVisible(True)
            self.wrong_data_label_2.setText(message)

        if checkPasswordKey(passwordKey) and checkEmail(email):

            try: #Putting data base funcs in try/except to prevent app crash on error.
                auth.sign_in_with_email_and_password(email,passwordKey)

            # This is a test to find out what user type has entered the program
                #users = db.child('Users').get()
                #for user in users.each():
                #    if user.val()['email'] == email:
                #        print('\n\nThe users type is: ' + user.val()['usertype'])

                print(">> Welcome! <<")
                self.change_to_homepage() #goes to next screen
            except: #if could not login then there is a connection error.
                showError(">> Connection Error! <<")

        else: #if there is no existing account then show this error message
            showError("Email or password is invalid.")
    

     
#--------------help funcs for login class-----------------

    def change_to_signup(self): # change to signup screen
        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_homepage(self): #change to homepage screen
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.change_to_signup)
        self.wrong_data_label_2.setVisible(False)
        self.login_button.clicked.connect(self.logging)


    def change_forgetpassword(self):
        password = Password()
        widget.addWidget(password)
        widget.setCurrentIndex(widget.currentIndex() + 1)



#------------------------------Create/publish job class-----------------------------


class NewAd(QMainWindow):

    def __init__(self):
        super(NewAd, self).__init__()
        loadUi("ui/new_ad.ui", self)
        self.handle_buttons()

    def CreateAd(self):

        fname=self.name_textbox.text()      #
        Pnumber=self.phone_textbox.text()   #
        email=self.email_textbox.text()     #
        workExp=self.work_exp_comboBox.currentText()
        workRate=self.work_rate_comboBox.currentText()
        workPlace=self.work_place_comboBox.currentText()
        role=self.role_comboBox.currentText()
        location=self.location_comboBox.currentText()
        jobType=self.job_type_comboBox.currentText()
        degree=self.degree_comboBox.currentText()
        title=self.title_text_box.text()         #
        Java=self.Java_checkBox

        description=self.description_text_box.toPlainText()

        knowledge = [
        'Java',
        'Python',
        'Javascript',
        'Kotlin',
        'Go',
        'Swift',
        'Rust',
        'C and C++',
        'HTML',
        'SQL',
        'CSS',
        'PHP',
        'TypeScript',
        'Perl'
        ]

        if self.Javascript_checkbox.isChecked() != True:
            knowledge.remove('Javascript')

        if self.Python_checkbox.isChecked() != True:
            knowledge.remove('Python')

        if self.Kotlin_checkbox.isChecked() != True:
            knowledge.remove('Kotlin')

        if self.Go_checkbox.isChecked() != True:
            knowledge.remove('Go')

        if self.Swift_checkbox.isChecked() != True:
            knowledge.remove('Swift')

        if self.C_checkbox.isChecked() != True:
            knowledge.remove('C and C++')

        if self.SQL_checkbox.isChecked() != True:
            knowledge.remove('SQL')

        if self.CSS_checkbox.isChecked() != True:
            knowledge.remove('CSS')

        if self.PHP_checkbox.isChecked() != True:
            knowledge.remove('PHP')

        if self.TypeScript_checkbox.isChecked() != True:
            knowledge.remove('TypeScript')

        if self.Perl_checkbox.isChecked() != True:
            knowledge.remove('Perl')

        if self.Java_checkbox.isChecked() != True:
            knowledge.remove('Java')

        if self.HTML_checkbox.isChecked() != True:
            knowledge.remove('HTML')












        flag = 0
        if checkEmail(email)==False:
            ErrorString = ''.join((ErrorString,' Email,'))
            flag = 1        

        if checkFullName(fname)==False:
            ErrorString = ''.join((ErrorString,' Full Name,'))
            flag = 1

        if checkTitle(title)==False:
            ErrorString = ''.join((ErrorString,' Title,'))
            flag = 1

        if checkPhoneNumber(Pnumber)==False:
            ErrorString = ''.join((ErrorString,' Phone Number,'))
            flag = 1
            

        ErrorString = ''.join(('Invalid ',ErrorString))
        ErrorString = ErrorString[:-1] + '.'      

        #def showError(message): return
            #self.wrong_data_label.setVisible(True)    #
            #self.wrong_data_label.setText(message)    #   Qt Designer   

        if flag == 0:        

            try:
                data={
                    "title": title,
                    "description": description, 
                    "contactInfo": [fname, Pnumber, email], 
                    "knowledge": ["C++","Java","PHP"],
                    "preferences": {
                        "workExperience": workExp,
                        "daysPerWeek": workRate, 
                        "workingFrom": workPlace
                        },
                    "resumes": [],
                    "search": {
                        "role": role, 
                        "location": location, 
                        "degree": degree, 
                        "jobType": jobType
                        }
                }
                db.child('Jobs').push(data)
                self.back_to_homepage()    
            except:
                print('connection error something went wrong')      
                #showError(">> Connection Error! <<")        
        else:
            print(ErrorString)      

            #showError(ErrorString)  




        #--------------help funcs for Create/publish job class-----------------


    def back_to_homepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self):
        self.publish_button.clicked.connect(self.CreateAd)
    #    self.cancel_button.clicked.connect(self.back_to_homepage)   #  Need fix


#------------------------------------Ad Widget class------------------------------------

class AdWidget(QWidget):

    def __init__(self, id_widget=0, parent=None):
        super(AdWidget,self).__init__(parent)
        loadUi("ui/Ad_frame.ui",self)
        self.handle.buttons()
        






        #--------------help funcs for Ad Widget class-----------------

    def handle_buttons(self):
        self.edit_ad_button.clicked.connect(print('edit ad'))
        self.delete_ad_botton.clicked.connect(print('delete ad'))
        self.send_resume_button.clicked.connect(print('send resume'))
        self.send_message_button.clicked.connect(print('send message'))

    def back_to_homepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)






#------------------------------------Homepage class------------------------------------

class Homepage(QMainWindow):
    def __init__(self):
        super(Homepage, self).__init__()
        loadUi("ui/homepage.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons


    #def homepage_screen(self):



        #--------------help funcs for homepage class-----------------


    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_usersettings(self): # change to signup screen
        usersettings = Usersettings()
        widget.addWidget(usersettings)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_NewAd(self):
        ad = NewAd()
        widget.addWidget(ad)
        widget.setCurrentIndex(widget.currentIndex()+1)


        

    #def change_to_search_results(self): # change to signup screen
    #    search = Search_results()
    #    widget.addWidget(search)
    #    widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_out_button.clicked.connect(self.change_to_login) #for sign out button input
        self.user_settings_button.clicked.connect(self.change_to_usersettings) #for settings button input
        #self.search_button.clicked.connect(self.new_ad) #for search button input
        #self.free_search_button.clicked.connect(self.change_to_search_results)
        #self.advanced_search_button.clicked.connect(self.change_to_search_results)
        self.new_ad_button.clicked.connect(self.change_to_NewAd)

#-------------------------------Password class------------------------------------
class Password(QMainWindow):
    def __init__(self):
        super(Password, self).__init__()
        loadUi("ui/inputpassword.ui", self)  # file
        self.ok.clicked.connect(self.change_to_signup)

    def change_to_signup(self):

        signup = Signup()
        widget.addWidget(signup)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    # check
    def checkPasswordKey(self, passkey):
        if passkey == '':
            return False
        elif passkey != " ":
            countL = 0
            countN = 0
            index = 0
            for letter in passkey:
                if 'A' <= passkey <= 'Z':
                    countL += 1  # .
                    index += 1
                if '1' <= letter <= '9':  # check for password.
                    countL += 1
                    index += 1
            if countN >= 1 and countN >= 1:
                return True
        else:
            return False
        # passkey.islower() or passkey.isalpha():
        #   return False  # returns false if there are no uppercase letters or no numbers
        # return True

    def check(self):
        password = self.inputpassword.text()
        if self.checkPasswordKey(password):
            # update the data base
            self.change_to_signup()  # goes to next screen
        else:
            self.error.setText("Error! invalid Password")


#------------------------------------Usersettings class------------------------------------

class Usersettings(QMainWindow):
    def __init__(self):
        super(Usersettings, self).__init__()
        if UserType == 'Student':
            loadUi("ui/usersettings_student.ui", self) # file
        else:
            loadUi("ui/usersettings.ui", self)
        self.handle_buttons() 



        #--------------help funcs for usersettings class-----------------

    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def back_to_homepage(self): # back to previous screen
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_out_button.clicked.connect(self.change_to_login) #for sign out button input
        self.back_button.clicked.connect(self.back_to_homepage) #for going back to previous screen







#----------------------------------------Main----------------------------------


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # creates a Stack of widgets(windows)

login = Login()
widget.addWidget(login) # adding the first window to the stack
widget.show() # showing the stack of widgets, first window will be showen first

try:
    sys.exit(app.exec_()) # tring to run the app
except:
    print("Exiting")
