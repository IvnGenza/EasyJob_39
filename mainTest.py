
# this is a unit test file for the helper fuctions file.

from turtle import home
from main import *
import unittest


class Test(unittest.TestCase):

    login = Login();

    def test_Login_To_Homepage(self):
        self.assertTrue(self.login.change_to_homepage());

    def test_Login_To_Signup(self):
        self.assertTrue(self.login.change_to_signup());

    def test_Login_To_Forgetpass(self):
        self.assertTrue(self.login.change_to_forgetpassword());
    
    def test_Login_Handle_Buttons(self):
        self.assertTrue(self.login.handle_buttons());



    signup = Signup()

    def test_Signup_To_Homepage(self):
        self.assertTrue(self.signup.change_to_login());

    def test_Signup_Handle_Buttons(self):
        self.assertTrue(self.signup.handle_buttons());



    homepage = Homepage()

    def test_Homepage_To_Login(self):
        self.assertTrue(self.homepage.change_to_login());

    def test_Homepage_To_Handle_Buttons(self):
        self.assertTrue(self.homepage.handle_buttons());
    
    def test_Homepage_To_Usersettings(self):
        self.assertTrue(self.homepage.change_to_usersettings());
    
    def test_Homepage_To_AdvancedSearch(self):
        self.assertTrue(self.homepage.change_to_advanced_search());


    
    password = Password()

    def test_Password_To_Login(self):
        self.assertTrue(self.password.change_to_login());

    def test_Password_To_Handle_Buttons(self):
        self.assertTrue(self.password.handle_buttons());
    


if __name__ == '__main__':
    unittest.main()
