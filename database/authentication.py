
# Test for adding an authentication database

import pyrebase

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


firebase = pyrebase.initialize_app(firebaseConfig)
db = firebase.database()
auth = firebase.auth()
storage = firebase.storage()



SomeUser = db.child("Users").order_by_child('email').equal_to('name@name.name').get().val() # Search user by email example.


print(SomeUser)

print('123')
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



