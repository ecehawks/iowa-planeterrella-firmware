# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manual.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pyrebase
from time import sleep

# Set up and configure Firebase Connection
config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}
firebase = pyrebase.initialize_app(config)
db = firebase.database()
db.update({"connected":"1"})

# Build Application GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(990, 349)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(620, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(543, 0, 20, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(830, 50, 96, 181))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lowButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.lowButton.setChecked(False)
        self.lowButton.setObjectName("lowButton")
        # Testing Radio Button Selection
        self.lowButton.toggled.connect(lambda:self.btnstate(self.lowButton))
        self.verticalLayout_2.addWidget(self.lowButton)
        self.medButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.medButton.setChecked(True)
        self.medButton.setObjectName("medButton")
        # Testing Radio Button Selection
        self.medButton.toggled.connect(lambda:self.btnstate(self.medButton))
        self.verticalLayout_2.addWidget(self.medButton)
        self.highButton = QtWidgets.QRadioButton(self.layoutWidget)
        self.highButton.setObjectName("highButton")
        # Testing Radio Button Selection
        self.highButton.toggled.connect(lambda:self.btnstate(self.highButton))
        self.verticalLayout_2.addWidget(self.highButton)
        self.pressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pressureLabel.setGeometry(QtCore.QRect(810, 20, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setObjectName("pressureLabel")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(620, 50, 113, 181))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auroraButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.auroraButton.setChecked(True)
        self.auroraButton.setObjectName("auroraButton")
        # Testing Radio Button Selection
        self.auroraButton.toggled.connect(lambda:self.btnstate(self.auroraButton))
        self.verticalLayout.addWidget(self.auroraButton)
        self.radiationButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.radiationButton.setObjectName("radiationButton")
        # Testing Radio Button Selection
        self.radiationButton.toggled.connect(lambda:self.btnstate(self.radiationButton))
        self.verticalLayout.addWidget(self.radiationButton)
        self.ringButton = QtWidgets.QRadioButton(self.layoutWidget1)
        self.ringButton.setObjectName("ringButton")
        # Testing Radio Button Selection
        self.ringButton.toggled.connect(lambda:self.btnstate(self.ringButton))
        self.verticalLayout.addWidget(self.ringButton)
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setGeometry(QtCore.QRect(290, 80, 191, 91))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.spinBox = QtWidgets.QSpinBox(self.splitter)
        self.spinBox.setObjectName("spinBox")
        self.voltageLabel = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setObjectName("voltageLabel")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(780, 0, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uiowa Planeterella"))
        self.modeLabel.setText(_translate("MainWindow", "Select Mode"))
        self.lowButton.setText(_translate("MainWindow", "Low"))
        self.medButton.setText(_translate("MainWindow", "Medium"))
        self.highButton.setText(_translate("MainWindow", "High"))
        self.pressureLabel.setText(_translate("MainWindow", "Select Pressure"))
        self.auroraButton.setText(_translate("MainWindow", "Aurora"))
        self.radiationButton.setText(_translate("MainWindow", "Radiation Belts"))
        self.ringButton.setText(_translate("MainWindow", "Ring Current"))
        self.voltageLabel.setText(_translate("MainWindow", "Voltage"))
    
    # Function for handling Pressure selection
    def btnstate(self, b):
        #print("In button state fnc")
        if b.text() == "Low":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"air_pressure": "Low"})      
        if b.text() == "Medium":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"air_pressure": "Medium"})
        if b.text() == "High":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"air_pressure": "High"})
        if b.text() == "Aurora":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"mode": "Aurora"})
        if b.text() == "Radiation Belts":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"mode": "Radiation Belts"})
        if b.text() == "Ring Current":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                db.update({"mode": "Ring Current"})

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

