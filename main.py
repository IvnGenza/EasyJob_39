
from database.authentication import auth,db
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox,QWidget,QCheckBox
from functools import *
from users import *
from helperFuncs import *

userObj = None #global parameter



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
        global userObj #using global parameter
        email=self.username_lable.text()
        passwordKey=self.password_lable.text()

        # this function shows label with error message.
        def showError(message):
            self.wrong_data_label_2.setVisible(True)
            self.wrong_data_label_2.setText(message)

        if checkPasswordKey(passwordKey) and checkEmail(email):

            try: #Putting data base funcs in try/except to prevent app crash on error.
                auth.sign_in_with_email_and_password(email,passwordKey)
                users = db.child('Users').get()
                for user in users.each():
                    if user.val()['email'] == email:
                        if user.val()['usertype'] == 'Student': #user
                            userObj= Student(user.val()['fullname'], user.val()['age'], user.val()['username'], email, 'Student', user.val()['preferences'])
                        if user.val()['usertype'] == 'Employer':
                            userObj= Employer(user.val()['fullname'], user.val()['age'], user.val()['username'], email, 'Employer', {})
                        if user.val()['usertype'] == 'Admin':
                            userObj= Admin(user.val()['fullname'], user.val()['age'], user.val()['username'], email, 'Admin')
                
            # This is a test to find out what user type has entered the program
                #users = db.child('Users').get()
                #for user in users.each():
                #    if user.val()['email'] == email:
                #        print('\n\nThe users type is: ' + user.val()['usertype'])
                print(userObj.Fullname)
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
        self.forgotpass_button.clicked.connect(self.change_to_forgetpassword)


    def change_to_forgetpassword(self):
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

        def showError(message):
            self.wrong_data_label_3.setVisible(True)
            self.wrong_data_label_3.setText(message) 

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
        description=self.description_text_box.toPlainText()
        ErrorString = ''
        flag = 0

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
    
        if self.Rust_checkBox.isChecked() != True:
            knowledge.remove('Rust')

        if self.Python_checkBox.isChecked() != True:
            knowledge.remove('Python')

        if self.Kotlin_checkBox.isChecked() != True:
            knowledge.remove('Kotlin')

        if self.Go_checkBox.isChecked() != True:
            knowledge.remove('Go')

        if self.Swift_checkBox.isChecked() != True:
            knowledge.remove('Swift')

        if self.C_checkBox.isChecked() != True:
            knowledge.remove('C and C++')

        if self.SQL_checkBox.isChecked() != True:
            knowledge.remove('SQL')

        if self.CSS_checkBox.isChecked() != True:
            knowledge.remove('CSS')

        if self.PHP_checkBox.isChecked() != True:
            knowledge.remove('PHP')

        if self.TypeScript_checkBox.isChecked() != True:
            knowledge.remove('TypeScript')

        if self.Perl_checkBox.isChecked() != True:
            knowledge.remove('Perl')

        if self.Java_checkBox.isChecked() != True:
            knowledge.remove('Java')

        if self.HTML_checkBox.isChecked() != True:
            knowledge.remove('HTML')


        if checkEmail(email)==False:
            ErrorString = ''.join((ErrorString,' Email,'))
            flag = 1        

        if checkFullName(fname)==False:
            ErrorString = ''.join((ErrorString,' Full Name,'))
            flag = 1

        if checkTitle(title)==False:
            ErrorString = ''.join((ErrorString,' Title,'))
            flag = 1
            
        if checkDescription(description)==False:
            ErrorString = ''.join((ErrorString,' Description,'))
            flag = 1

        if checkPhoneNumber(Pnumber)==False:
            ErrorString = ''.join((ErrorString,' Phone Number,'))
            flag = 1
            

        ErrorString = ''.join(('Invalid ',ErrorString))
        ErrorString = ErrorString[:-1] + '.'      


        if flag == 0:        

            try:
                data={
                    "title": title,
                    "description": description, 
                    "contactInfo": [fname, Pnumber, email], 
                    "knowledge": knowledge,
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
                showError(">> Connection Error! <<")        
        else:
            showError(ErrorString)      





        #--------------help funcs for Create/publish job class-----------------

    def handle_buttons(self):
        self.publish_button.clicked.connect(self.CreateAd)
        self.cancel_button.clicked.connect(self.back_to_homepage)

    def back_to_homepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)



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
        loadUi("ui/homepage - Copy.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons
        self.advancedSearchWindow = None # this is a place holder for the advanced search small window

    def SearchJob(self, JobType, Degree, Location, Role):
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if job.val()['search']['degree'] == Degree or job.val()['search']['jobType']==JobType or job.val()['search']['location']==Location or job.val()['search']['role']==Role:
                print(job.val()['description'])
        return None

    def Search(self):
        if userObj.Usertype == 'Student':
            jobtype = self.comboBox_job_type.currentText()
            degree = self.comboBox_degree.currentText()
            location = self.comboBox_location.currentText()
            role = self.comboBox_role.currentText()
            self.SearchJob(jobtype, degree, location, role)



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

    def change_to_advanced_search(self):
        if self.advancedSearchWindow is None:
            self.advancedSearchWindow = AdvancedSearch()
            self.advancedSearchWindow.show()
        else:
            self.advancedSearchWindow.close()  # Close window.
            self.advancedSearchWindow = None  # Discard reference.



        

    #def change_to_search_results(self): # change to signup screen
    #    search = Search_results()
    #    widget.addWidget(search)
    #    widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_out_button.clicked.connect(self.change_to_login) #for sign out button input
        self.user_settings_button.clicked.connect(self.change_to_usersettings) #for settings button input
        self.search_button.clicked.connect(self.Search) #for search function
        #self.search_button.clicked.connect(self.new_ad) #for search button input
        #self.free_search_button.clicked.connect(self.change_to_search_results)
        self.advanced_search_button.clicked.connect(self.change_to_advanced_search)
        self.new_ad_button.clicked.connect(self.change_to_NewAd)
        
        #this gets an item from the list widget
        #abcd = self.listWidget.item(0)

        #this connects every list widget to a function when clicked
        #self.listWidget.itemClicked.connect(self.change_to_usersettings)

        #this adds an item to the list widget
        #self.listWidget.addItem('test test test')

#-------------------------------Password class------------------------------------
class Password(QMainWindow):
    def __init__(self):
        super(Password, self).__init__()
        loadUi("ui/inputpassword.ui", self)  # file
        self.handle_buttons()


    def forgetPass(self):

        email=self.email_textbox.text()

        try:
            auth.send_password_reset_email(email)
            self.error.setVisible(True)
            self.error.setText(">> Successful! <<")

        except:
            self.error.setVisible(True)
            self.error.setText(">> Error! invalid Email :( <<")

        #--------------help funcs for Password class-----------------

    def handle_buttons(self):

        self.back_login_botton.clicked.connect(self.change_to_login)
        self.send_email_botton.clicked.connect(self.forgetPass)
    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)


    # # check
    # def checkPasswordKey(self, passkey,asd):
    #     if passkey == '':
    #         return False
    #     elif passkey != " ":
    #         countL = 0
    #         countN = 0
    #         index = 0
    #         for letter in passkey:
    #             if 'A' <= passkey <= 'Z':
    #                 countL += 1  # .
    #                 index += 1
    #             if '1' <= letter <= '9':  # check for password.
    #                 countL += 1
    #                 index += 1
    #         if countN >= 1 and countN >= 1:
    #             return True
    #     else:
    #         return False
    #     # passkey.islower() or passkey.isalpha():
    #     #   return False  # returns false if there are no uppercase letters or no numbers
    #     # return True

    # def check(self):
    #     password = self.inputpassword.text()
    #     if self.checkPasswordKey(password):
    #         # update the data base
    #         self.change_to_signup()  # goes to next screen
    #     else:
    #         self.error.setText("Error! invalid Password")


#------------------------------------Usersettings class------------------------------------

class Usersettings(QMainWindow):
    def __init__(self):
        super(Usersettings, self).__init__()
        if userObj.Usertype == 'Student':
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




#------------------------------------advanced search class------------------------------------

class AdvancedSearch(QMainWindow):
    def __init__(self):
        super(AdvancedSearch, self).__init__()
        loadUi("ui/advancedSearch.ui", self) 
        self.handle_buttons() 

    def handle_buttons(self): 
        #this button should call a function that saves the data and passes into the search engine
        #self.save_settings_button.clicked.connect(self.foo) #saves the preferences of the advanced search
        pass


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
