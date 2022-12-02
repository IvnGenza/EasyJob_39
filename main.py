
# Test for creating a window with PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("ui/login.ui", self) # file
        self.show()
        self.handel_buttons()
      
    
    def login_button1(self):
        print("Login works")

    def handel_buttons(self):
        self.login_button.clicked.connect(self.login_button1) #function that handles all buttons, calls the buttons functions
        








def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()

