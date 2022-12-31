
# this is a unit test file for the helper fuctions file.

from helperFuncs import *
import unittest


class Test(unittest.TestCase):

    def test_checkPasswordKey(self):
        self.assertTrue(checkPasswordKey('12345Name'))
        self.assertFalse(checkPasswordKey('12345name'))
        self.assertFalse(checkPasswordKey('name'))
        self.assertFalse(checkPasswordKey('Name'))
        print("Test 1 success\n")

    def test_checkEmail(self):
        self.assertTrue(checkEmail('test@mail.com'))
        self.assertFalse(checkEmail('test@mail'))
        self.assertFalse(checkEmail('test.com'))
        self.assertFalse(checkEmail('test'))
        print("Test 2 success\n")

    def test_checkFullName(self):
        self.assertTrue(checkFullName('First Last'))
        self.assertFalse(checkFullName('First'))
        self.assertFalse(checkFullName('First '))
        self.assertFalse(checkFullName('First 234'))
        print("Test 3 success\n")

    def test_checkUserName(self):
        self.assertTrue(checkUserName('User'))
        self.assertTrue(checkUserName('username'))
        self.assertFalse(checkUserName('user123'))
        self.assertFalse(checkUserName('User1'))
        print("Test 4 success\n")



if __name__ == '__main__':
    unittest.main()

