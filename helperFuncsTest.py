
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
    
    def test_checkTitle(self):
        self.assertTrue(checkTitle('this is a title'))
        self.assertFalse(checkTitle('ajsdfhaksjdfhadfhaskjdfhsdkjfhaskjdfsdfasfsdfsdfasdf'))
        print("Test 5 success\n")

    def test_checkDescription(self):
        self.assertTrue(checkDescription('alschgdcvhdshfasdhfshfksjadhfklshdkashfkasdhjaskdhfakjsdhfaksjdfhalksdjfhaskjfhasdkfhaklsdhfakljsdhfkajlshfdk'))
        self.assertFalse(checkDescription('abcd'))
        print("Test 6 success\n")

    def test_checkPhoneNumber(self):
        self.assertTrue(checkPhoneNumber('0546143258'))
        self.assertFalse(checkPhoneNumber('214352'))
        print("Test 7 success\n")



if __name__ == '__main__':
    unittest.main()

