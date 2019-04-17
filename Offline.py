# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manual.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sys
import icons
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

#initialize ADC 16 bit
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering

GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # Second Needle
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # Top Needle
GPIO.setup(13, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Pos)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Neg)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Big Sphere

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # First Pressure
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Second Pressure

##Buttons left##
#inhibit pin gpio 16 unless more gpio are needed
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)

GPIO.setup(16, GPIO.OUT) #PWM PIN
p = GPIO.PWM(26,100)
p.start(0)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(850, 20, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(780, 0, 20, 1211))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(1250, 180, 281, 971))
        self.layoutWidget.setObjectName("layoutWidget")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        self.lowButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.lowButton.setFont(font)
        self.lowButton.setChecked(False)
        self.lowButton.setObjectName("lowButton")
        #button pressed
        self.lowButton.toggled.connect(lambda:self.pressurebtnstate(self.lowButton))
        self.verticalLayout_2.addWidget(self.lowButton)
        self.medButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.medButton.setFont(font)
        self.medButton.setChecked(True)
        self.medButton.setObjectName("medButton")
        #button pressed
        self.medButton.toggled.connect(lambda:self.pressurebtnstate(self.medButton))
        self.verticalLayout_2.addWidget(self.medButton)
        self.highButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.highButton.setFont(font)
        self.highButton.setObjectName("highButton")
        #button pressed
        self.highButton.toggled.connect(lambda:self.pressurebtnstate(self.highButton))  
        self.verticalLayout_2.addWidget(self.highButton)
        self.pressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pressureLabel.setGeometry(QtCore.QRect(1250, 30, 271, 131))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setObjectName("pressureLabel")
        
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(1180, 0, 21, 1221))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(10, 10, 141, 121))
        self.powerButton.setStyleSheet("#powerButton{\n"
"background-color: transparent;\n"
"border-image: url(:/Power/Power.png);\n"
"background: none;\n"
"broder: none;\n"
"background-repeat: none;\n"
"\n"
"}\n"
"\n"
"#powerButton:pressed\n"
"{\n"
"    border-image: url(:/Power/PowerPressed.png);\n"
"}")
        self.powerButton.setText("")
        self.powerButton.setIconSize(QtCore.QSize(90, 90))
        self.powerButton.clicked.connect(self.powerDown)
        self.powerButton.setObjectName("powerButton")
        
        self.voltageLabelName = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabelName.setGeometry(QtCore.QRect(100, 280, 311, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.voltageLabelName.setFont(font)
        self.voltageLabelName.setObjectName("voltageLabelName")

        self.hvButton = QtWidgets.QPushButton(self.centralwidget)
        self.hvButton.setGeometry(QtCore.QRect(50, 1060, 151, 61))
        self.hvButton.setText("")
        self.hvButton.setObjectName("hvButton")
        self.hvButton.setCheckable(True)
        self.hvButton.toggle()
        self.hvButton.clicked.connect(lambda:self.buttonToggle(self.hvButton))
        self.hvButton.setIcon(QtGui.QIcon(":/HV/HVON.png"))
        self.hvButton.setIconSize(QtCore.QSize(1060,61))

        self.hvLabel = QtWidgets.QLabel(self.centralwidget)
        self.hvLabel.setGeometry(QtCore.QRect(260, 1040, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hvLabel.setFont(font)
        self.hvLabel.setObjectName("hvLabel")
        
        self.voltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabel.setGeometry(QtCore.QRect(450, 300, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setObjectName("voltageLabel")
        
        self.currentLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentLabel.setGeometry(QtCore.QRect(450, 590, 131, 71))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.currentLabel.setFont(font)
        self.currentLabel.setObjectName("currentLabel")
        
        self.currentLabelName = QtWidgets.QLabel(self.centralwidget)
        self.currentLabelName.setGeometry(QtCore.QRect(100, 580, 301, 81))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.currentLabelName.setFont(font)
        self.currentLabelName.setObjectName("currentLabelName")
        
        self.voltageSlider = QtWidgets.QSlider(self.centralwidget)
        self.voltageSlider.setGeometry(QtCore.QRect(50, 430, 661, 71))
        self.voltageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.voltageSlider.valueChanged.connect(self.valueChange)
        self.voltageSlider.setObjectName("voltageSlider")
        
        self.currentSlider = QtWidgets.QSlider(self.centralwidget)
        self.currentSlider.setGeometry(QtCore.QRect(50, 710, 661, 71))
        self.currentSlider.setOrientation(QtCore.Qt.Horizontal)
        self.currentSlider.setObjectName("currentSlider")
        
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(850, 180, 311, 971))
        self.layoutWidget1.setObjectName("layoutWidget1")
        
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.auroraButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.auroraButton.setFont(font)
        self.auroraButton.setChecked(True)
        self.auroraButton.setObjectName("auroraButton")
        self.verticalLayout.addWidget(self.auroraButton)
        self.radiationButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.radiationButton.setFont(font)
        self.radiationButton.setObjectName("radiationButton")
        self.verticalLayout.addWidget(self.radiationButton)
        self.ringButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ringButton.setFont(font)
        self.ringButton.setObjectName("ringButton")
        self.verticalLayout.addWidget(self.ringButton)
        
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(500) #.5 second
        self.timer.timeout.connect(self.voltsTimer)
        self.timer.start()        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uiowa Planeterella"))
        self.modeLabel.setText(_translate("MainWindow", "Mode"))
        self.lowButton.setText(_translate("MainWindow", "Low"))
        self.medButton.setText(_translate("MainWindow", "Medium"))
        self.highButton.setText(_translate("MainWindow", "High"))
        self.pressureLabel.setText(_translate("MainWindow", "Pressure"))
        self.voltageLabelName.setText(_translate("MainWindow", "Voltage:"))
        self.hvLabel.setText(_translate("MainWindow", "High Voltage ON"))
        self.voltageLabel.setText(_translate("MainWindow", "0"))
        self.currentLabel.setText(_translate("MainWindow", "0"))
        self.currentLabelName.setText(_translate("MainWindow", "Current:"))
        self.auroraButton.setText(_translate("MainWindow", "Aurora"))
        self.radiationButton.setText(_translate("MainWindow", "Radiation Belts"))
        self.ringButton.setText(_translate("MainWindow", "Ring Current"))

    # Function for handling Pressure selection
    def pressurebtnstate(self, b):
        #print("In button state fnc")
        if b.text() == "Low":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (20, GPIO.LOW)
                GPIO.output (21, GPIO.LOW)
                
        if b.text() == "Medium":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (20, GPIO.LOW)
                GPIO.output (21, GPIO.HIGH)
                
        if b.text() == "High":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (20, GPIO.LOW)
                GPIO.output (21, GPIO.LOW)

    #Function handles mode selection
    def modebtnstate(self, b):    
        if b.text() == "Aurora":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (5, GPIO.LOW)
                GPIO.output (6, GPIO.HIGH)
                GPIO.output (13, GPIO.LOW)
                GPIO.output (19, GPIO.LOW)
                GPIO.output (26, GPIO.HIGH)
                
        if b.text() == "Radiation Belts":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (5, GPIO.HIGH)
                GPIO.output (6, GPIO.LOW)
                GPIO.output (13, GPIO.LOW)
                GPIO.output (19, GPIO.HIGH)
                GPIO.output (26, GPIO.LOW)       
                
        if b.text() == "Ring Current":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (5, GPIO.LOW)
                GPIO.output (6, GPIO.LOW)
                GPIO.output (13, GPIO.HIGH)
                GPIO.output (19, GPIO.LOW)
                GPIO.output (26, GPIO.HIGH)
                
    
    #Will be used for sliders
    def valueChange(self):
        p.ChangeDutyCycle(self.spinBox.value())
    
    #Tier for reading power supply    
    def voltsTimer(self):
        v = adc.read_adc(0,gain=GAIN)
        volts = (v * 187.5) / (10 ** 6)
        self.voltageLabel.setText('%.2f' %volts)
        print (str(volts))
        
    #Nicely power down the device
    def powerDown(self):
        GPIO.output (5, GPIO.LOW)
        GPIO.output (6, GPIO.LOW)
        GPIO.output (13, GPIO.LOW)
        GPIO.output (19, GPIO.LOW)
        GPIO.output (26, GPIO.LOW)
        p.ChangeDutyCycle(0)
        
        print ("Powering Down")
        sleep(2) #fake news
        sys.exit()
        
    def buttonToggle(self, b):
        if self.hvButton.isChecked():
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVON.png"))
            self.hvLabel.setText("High Voltage ON")
        else:
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))    
            self.hvLabel.setText("High Voltage OFF")



def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()


