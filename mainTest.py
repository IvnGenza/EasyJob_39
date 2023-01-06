
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
        #add more classes here . . . 


        # Unit Tests for Login: 
            # None

        # Unit Tests for Signup: 
            # None

        # Unit Tests for Homepage: 
            # None

        # Unit Tests for Password: 
            # None

        # Unit Tests for XXXXX: 
    


#------------------------------------------------------#
# Unit tests specific for users type EMPLOYER:
if userObj.Usertype == "Employer":

    class EmployerTests(unittest.TestCase):

        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        #add more classes here . . . 

        
        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd);
    
        def test_Homepage_To_My_Ads(self):
            self.assertTrue(self.homepage.change_to_my_ads);   

        # Unit Tests for Password:
            # None

        # Unit Tests for XXXXX: 



#------------------------------------------------------#
# Unit tests specific for user type ADMIN:
if userObj.Usertype == "Admin":

    class AdminTests(unittest.TestCase):
        
        #classes that we are gonna be testing:
        login = Login()
        signup = Signup()
        homepage = Homepage()
        password = Password()
        #add more classes here . . . 

        # Unit Tests for Login:
            # None

        # Unit Tests for Signup:
            # None

        # Unit Tests for Homepage:
        def test_Homepage_To_NewAd(self):
            self.assertTrue(self.homepage.change_to_NewAd);
    
        def test_Homepage_To_UserPopup(self):
            self.assertTrue(self.homepage.change_to_UserPopup);
        
        
        # Unit Tests for Password:
            # None

        # Unit Tests for XXXXX: 



#------------------------------------------------------#
# Unit tests for EVERY USER TYPE together (these are mutual functions that we test):
class GeneralTests(unittest.TestCase):
        
    #classes that we are gonna be testing:
    login = Login()
    signup = Signup()
    homepage = Homepage()
    password = Password()
    #add more classes here . . . 


    # Unit Tests for Login:
    def test_Login_To_Homepage(self):
        self.assertTrue(self.login.change_to_homepage);

    def test_Login_To_Signup(self):
        self.assertTrue(self.login.change_to_signup);

    def test_Login_To_Forgetpass(self):
        self.assertTrue(self.login.change_to_forgetpassword);
    
    def test_Login_Handle_Buttons(self):
        self.assertTrue(self.login.handle_buttons);



    # Unit Tests for Signup:
    def test_Signup_To_Homepage(self):
        self.assertTrue(self.signup.change_to_login);

    def test_Signup_Handle_Buttons(self):
        self.assertTrue(self.signup.handle_buttons);



    # Unit Tests for Homepage:
    def test_Homepage_To_Login(self):
        self.assertTrue(self.homepage.change_to_login);

    def test_Homepage_To_Handle_Buttons(self):
        self.assertTrue(self.homepage.handle_buttons);
    
    def test_Homepage_To_Usersettings(self):
        self.assertTrue(self.homepage.change_to_usersettings);
    
    def test_Homepage_To_AdvancedSearch(self):
        self.assertTrue(self.homepage.change_to_advanced_search);

    def test_Homepage_To_AdPopup(self):
        self.assertTrue(self.homepage.change_to_AdPopup)



    # Unit Tests for Password:
    def test_Password_To_Login(self):
        self.assertTrue(self.password.change_to_login);

    def test_Password_To_Handle_Buttons(self):
        self.assertTrue(self.password.handle_buttons);
    

    # Unit Tests for XXXXX: 


    # Unit Tests for XXXXX: 


    # Unit Tests for XXXXX: 





if __name__ == '__main__':
    unittest.main()
