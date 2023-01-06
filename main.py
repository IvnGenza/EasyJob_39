from database.authentication import auth,db
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QGroupBox,QWidget,QCheckBox,QDesktopWidget
from functools import *
from users import *
from helperFuncs import *

userObj = None #global parameter, this will hold the current user object like student, employer and admin.
CURRENTUSER = None #global parameter for auth 
 

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
                if UserType == 'Student':
                    db.child('Users').push({'username':UserName,'fullname':FullName,'age':Age,'usertype':UserType,'email':email,'preferences':{'location':'','role':'','workingFrom':'',}, 'resume':''}) #Saving new user data in RealTime db.
                else:
                    db.child('Users').push({'username':UserName,'fullname':FullName,'age':Age,'usertype':UserType,'email':email}) #Saving new user data in RealTime db.
                self.change_to_login()

            except:
                showError(">> Connection Error! <<")

        else:
            showError(ErrorString)


#--------------help funcs for signup class-----------------

    def change_to_login(self): # just a test function
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return True

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.CreateNewAccFunc)
        self.existing_account_button.clicked.connect(self.change_to_login)
        return True
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
                global CURRENTUSER
                CURRENTUSER = auth.sign_in_with_email_and_password(email,passwordKey)
                users = db.child('Users').get()
                for user in users.each():
                    if user.val()['email'] == email:
                        if user.val()['usertype'] == 'Student': #user
                            userObj= Student(user.val()['fullname'], user.val()['age'], user.val()['username'], email, 'Student', user.val()['preferences'], user.val()['resume']) 
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
        return True


    def change_to_homepage(self): #change to homepage screen
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return True

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_up_button.clicked.connect(self.change_to_signup)
        self.wrong_data_label_2.setVisible(False)
        self.login_button.clicked.connect(self.logging)
        self.forgotpass_button.clicked.connect(self.change_to_forgetpassword)
        return True

    def change_to_forgetpassword(self):
        password = Password()
        widget.addWidget(password)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        return True




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
                    "resumes": [{"email":"none","status":"False"}], 
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
        if userObj.Usertype == 'Admin':
            loadUi("ui/homepage_admin.ui", self) # file
        else:
            loadUi("ui/homepage.ui", self) # file
        self.handle_buttons() # allows us to listen for clicks on all the buttons
        self.advancedSearchWindow = None # this is a place holder for the advanced search small window
        self.userpopup = None #this is a place holder for a user info popup window
        self.adpopup = None #this is a place holder for a job ad info popup window
        self.deletepopup = None

        if userObj.Usertype == 'Student': #if the user is NOT an employer, hide the "add new job ad" button
            self.new_ad_button.hide() #on buttons we can use the hide method to hide them
            self.my_ads_button.hide() #only for employer 
            self.line_4.hide() 
    
    #--------------------Main Functionality Functions-----------------------#

    def Search(self): #this is a helper function that will call the main search function that will show us the jobs in the homepage screen
        #saving the data that was submited in the search bar
        jobtype = self.comboBox_job_type.currentText()
        degree = self.comboBox_degree.currentText()
        location = self.comboBox_location.currentText()
        role = self.comboBox_role.currentText()

        self.no_jobs_found_label.setText('') #setting the error message to be empty at the start
        self.listWidget.clear() #this clears all of the lists items (all previous job ads that were found)

        #if the advanced search window was opened atleast ones, then get the data that was inside that window, else just do a regular search with the regular search bar
        if self.advancedSearchWindow == None:
            self.SearchJob(jobtype, degree, location, role) #regular search 
        else:
            #getting the data from the advanced search popup window
            workExperience = self.advancedSearchWindow.searchData['workExperience']
            daysPerWeek = self.advancedSearchWindow.searchData['daysPerWeek']
            workingFrom = self.advancedSearchWindow.searchData['workingFrom']
            knowledge = self.advancedSearchWindow.searchData['knowledge'] #knowledge is an array
            self.AdvancedSearchJob(jobtype, degree, location, role, workExperience, daysPerWeek, workingFrom, knowledge) #advanced search



        
    def SearchAllJobs(self): #this method searches for all the jobs in the database and adds them to the job list
        self.listWidget.clear() #this clears all of the lists items
        #for every job in the data base, add it to the list of jobs on the screen
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            self.listWidget.addItem(job.val()['title']+' | '+job.val()['search']['location']+' | '+job.val()['search']['role']+' | '+job.val()['preferences']['workingFrom']+' | '+job.val()['search']['degree'])



    def SearchJob(self, JobType, Degree, Location, Role): #this functions performs a regular search in the data base, all the jobs that fit the description will be added to the list of jobs on the homepage screen.
        flag = 0 #flag will help us keep track of the jobs we found, if we didnt find any jobs then flag will stay 0 and then show an error message

        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if (
                job.val()['search']['degree'] == Degree or 
                job.val()['search']['jobType'] == JobType or 
                job.val()['search']['location'] == Location or 
                job.val()['search']['role'] == Role
                ): #for now the description is atleast on of the 4 search criteria must be meet, maybe later we will change it to all of the 4 criteria must be meet all together.
                
                #print(job.val()['description'])
                flag = 1 #flag = 1 means that we found at least one job ad that fits the description

                #this line adds all the jobs from the database that fit ONE OR MORE of the 4 main search criteria, adds them to the list in this order: Title | location | role | work from | degree 
                self.listWidget.addItem(job.val()['title']+' | '+job.val()['search']['location']+' | '+job.val()['search']['role']+' | '+job.val()['preferences']['workingFrom']+' | '+job.val()['search']['degree'])

        if flag == 0:
            self.no_jobs_found_label.setText('could not find jobs that fit your search') #if no job was found, paste the error message 



    def AdvancedSearchJob(self, JobType, Degree, Location, Role, WorkExperience, DaysPerWeek, WorkingFrom, Knowledge): #this function is used in the advances search, its exactly like the regular search with the only difference beening that the criteria for the search in the data base also includes the additional information found inside the advanced search window.
        flag = 0 #flag will help us keep track of the jobs we found, if we didnt find any jobs then flag will stay 0 and then show an error message

        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if (
                job.val()['search']['degree'] == Degree or 
                job.val()['search']['jobType'] == JobType or 
                job.val()['search']['location'] == Location or 
                job.val()['search']['role'] == Role or 
                job.val()['preferences']['workExperience'] == WorkExperience or 
                job.val()['preferences']['daysPerWeek'] == DaysPerWeek or 
                job.val()['preferences']['workingFrom'] == WorkingFrom or 
                all(elem in job.val()['knowledge'] for elem in Knowledge) #"all" checks if the database list contains all elements in in the Knowledge parameter list
                ): 

                flag = 1 #flag = 1 means that we found at least one job ad that fits the description

                #this line adds all the jobs from the database that fit ONE OR MORE of the 4 main search criteria, adds them to the list in this order: Title | location | role | work from | degree 
                self.listWidget.addItem(job.val()['title']+' | '+job.val()['search']['location']+' | '+job.val()['search']['role']+' | '+job.val()['preferences']['workingFrom']+' | '+job.val()['search']['degree'])

        if flag == 0:
            self.no_jobs_found_label.setText('could not find jobs that fit your search') #if no job was found, paste the error message 


    def SearchUser(self): #this function can only be called by the admin, in his version of the homepage, this fucntion works like the regular searches, but instead of searching for jobs, it searches for users in the database.
        flag = 0
        self.listWidget_users.clear()
        self.no_jobs_found_label.setText('')
        userName = self.username_textBox.text()

        users = db.child('Users').get()
        for user in users.each():
            index = user.val()['username'].find(userName) #if the loop finds a user that has a username that is the same as the username that was clicked then add that username to the list of user names
            if index != -1 and user.val()['username'] != 'Admin':
                flag = 1
                self.listWidget_users.addItem(user.val()['username'])
        
        if flag == 0:
            self.no_jobs_found_label.setText('could not find users that fit your search') #if no user was found, paste the error message 

        #--------------help funcs for homepage class-----------------

       
    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return True

    def change_to_usersettings(self): # change to user settings screen
        usersettings = Usersettings()
        widget.addWidget(usersettings)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return True

    def change_to_NewAd(self): # open the new add screen (only by employer)
        ad = NewAd()
        widget.addWidget(ad)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_advanced_search(self): # open the advanced settings screen
        self.advancedSearchWindow = AdvancedSearch()
        self.advancedSearchWindow.show()
        return True
       
    def change_to_AdPopup(self, item): #open the ad popup window when an ad is clicked
        self.adpopup = AdPopup()
        self.adpopup.SetParameters(item.text())
        self.adpopup.show()

    def change_to_UserPopup(self, item): #open the ad popup window when an ad is clicked
        self.userpopup = UserPopup()
        self.userpopup.SetParameters(item.text())
        self.userpopup.show()

    def change_to_my_ads(self): #change to my ads window for employer
        myads = MyAds()
        widget.addWidget(myads)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_out_button.clicked.connect(self.change_to_login) #for sign out button 
        self.user_settings_button.clicked.connect(self.change_to_usersettings) #for user settings button 
        self.search_button.clicked.connect(self.Search) #this is for the main search function
        self.free_search_button.clicked.connect(self.SearchAllJobs) #this is for the free search button
        self.advanced_search_button.clicked.connect(self.change_to_advanced_search) #this is for the advanced search button
        self.listWidget.itemClicked.connect(self.change_to_AdPopup) #this is for opening the different job ads on the screen after search
 
        if userObj.Usertype == 'Employer':
            self.new_ad_button.clicked.connect(self.change_to_NewAd) #only the employer has this button
            self.my_ads_button.clicked.connect(self.change_to_my_ads)

        if userObj.Usertype == 'Admin': #only the admin has these buttons, thats why we check if the current user is admin or not
            self.search_username_button.clicked.connect(self.SearchUser)
            self.listWidget_users.itemClicked.connect(self.change_to_UserPopup)
        
        return True
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
        return True

    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        return True


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

    def change_to_deletePopup(self):
        global userObj
        self.deletepopup = DeletePopup(userObj)
        self.deletepopup.show()


        #--------------help funcs for usersettings class-----------------

    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def back_to_homepage(self): # back to previous screen
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_student_resume(self): # change to login screen
        studentResume = StudentResume()
        widget.addWidget(studentResume)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_student_resume(self): # change to login screen
        studentResume = StudentResume()
        widget.addWidget(studentResume)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def change_to_my_ads(self): #change to my ads window for employer
        myads = MyAds()
        widget.addWidget(myads)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_forgetpassword(self):
        password = Password()
        widget.addWidget(password)
        widget.setCurrentIndex(widget.currentIndex() + 1)

    def handle_buttons(self): # this function handles the click of the signup button
        self.sign_out_button.clicked.connect(self.change_to_login) #for sign out button input
        self.back_button.clicked.connect(self.back_to_homepage) #for going back to previous screen
        self.delete_account_button.clicked.connect(self.change_to_deletePopup)
        self.change_password_button.clicked.connect(self.change_to_forgetpassword)
        if userObj.Usertype == 'Student':
            self.my_resume_button.clicked.connect(self.change_to_student_resume)
        if userObj.Usertype == 'Employer':
            self.my_job_ads_button.clicked.connect(self.change_to_my_ads)
        if userObj.Usertype == 'Admin':
            #hiding the buttons because the admin cant change the password, delete the account or see his jobs
            self.change_password_button.hide()
            self.delete_account_button.hide()
            self.my_job_ads_button.hide()

#------------------------------------Advanced search class------------------------------------

class AdvancedSearch(QMainWindow): #in the homepage, when the advanced search is clicked, this class is called, it allows us to filter the search with additional information that a regular search does not have.
    def __init__(self):
        super(AdvancedSearch, self).__init__()
        loadUi("ui/advancedSearch.ui", self) 
        self.handle_buttons() 
        self.searchData = { #this is the data the user inputs in the advanced search window, we then pass this data to the homepage inorder to filter the search with this additional information
            'workExperience':'',   
            'daysPerWeek':'',    
            'workingFrom':'',    
            'knowledge':[]    
        }

    def saveAdvancedSearch(self):
        #getting the information from the advanced search window
        workExp=self.comboBox_work_experience.currentText()
        workRate=self.comboBox_work_days.currentText()
        workPlace=self.comboBox_working_from.currentText()

        knowledge = ['Java','Python','Javascript','Kotlin','Go','Swift','Rust','C and C++','HTML','SQL','CSS','PHP','TypeScript','Perl']
        
        #these if statments checks what languages did the user choose in the advanced search window
        if self.checkBox_javascript.isChecked() != True:
            knowledge.remove('Javascript')
    
        if self.checkBox_rust.isChecked() != True:
            knowledge.remove('Rust')

        if self.checkBox_python.isChecked() != True:
            knowledge.remove('Python')

        if self.checkBox_kotlin.isChecked() != True:
            knowledge.remove('Kotlin')

        if self.checkBox_go.isChecked() != True:
            knowledge.remove('Go')

        if self.checkBox_swift.isChecked() != True:
            knowledge.remove('Swift')

        if self.checkBox_c_cpp.isChecked() != True:
            knowledge.remove('C and C++')

        if self.checkBox_sql.isChecked() != True:
            knowledge.remove('SQL')

        if self.checkBox_css.isChecked() != True:
            knowledge.remove('CSS')

        if self.checkBox_php.isChecked() != True:
            knowledge.remove('PHP')

        if self.checkBox_typescript.isChecked() != True:
            knowledge.remove('TypeScript')

        if self.checkBox_perl.isChecked() != True:
            knowledge.remove('Perl')

        if self.checkBox_java.isChecked() != True:
            knowledge.remove('Java')

        if self.checkBox_html.isChecked() != True:
            knowledge.remove('HTML')


        #saveing the data from the window in a dictionary and returning the dictionary
        self.searchData['workExperience'] = workExp
        self.searchData['daysPerWeek'] = workRate
        self.searchData['workingFrom'] = workPlace
        self.searchData['knowledge'] = knowledge

        self.close() #close the popup window
        


    def handle_buttons(self): 
        #this button calls a function that saves the aditional data and passes it into the search engine
        self.save_settings_button.clicked.connect(self.saveAdvancedSearch) #saves the preferences of the advanced search
        
    
    #------------------------------------AdPopup class------------------------------------

class AdPopup(QMainWindow):
    def __init__(self):
        super(AdPopup, self).__init__()
        loadUi("ui/Ad_frame.ui", self)
        self.handle_buttons() 
        self.jobReference = ''
        self.error_success_message.setText('')
        if userObj.Usertype == 'Student': #students cant edit or delete ads, only employer and admin can, thats why we disable the buttons
            self.edit_ad_button.hide()
            self.delete_ad_button.hide()
        elif userObj.Usertype == 'Admin' or userObj.Usertype == 'Employer': #the admin and employers cant send a resume, so we disable the button if the user is an admin
            self.send_resume_button.hide()
        


    def SetParameters(self,item):
        print(item)
        title = (item.split(' | '))[0]
        #print(title)
        temp =''
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if job.val()['title'] == title:
                if userObj.Usertype == 'Employer' and job.val()['contactInfo'][2] != userObj.Email:
                    self.edit_ad_button.hide()
                    self.delete_ad_button.hide()

                self.title_textBox.setText(job.val()['title'])
                self.description_textBox.setText(job.val()['description'])
                for x in job.val()['knowledge']:
                    temp += x+' , '
                temp = temp[:-2] + ' '
                self.knowledge_textBox.setText(temp)

                self.details_textBox.setText(job.val()['search']['degree']+' , '+job.val()['search']['jobType']+
                    ' , '+job.val()['search']['location']+' , '+job.val()['search']['role']+' , '+job.val()['preferences']['daysPerWeek']+' , '+job.val()['preferences']['workExperience']+' , '+job.val()['preferences']['workingFrom'])
                self.contact_info_textBox.setText(job.val()['contactInfo'][0]+ ' , '+job.val()['contactInfo'][1]+ ' , '+job.val()['contactInfo'][2])
                
                #saving the key of the job from the database for later use in sendResume, sendMessage, editAd and deleteAd functions.
                self.jobReference = job.key()
        
    def SendResume(self): #this function is called when a student presses the "send resume button" in the ad frame, this function updates the database acordingly and checks for duplications in the database.
        count,flag = 0,0
        for resume in db.child('Jobs').child(self.jobReference).child('resumes').get():
            if resume.val()["email"] == userObj.Email: #for every email in the database in the resume of this specific job ad, check if the current user email already exists
                flag = 1
                self.error_success_message.setText("you have already submited your resume to this job ad")
                break
            if resume.val()["email"] == 'none':
                break #when the ad is first created, the resumes array in the database will have an empty string in index 0, there for we need to check if the current resume array is empty or not by checking for the empty string.
            count += 1

        if flag == 0:
            data = {count:{"email":userObj.Email,"status":"False"}}
            db.child('Jobs').child(self.jobReference).child('resumes').update(data)
            self.error_success_message.setText('resume submitted successfully')
                


    def SendMessage(self):
        pass
    
    def handle_buttons(self):
        self.send_resume_button.clicked.connect(self.SendResume)
        self.send_message_button.clicked.connect(self.SendMessage)

#----------------------------------------User popup----------------------------------

class UserPopup(QMainWindow): #this is a popup window that we see when the admin clickes on some user from the user's list, in this popup window there is all the information about this specific user from the database
    def __init__(self):
        super(UserPopup, self).__init__()
        loadUi("ui/User_frame_student.ui", self) #frist we assume its a student user
        self.handle_buttons() 
        self.usernameRef = None
        self.deletepopup = None

    def SetParameters(self, UserName):
        users = db.child('Users').get()
        for user in users.each():
            if user.val()['username'] == UserName: #if the usernames match do this:
                if user.val()['usertype'] == 'Student': #then we check, if the account is actualy a sturent, if not we change the ui file
                    self.resume_textBox.setText(user.val()['resume']) #only students have resumes in the database, employers dont have it
                else:
                    loadUi("ui/User_frame_employer.ui", self)

                #adding all the data from the data base into the ui window based on the current user (username)
                self.usernameRef = UserName
                self.fullname_textBox.setText(user.val()['fullname'])
                self.username_textBox.setText(user.val()['username'])
                self.email_textBox.setText(user.val()['email'])
                self.age_textBox.setText(user.val()['age'])
                self.usertype_textBox.setText(user.val()['usertype'])


    def SendMessage(self):
        pass

    def DeleteAccount(self):
        self.deletepopup = DeletePopup(self.usernameRef)
        self.deletepopup.show()


    def handle_buttons(self): # this function handles the click of the signup button
        self.send_message_button.clicked.connect(self.SendMessage) #calls a function that send a message to the user
        self.delete_account_button.clicked.connect(self.DeleteAccount) #calls a function that deletes the given account

    #----------------------------------------DeletePopup----------------------------------
class DeletePopup(QMainWindow):
    def __init__(self,User):
        super(DeletePopup, self).__init__()
        loadUi("ui/Delete_Popup.ui", self)
        self.deleteUser = User
        self.handle_buttons() 

    def delete_account(self): #deleting the current user
        global CURRENTUSER
        users = db.child('Users').get()
        for user in users.each(): #this is loop to find the user we want to delete
            if user.val()['email'] == self.deleteUser.Email: 
                auth.delete_user_account(CURRENTUSER['idToken']) #we delete the user from auth with his id
                db.child('Users').child(user.key()).remove()  # we deletethe user from database
                self.close()
                self.change_to_login() #when we delete the account we go back to login screen

    def delete_user(self): #deleting the current user just for Admin
        users = db.child('Users').get()
        for user in users.each(): #this is loop to find the user we want to delete
            if user.val()['username'] == self.deleteUser:
                #auth.delete_user_account(self.deleteUser['idToken']) #we delete the user from auth with his id
                db.child('Users').child(user.key()).remove()  # we delete the user from database
                self.close()
                self.change_to_login() #when we delete the account we go back to login screen

    def noButton(self):
        self.close()
    
    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self): #if user is admin so he can delete a user account else
        if userObj.Usertype == 'Admin': #check if its Admin so we can delete a user
            self.yes_button.clicked.connect(self.delete_user)
        else:# if not admin - go to delete Account
            self.yes_button.clicked.connect(self.delete_account)
        
        self.no_button.clicked.connect(self.noButton) # if press no close the


#----------------------------------------MyAds---------------------------------------
class MyAds(QMainWindow):
    def __init__(self):
        super(MyAds, self).__init__()
        loadUi("ui/My_Ads.ui", self)
        self.handle_buttons()
        self.ShowAds()

    def ShowAds(self):
        flag = 0 #flag will help us keep track of the jobs we found, if we didnt find any jobs then flag will stay 0 and then show an error message
        self.listWidget.clear()
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if job.val()['contactInfo'][2] == userObj.Email: 
                flag = 1 #flag = 1 means that we found at least one job ad that fits the description
                #this line adds all the jobs from the database that fit ONE OR MORE of the 4 main search criteria, adds them to the list in this order: Title | location | role | work from | degree 
                self.listWidget.addItem(job.val()['title']+' | '+job.val()['search']['location']+' | '+job.val()['search']['role']+' | '+job.val()['preferences']['workingFrom']+' | '+job.val()['search']['degree'])

        if flag == 0:
            self.error_message_text.setText('You have no job ads!') #if no job was found, paste the error message 


    def change_to_login(self): # change to login screen
        login = Login()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_usersettings(self): # change to user settings screen
        usersettings = Usersettings()
        widget.addWidget(usersettings)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_homepage(self):
        homepage = Homepage()
        widget.addWidget(homepage)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_myAdsDetails(self,item):
        myAdsDetails = MyAdsDetails()
        myAdsDetails.ShowResume(item.text())
        widget.addWidget(myAdsDetails)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_NewAd(self): # open the new add screen (only by employer)
        ad = NewAd()
        widget.addWidget(ad)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def handle_buttons(self):
        self.sign_out_button.clicked.connect(self.change_to_login)
        self.user_settings_button.clicked.connect(self.change_to_usersettings)
        self.back_button.clicked.connect(self.change_to_homepage)
        self.new_ad_button.clicked.connect(self.change_to_NewAd)
        self.listWidget.itemClicked.connect(self.change_to_myAdsDetails) 

#----------------------------------------MyAdsDetails----------------------------------
class MyAdsDetails(QMainWindow):
    def __init__(self):
        super(MyAdsDetails, self).__init__()
        loadUi("ui/My_Ads_Details.ui", self)
        self.handle_buttons()
        self.save_changes_button.hide()
        self.ResumeFramePopup=None
        self.jobreference=None

    def ShowResume(self,item):
        title = (item.split(' | '))[0]
        flag = 0 #flag will help us keep track of the jobs we found, if we didnt find any jobs then flag will stay 0 and then show an error message
        temp=''
        self.listWidget.clear()
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if job.val()['title'] == title: 
                self.title_textBox.setText(job.val()['title'])
                self.description_textBox.setText(job.val()['description'])
                for x in job.val()['knowledge']:
                    temp += x+' , '
                temp = temp[:-2] + ' '
                self.knowledge_textBox.setText(temp)
                self.details_textBox.setText(job.val()['search']['degree']+' , '+job.val()['search']['jobType']+
                    ' , '+job.val()['search']['location']+' , '+job.val()['search']['role']+' , '+job.val()['preferences']['daysPerWeek']+' , '+job.val()['preferences']['workExperience']+' , '+job.val()['preferences']['workingFrom'])
                self.contact_info_textBox.setText(job.val()['contactInfo'][0]+ ' , '+job.val()['contactInfo'][1]+ ' , '+job.val()['contactInfo'][2])
                self.jobreference = job.key() #we catch the job for later use in next classes

                flag = 1 #flag = 1 means that we found at least one job ad that fits the description
                #this line adds all the jobs from the database that fit ONE OR MORE of the 4 main search criteria, adds them to the list in this order: Title | location | role | work from | degree 
                users = db.child('Users').get()
                for resume in db.child('Jobs').child(job.key()).child('resumes').get():
                    for user in users.each():
                        if resume.val()["email"] == user.val()['email']:    
                            self.listWidget.addItem(user.val()['fullname']+' | '+user.val()['email']+' | '+user.val()['age'])
                #break
        if flag == 0:
            self.listWidget.addItem('No resumes at the moment..')  # if employer doesnt have resumes we print a message

    def change_to_MyAds(self):
        myads = MyAds()
        widget.addWidget(myads)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def change_to_ResumeFramePopup(self,item): # open the advanced settings screen
        self.ResumeFramePopup = MyAdsResumePopup()
        self.ResumeFramePopup.SetParameters(item.text(),self.jobreference)
        self.ResumeFramePopup.show()

    #def edit_job(self): #function to edit job ad, needs more work
    #    self.edit_button.hide() #hides the edit button
    #    self.save_changes_button.show() #unhides the save changes button
    #    #makes all areas editable
    #    self.title_textBox.setReadOnly(False)
    #    self.description_textBox.setReadOnly(False)
    #    self.knowledge_textBox.setReadOnly(False)
    #    self.details_textBox.setReadOnly(False)
    #    self.contact_info_textBox.setReadOnly(False)
    #    if self.save_changes_button.clicked:
    #        self.save_changes_button.hide() #we hide the save changes button
    #        self.edit_button.show() #we unhide the edit button

    def handle_buttons(self):
        self.back_button.clicked.connect(self.change_to_MyAds)
        self.listWidget.itemClicked.connect(self.change_to_ResumeFramePopup)
        #self.edit_button.clicked.connect(self.edit_job)
        #self.delete_button.clicked.connect()


#-------------------------------My Ads Resume Frame--------------------------------

class MyAdsResumePopup(QMainWindow):
    def __init__(self):
        super(MyAdsResumePopup, self).__init__()
        loadUi("ui/My_Ads_Resume_Frame.ui", self)
        self.handle_buttons() 
        self.usersEmail=''
        self.Jobreference=None


    def SetParameters(self, item, jobreference):
        self.Jobreference = jobreference
        #finds the correct user that has the email that appears in the resumes list, then enter that user's data into the popup window
        self.usersEmail = (item.split(' | '))[1]
        users = db.child('Users').get()
        for user in users.each():
            if user.val()['email'] == self.usersEmail: #if the emails match do this:
                #adding all the data from the data base into the ui window based on the current user (username)
                self.fullname_textBox.setText(user.val()['fullname'])
                self.username_textBox.setText(user.val()['username'])
                self.email_textBox.setText(user.val()['email'])
                self.age_textBox.setText(user.val()['age'])
                self.resume_textBox.setText(user.val()['resume'])
            

    def AcceptResume(self):
        count = 0
        for resume in db.child('Jobs').child(self.Jobreference).child('resumes').get():
            if resume.val()['email'] != self.usersEmail: 
                count+=1
            else:
                try:
                    if resume.val()['status'] == "False":
                        data = {count:{"email":self.usersEmail,"status":"True"}}
                        db.child('Jobs').child(self.Jobreference).child('resumes').update(data)  
                        self.error_success_message.setText('Successfuly accepted the resume')
                    else:
                        self.error_success_message.setText('The resume has already been accepted')
                except:
                    self.error_success_message.setText('Something when wrong, try again later')
                
                break

    
    def RejectResume(self):
        pass
    
    def SendMessage(self):
        pass

    def handle_buttons(self):
        self.accept_resume_button.clicked.connect(self.AcceptResume)
        self.reject_resume_button.clicked.connect(self.RejectResume)
        self.send_message_button.clicked.connect(self.SendMessage)




#-------------------------------Student Resume Frame--------------------------------

class StudentResume(QMainWindow):
    def __init__(self):
        super(StudentResume, self).__init__()
        loadUi("ui/student_resume.ui", self)
        self.handle_buttons() 
        self.save_changes_button.hide()
        self.resume_textBox.setText(userObj.Resume)
    
    def change_to_usersettings(self): # change to user settings screen
        usersettings = Usersettings()
        widget.addWidget(usersettings)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    def edit_resume(self):
        self.edit_button.hide() #we hide edit button
        self.save_changes_button.show() #we unhide the save changes button
        self.resume_textBox.setReadOnly(False) 

    def save_changes(self):
        self.edit_button.show() 
        self.save_changes_button.hide()
        abc = self.resume_textBox.toPlainText()
        userObj.setResume(abc)
        self.resume_textBox.setReadOnly(True)

    def handle_buttons(self):
        self.back_button.clicked.connect(self.change_to_usersettings)
        self.edit_button.clicked.connect(self.edit_resume)
        self.save_changes_button.clicked.connect(self.save_changes)

#----------------------------------------Main----------------------------------


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget() # creates a Stack of widgets(windows)

login = Login()
widget.addWidget(login) # adding the first window to the stack
widget.move(320, 135) # places the page at the center of the screen
widget.show() # showing the stack of widgets, first window will be showen first

try:
    sys.exit(app.exec_()) # tring to run the app
except:
    print("Exiting")






