
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



p=db.child("Data").child("Name").get().val()

print(p)