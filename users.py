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
    
    #def setPreferences(self, key, value):
    #    user = self.SearchUser(self.Email)
    #    if user != None:
    #        self.Preferences[key] = value #giving the key its value
    #        db.child('Users').child((user.key())).child('preferences').update({key:value})

    # we need to add setResume to class

class Employer(User):
    def __init__(self, fullname, age, username, email, usertype, jobAds): 
        super(Employer,self).__init__(fullname, age, username, email)
        self.Usertype = usertype
        self.JobAds = jobAds #JobAds is an array of dicitionaries

    def AddJobAds(self, job):
        self.JobAds.append(job) #job is a dicitionary

    def EditJobAds(self, index, job):
        self.JobAds[index]=job

    def DeleteJobAds(self, index):
        self.JobAds.pop(index) 

    def GetResume(self, title):
        jobs = db.child('Jobs').get()
        for job in jobs.each():
            if job.val()['title'] == title:
                return db.child('Jobs').child((job.key())).child('resumes').get().val()
        
#employer = Employer('max', '20', 'maxl', 'max@max.com', 'Employer', {}) #test 
#print(employer.GetResume('Job at apple'))

class Admin(User):
    def __init__(self, fullname, age, username, email, usertype): 
        super(Admin,self).__init__(fullname, age, username, email)
        self.Usertype = usertype
