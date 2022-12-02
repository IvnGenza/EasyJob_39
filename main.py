
# Test for creating a window with PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import uic

class MyGUI(QMainWindow):
    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("ui/test.ui", self) # file
        self.show()
        print("lol")

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()
