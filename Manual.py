# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manual.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

#initialize ADC 16 bit
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(26, GPIO.OUT) #PWM PIN
p = GPIO.PWM(26,100)
p.start(0)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 350)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(510, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(433, 0, 20, 581))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(690, 50, 171, 271))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lowButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.lowButton.setFont(font)
        self.lowButton.setChecked(False)
        self.lowButton.setObjectName("lowButton")
		#button pressed
        self.lowButton.toggled.connect(lambda:self.pressurebtnstate(self.lowButton))
        self.verticalLayout_2.addWidget(self.lowButton)
        self.medButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.medButton.setFont(font)
        self.medButton.setChecked(True)
        self.medButton.setObjectName("medButton")
		#button pressed
        self.medButton.toggled.connect(lambda:self.pressurebtnstate(self.medButton))
        self.verticalLayout_2.addWidget(self.medButton)
        self.highButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.highButton.setFont(font)
        self.highButton.setObjectName("highButton")
		#button pressed
        self.highButton.toggled.connect(lambda:self.pressurebtnstate(self.highButton))
        self.verticalLayout_2.addWidget(self.highButton)
        self.pressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pressureLabel.setGeometry(QtCore.QRect(700, 20, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pressureLabel.setFont(font)
        self.pressureLabel.setObjectName("pressureLabel")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(450, 50, 221, 271))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.auroraButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.auroraButton.setFont(font)
        self.auroraButton.setChecked(True)
        self.auroraButton.setObjectName("auroraButton")
		#button pressed
        self.auroraButton.toggled.connect(lambda:self.modebtnstate(self.auroraButton))		
        self.verticalLayout.addWidget(self.auroraButton)
        self.radiationButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiationButton.setFont(font)
        self.radiationButton.setObjectName("radiationButton")
		#button pressed
        self.radiationButton.toggled.connect(lambda:self.modebtnstate(self.radiationButton))
        self.verticalLayout.addWidget(self.radiationButton)
        self.ringButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ringButton.setFont(font)
        self.ringButton.setObjectName("ringButton")
		#button pressed
        self.ringButton.toggled.connect(lambda:self.modebtnstate(self.ringButton))
        self.verticalLayout.addWidget(self.ringButton)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(670, 0, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(10, 10, 81, 91))
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
        self.powerButton.setObjectName("powerButton")
        self.ringButton.toggled.connect(lambda:self.powerDown(self.powerButton))
        self.voltageLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabel_2.setGeometry(QtCore.QRect(180, 10, 191, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.voltageLabel_2.setFont(font)
        self.voltageLabel_2.setObjectName("voltageLabel_2")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(160, 60, 191, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.spinBox_2.setFont(font)
        self.spinBox_2.setObjectName("spinBox_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #timer
        self.timer = QtCore.QTimer()
        self.timer.setInterval(2000) #2 second
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
        self.auroraButton.setText(_translate("MainWindow", "Aurora"))
        self.radiationButton.setText(_translate("MainWindow", "Radiation Belts"))
        self.ringButton.setText(_translate("MainWindow", "Ring Current"))
        self.voltageLabel_2.setText(_translate("MainWindow", "Voltage"))

    # Function for handling Pressure selection
    def pressurebtnstate(self, b):
        #print("In button state fnc")
        if b.text() == "Low":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (21, GPIO.HIGH)
                GPIO.output (20, GPIO.LOW)
                GPIO.output (16, GPIO.LOW) 
        if b.text() == "Medium":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (21, GPIO.LOW)
                GPIO.output (20, GPIO.HIGH)
                GPIO.output (16, GPIO.LOW)

        if b.text() == "High":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output (21, GPIO.LOW)
                GPIO.output (20, GPIO.LOW)
                GPIO.output (16, GPIO.HIGH)

    #Function handles mode selection
    def modebtnstate(self, b):    
        if b.text() == "Aurora":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
        if b.text() == "Radiation Belts":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
        if b.text() == "Ring Current":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
    
    def valuechange(self):
        p.ChangeDutyCycle(self.spinBox.value())
        
    def voltsTimer(self):
        v = adc.read_adc(0,gain=GAIN)
        volts = (v * 187.5) / (10 ** 6)
        self.voltageLabel.setText(str(volts))
        print (str(volts))
		
	
	def powerDown(self):
		GPIO.output (21, GPIO.LOW)
        GPIO.output (20, GPIO.LOW)
        GPIO.output (16, GPIO.LOW)
		p.ChangeDutyCycle(0)
		sys.exit()
	
	
	
import icons_rc


def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
	
