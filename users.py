from abc import ABC, abstractmethod
from database.authentication import auth,db

class User():
    def __init__(self, fullname, age, username, email):
        self.Fullname = fullname
        self.Age = age
        self.Username = username
        self.Email = email
     
    def SearchUser(self, Email):
        users = db.child('Users').get()
        for user in users.each():
            if user.val()['email'] == Email:
                return user
        return None
   
    def setFullname(self, temp):
        user = self.SearchUser(self.Email)
        if user != None:
            self.Fullname = temp
            db.child('Users').child((user.key())).update({"fullname":temp})

    def setAge(self, temp):
        user = self.SearchUser(self.Email)
        if user != None:
            self.Age = temp
            db.child('Users').child((user.key())).update({"age":temp})
     
    def setUsername(self, temp):
        user = self.SearchUser(self.Email)
        if user != None:
            self.Username = temp
            db.child('Users').child((user.key())).update({"username":temp})

    def setEmail(self, temp):
        user = self.SearchUser(self.Email)
        if user != None:
            self.Email = temp
            db.child('Users').child((user.key())).update({"email":temp})

class Student(User):
    def __init__(self, fullname, age, username, email, usertype, preferences): 
        super(Student,self).__init__(fullname, age, username, email)
        self.Usertype = usertype
        self.Preferences = preferences #dictionary from database 
    
    def setPreferences(self, key, value):
        self.Preferences[key] = value #giving the key its value
    # we need to add setResume to class

class Employer(User):
    def __init__(self, fullname, age, username, email, usertype, jobAds): 
        super(Employer,self).__init__(fullname, age, username, email)
        self.Usertype = usertype
        self.JobAds = jobAds #JobAds is an array of dicitionaries

    def setJobAds(self, job):
       self.JobAds.append(job) #job is a dicitionary
