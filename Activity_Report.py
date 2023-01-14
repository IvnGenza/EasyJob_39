from database.authentication import *

import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5 import QtCore, QtGui, QtWidgets


#--------------------------------------------------------------
#--------------------------------------------------------------


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(895, 590)
        MainWindow.setMinimumSize(QtCore.QSize(895, 590))
        MainWindow.setMaximumSize(QtCore.QSize(895, 590))
        font = QtGui.QFont()
        font.setPointSize(16)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(895, 570))
        self.centralwidget.setMaximumSize(QtCore.QSize(895, 570))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setContentsMargins(25, 25, 25, 25)
        self.verticalLayout_2.setSpacing(25)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.date_list = QtWidgets.QListWidget(self.centralwidget)
        self.date_list.setMinimumSize(QtCore.QSize(150, 340))
        self.date_list.setMaximumSize(QtCore.QSize(150, 340))
        self.date_list.setObjectName("date_list")
        self.verticalLayout.addWidget(self.date_list)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 148, 338))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

#------------------------------------------------------------------------------------

        self.send_report_button = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.FullDateList())
        self.date_list.itemClicked.connect(self.plotOnCanvas)

#------------------------------------------------------------------------------------

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.send_report_button.sizePolicy().hasHeightForWidth())
        self.send_report_button.setSizePolicy(sizePolicy)
        self.send_report_button.setMinimumSize(QtCore.QSize(100, 30))
        self.send_report_button.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.send_report_button.setFont(font)
        self.send_report_button.setObjectName("send_report_button")
        self.verticalLayout.addWidget(self.send_report_button, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.activity_chart = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.activity_chart.sizePolicy().hasHeightForWidth())
        self.activity_chart.setSizePolicy(sizePolicy)
        self.activity_chart.setMinimumSize(QtCore.QSize(640, 450))
        self.activity_chart.setMaximumSize(QtCore.QSize(640, 450))
        self.activity_chart.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.activity_chart.setFrameShadow(QtWidgets.QFrame.Raised)
        self.activity_chart.setObjectName("activity_chart")

#------------------------------------------------------------------------------------

        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.activity_chart)  # Create a horizontal Layout in activity chart frame
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.figure = plt.figure()                                  # Create Canvas
        self.canvas = FigureCanvas(self.figure)                     
        self.horizontalLayout_4.addWidget(self.canvas)              # Add Canvas into activity chart 

#------------------------------------------------------------------------------------


        self.horizontalLayout.addWidget(self.activity_chart, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; text-decoration: underline;\">Activity Chart</span></p></body></html>"))
        self.send_report_button.setText(_translate("MainWindow", "Show reports"))


    def FullDateList(self):

        years = db.child('Reports').child('Activity').get()     #######################################
        for year in years.each():                               ##This func push every report in db into the QListWidget.
        #print(year.key())                                      ##Reports are sorted by yyyy/m.
            temp = len(year.val())                              #######################################

            for month in range(temp-1):
                date = str(year.key()) + "/" + str(month+1)
                self.date_list.addItem(date)



    def plotOnCanvas(self,item):
        self.figure.clear() #Clear the canvas.

        a = db.child('Reports').child('Activity').child(item.text()).child('Employer Create Acc').get().val()   #######################################
        b = db.child('Reports').child('Activity').child(item.text()).child('Student Delete Acc').get().val()    ##Gets value of every creating
        c = db.child('Reports').child('Activity').child(item.text()).child('Employer Delete Acc').get().val()   ## or deleting acc. move in some month.
        d = db.child('Reports').child('Activity').child(item.text()).child('Student Create Acc').get().val()    #######################################

        valLabels = ['S_CreateAc.', 'E_CreateAc.', 'S_DeleteAc.', 'E_DeleteAc.']     
        values = [a, b, c, d]

        plt.bar(valLabels,values, color = 'grey', width= 0.5)      #############################################
        plt.xlabel("Student/Employer Create/Delete Account")       ##Set names of the parameters into the graph.
        plt.ylabel("User Acc. Value")                              ############################################
        self.canvas.draw()  #show a new chart                      






# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
    


