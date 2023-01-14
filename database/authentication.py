
# Test for adding an authentication database

import pyrebase
import datetime

firebaseConfig ={
'apiKey': "AIzaSyAwzsiCVmWkqAwh_zDR1XDsFbl_1g3vicw",
'authDomain': "dj-test-ac00d.firebaseapp.com",
'databaseURL': "https://dj-test-ac00d-default-rtdb.asia-southeast1.firebasedatabase.app",
'projectId': "dj-test-ac00d",
'storageBucket': "dj-test-ac00d.appspot.com",
'messagingSenderId': "324559082205",
'appId': "1:324559082205:web:bc45a327ebcce2a30b0134",
'measurementId': "G-4FS7N8MX70"
};
current_day = int(datetime.datetime.now().day)
current_month = str(datetime.datetime.now().month)
current_year = str(datetime.datetime.now().year)

current_date = current_year + "/" + current_month

firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()

#------------------------------ Activity Report -----------------------------------

if current_day == 1:                                                   
    db.child('Reports').child('Activity').child(current_date).update({          #################################################
        'Student Create Acc':0,                                                 ##   If today is the first day of the month,   ##                   
        'Employer Create Acc':0,                                                ##  this part of the code will automatically   ##
        'Student Delete Acc':0,                                                 ## create a new empty report in the database.  ##
        'Employer Delete Acc':0                                                 #################################################
        })

EmployerAccCounter = db.child('Reports').child('Activity').child(current_date).child('Employer Create Acc').get().val()
StudentDeleteAccCounter = db.child('Reports').child('Activity').child(current_date).child('Student Delete Acc').get().val()
EmployerDeleteAccCounter = db.child('Reports').child('Activity').child(current_date).child('Employer Delete Acc').get().val()
StudentAccCounter = db.child('Reports').child('Activity').child(current_date).child('Student Create Acc').get().val()


#for u in db.child('Users').get().each():

    #print(u.val()['username'])
    #print(u.key())                   
    # print(u.val()['contactInfo'])   # list with contact info of the employer who posted the ad.
    # print(u.val()['resumes'])       #dictionary with every resume that was sent to each Job in db.
    # print(u.val()['search'])
    #for i in u.val()['search'].values():
    #     print(i)




#UpdateReport = db.child('Reports').child('Activity').child(current_date)



#SomeUser = db.child("Users").order_by_child('email').equal_to('name@name.name').get().val() # Search user by email example.

#pushing some job adds to the database, you can use these lines, 
#just change up the information and run THIS file. 
#or you can take these lines elsewhere and run there. 
#adding stuff this way allows for randomly generated keys for the database for added security

##this is the data you want to push to the database, is something went wrong you can go into the database URL and change stuff there btw
#data={
#    "title": "Microsoft Needs A System Analyst",
#    "description": "bla bla bla this is some text", 
#    "contactInfo": ["Lisa Doe", "0509988556", "email5@gmail.com"], 
#    "knowledge": ["C++","Java","PHP"],
#    "preferences": {
#        "workExperience": "more then 5 years",
#        "daysPerWeek": "more then 3 days", 
#        "workingFrom": "hybrid"
#        },
#    "search": {
#        "role": "Business systems analyst", 
#        "location": "Tel Aviv-Yafo", 
#        "degree": "Ph.D (3nd)", 
#        "jobType": "Full Time"
#        }
#}


##this addes the above data into the 'Jobs' section of the realtime database
    #db.child('Jobs').push(data)

##this addes data into the 'Users' section of the realtime database into each user in a specific key
#users = db.child('Users').get()
#for user in users.each():
    #db.child('Users').child((user.key())).child('preferences').push(data)





