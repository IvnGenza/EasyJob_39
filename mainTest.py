
# This is a Unit Test file for the helper fuctions file.

from main import *
import unittest

# Unit tests specific for users type STUDENT:
if userObj.Usertype == "Student":

    class StudentTests(unittest.TestCase):

        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        myAdsDetails = MyAdsDetails()
        studentResume = StudentResume()
        #=-----------------------------=#


        # Unit Tests for Login: 
            # None

        # Unit Tests for Signup: 
            # None

        # Unit Tests for Homepage: 
            # None

        # Unit Tests for Password: 
            # None

        # Unit Tests for Usersettings: 


        # Unit Tests for AdPopup: 


        # Unit Tests for MyAds: 


        # Unit Tests for MyAdsDetails: 


        # Unit Tests for StudentResume: 


    


#------------------------------------------------------#
# Unit tests specific for users type EMPLOYER:
if userObj.Usertype == "Employer":

    class EmployerTests(unittest.TestCase):

        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        myAdsDetails = MyAdsDetails()
        #=-----------------------------=#
        
        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd)
    
        def test_Homepage_To_My_Ads(self):
            self.assertTrue(self.homepage.change_to_my_ads)

        # Unit Tests for Password:
            # None

        # Unit Tests for Usersettings: 


        # Unit Tests for AdPopup: 


        # Unit Tests for MyAds: 


        # Unit Tests for MyAdsDetails: 







#------------------------------------------------------#
# Unit tests specific for user type ADMIN:
if userObj.Usertype == "Admin":

    class AdminTests(unittest.TestCase):
        
        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        usersettings = Usersettings()
        adPopup = AdPopup()
        myAds = MyAds()
        myAdsDetails = MyAdsDetails()
        #=-----------------------------=#

        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd)
    
        def test_Homepage_To_UserPopup(self):
            self.assertTrue(self.homepage.change_to_UserPopup)
        
        
        # Unit Tests for Password:
            # None

        # Unit Tests for Usersettings: 


        # Unit Tests for AdPopup: 


        # Unit Tests for MyAds: 


        # Unit Tests for MyAdsDetails: 





#------------------------------------------------------#
# Unit tests for EVERY USER TYPE together (these are mutual functions that we test):
class GeneralTests(unittest.TestCase):
        
    #classes that we are gonna be testing:
    login = Login()
    signup = Signup()
    homepage = Homepage()
    password = Password()
    usersettings = Usersettings()
    adPopup = AdPopup()
    myAds = MyAds()
    myAdsDetails = MyAdsDetails()
    #=-----------------------------=#


    # Unit Tests for Login:
    def test_Login_To_Homepage(self):
        self.assertTrue(self.login.change_to_homepage)

    def test_Login_To_Signup(self):
        self.assertTrue(self.login.change_to_signup)

    def test_Login_To_Forgetpass(self):
        self.assertTrue(self.login.change_to_forgetpassword)
    
    def test_Login_Handle_Buttons(self):
        self.assertTrue(self.login.handle_buttons)



    # Unit Tests for Signup:
    def test_Signup_To_Homepage(self):
        self.assertTrue(self.signup.change_to_login)

    def test_Signup_Handle_Buttons(self):
        self.assertTrue(self.signup.handle_buttons)



    # Unit Tests for Homepage:
    def test_Homepage_To_Login(self):
        self.assertTrue(self.homepage.change_to_login)

    def test_Homepage_To_Handle_Buttons(self):
        self.assertTrue(self.homepage.handle_buttons)
    
    def test_Homepage_To_Usersettings(self):
        self.assertTrue(self.homepage.change_to_usersettings)
    
    def test_Homepage_To_AdvancedSearch(self):
        self.assertTrue(self.homepage.change_to_advanced_search)

    def test_Homepage_To_AdPopup(self):
        self.assertTrue(self.homepage.change_to_AdPopup)



    # Unit Tests for Password:
    def test_Password_To_Login(self):
        self.assertTrue(self.password.change_to_login)

    def test_Password_To_Handle_Buttons(self):
        self.assertTrue(self.password.handle_buttons)
    


    # Unit Tests for Usersettings: 
    def test_Usersettings_To_Handle_Buttons(self):
        self.assertTrue(self.usersettings.handle_buttons)
    
    #def test_Usersettings_To_(self):
    
    #def test_Usersettings_To_(self):
    

    
    # Unit Tests for AdPopup: 
    def test_AdPopup_To_Handle_Buttons(self):
        self.assertTrue(self.adPopup.handle_buttons)

    #def test_AdPopup_To_(self):
    
    #def test_AdPopup_To_(self):



    # Unit Tests for MyAds: 
    def test_MyAds_To_Handle_Buttons(self):
        self.assertTrue(self.myAds.handle_buttons)
    
    #def test_MyAds_To_(self):
    
    #def test_MyAds_To_(self):



    # Unit Tests for MyAdsDetails: 
    def test_MyAdsDetails_To_Handle_Buttons(self):
        self.assertTrue(self.myAdsDetails.handle_buttons)
        
    #def test_MyAdsDetails_To_(self):
    
    #def test_MyAdsDetails_To_(self):


 





if __name__ == '__main__':
    unittest.main()
