# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Offline.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import board
import busio
import adafruit_mcp4725
import sys
import icons
from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

#####################################
#initialize ADC 16 bit
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)
#####################################
adc = Adafruit_ADS1x15.ADS1115()
GAIN = 2/3

#################################
#GPIO Setup
#################################
GPIO.setwarnings(False)   
GPIO.setmode(GPIO.BCM)

GPIO.setup(0, GPIO.OUT, initial=GPIO.LOW)  # Second Needle
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # Top Needle
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # Little Sphere (Pos)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Neg)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Big Sphere

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # Pressure
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Neon

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # inhibit

GPIO.setup(12, GPIO.OUT) #PWM PIN Voltage
#pv = GPIO.PWM(12,100) #can range 0-100
#pv.start(0) #start at 0

GPIO.setup(13, GPIO.OUT)#PWM Pin Current
#pc = GPIO.PWM(13, 100) #can range 0-100
#pc.start(0) #start at 0

i2c = busio.I2C(board.SCL, board.SDA)
currentdac = adafruit_mcp4725.MCP4725(i2c, address=0x62)
voltagedac = adafruit_mcp4725.MCP4725(i2c, address=0x63)


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
        ##########button pressed
        self.lowButton.toggled.connect(lambda:self.pressurebtnstate(self.lowButton))
        self.verticalLayout_2.addWidget(self.lowButton)
        
        
        #self.medButton = QtWidgets.QRadioButton(self.layoutWidget)
        #font = QtGui.QFont()
        #font.setPointSize(26)
        #self.medButton.setFont(font)
        #self.medButton.setChecked(True)
        #self.medButton.setObjectName("medButton")
        ############button pressed
        #self.medButton.toggled.connect(lambda:self.pressurebtnstate(self.medButton))
        #self.verticalLayout_2.addWidget(self.medButton)
        
        
        self.highButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.highButton.setFont(font)
        self.highButton.setObjectName("highButton")
        ############button pressed
        self.highButton.toggled.connect(lambda:self.pressurebtnstate(self.highButton))
        self.verticalLayout_2.addWidget(self.highButton)
        
        
        self.pressureLabel = QtWidgets.QLabel(self.centralwidget)
        self.pressureLabel.setGeometry(QtCore.QRect(1250, 30, 311, 131))
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
"border: none;\n"
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
        ###################power down button clicked
        self.powerButton.clicked.connect(self.powerDown)
        self.powerButton.setObjectName("powerButton")
        
        
        self.voltageLabelName = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabelName.setGeometry(QtCore.QRect(20, 280, 441, 101))
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
        self.hvButton.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
        self.hvButton.setIconSize(QtCore.QSize(1060,61))
        
        self.hvLabel = QtWidgets.QLabel(self.centralwidget)
        self.hvLabel.setGeometry(QtCore.QRect(250, 1030, 591, 111))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.hvLabel.setFont(font)
        self.hvLabel.setObjectName("hvLabel")
        
        
        self.voltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabel.setGeometry(QtCore.QRect(540, 280, 221, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setObjectName("voltageLabel")
        
        
        self.currentLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentLabel.setGeometry(QtCore.QRect(540, 570, 201, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.currentLabel.setFont(font)
        self.currentLabel.setObjectName("currentLabel")
        
        
        self.currentLabelName = QtWidgets.QLabel(self.centralwidget)
        self.currentLabelName.setGeometry(QtCore.QRect(20, 570, 501, 101))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.currentLabelName.setFont(font)
        self.currentLabelName.setObjectName("currentLabelName")
        
        
        self.voltageSlider = QtWidgets.QSlider(self.centralwidget)
        self.voltageSlider.setGeometry(QtCore.QRect(50, 430, 661, 68))
        self.voltageSlider.setOrientation(QtCore.Qt.Horizontal)
        #####################Slider changes
        voltagedac.normalized_value = (0)
        self.voltageSlider.valueChanged.connect(self.valueChangeVolt)
        self.voltageSlider.setObjectName("voltageSlider")
        
        
        self.currentSlider = QtWidgets.QSlider(self.centralwidget)
        self.currentSlider.setGeometry(QtCore.QRect(50, 710, 661, 71))
        self.currentSlider.setOrientation(QtCore.Qt.Horizontal)
        ####################Slider changes
        currentdac.normalized_value = (0)
        self.currentSlider.valueChanged.connect(self.valueChangeCurrent)
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
        self.auroraButton.setObjectName("auroraButton")
        ########button pressed
        self.auroraButton.toggled.connect(lambda:self.modebtnstate(self.auroraButton))
        self.verticalLayout.addWidget(self.auroraButton)
        
        
        self.radiationButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.radiationButton.setFont(font)
        self.radiationButton.setObjectName("radiationButton")
        ########button pressed
        self.radiationButton.toggled.connect(lambda:self.modebtnstate(self.radiationButton))
        self.verticalLayout.addWidget(self.radiationButton)
        
        
        self.ringButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.ringButton.setFont(font)
        self.ringButton.setObjectName("ringButton")
        #######button pressed
        self.ringButton.toggled.connect(lambda:self.modebtnstate(self.ringButton))
        self.verticalLayout.addWidget(self.ringButton)
        
        
        self.neon_button = QtWidgets.QPushButton(self.centralwidget)
        self.neon_button.setGeometry(QtCore.QRect(50, 900, 151, 61))
        self.neon_button.setText("")
        self.neon_button.setObjectName("neon_button")
        self.neon_button.setCheckable(True)
        self.neon_button.toggle()
        self.neon_button.clicked.connect(lambda:self.neonToggle(self.neon_button))
        self.neon_button.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
        self.neon_button.setIconSize(QtCore.QSize(900,61))        
        
        
        self.neonLabel = QtWidgets.QLabel(self.centralwidget)
        self.neonLabel.setGeometry(QtCore.QRect(260, 870, 401, 91))
        font = QtGui.QFont()
        font.setPointSize(48)
        self.neonLabel.setFont(font)
        self.neonLabel.setObjectName("neonLabel")
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
        
        
        
    
    ##############################
    #toggles HV on off
    ##############################
    def buttonToggle(self, b):
        if self.hvButton.isChecked():
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
            self.hvLabel.setText("High Voltage OFF")
            GPIO.output(16, GPIO.LOW)
        else:
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVON.png"))
            self.hvLabel.setText("High Voltage ON")
            GPIO.output(16, GPIO.HIGH)
            
            
    ##############################
    # Toggles neon 
    ##############################
    def neonToggle(self, b):
        if self.neon_button.isChecked():
            self.neon_button.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
            self.neonLabel.setText("Neon: OFF")
            #GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # Pressure shouldnt adjust this
            GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Neon
        else:
            self.neon_button.setIcon(QtGui.QIcon(":/HV/HVON.png"))
            self.neonLabel.setText("Neon: ON")
            GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # Pressure
            GPIO.setup(21, GPIO.OUT, initial=GPIO.HIGH) # Neon

            
    ###########################################    
    # Function for handling Pressure selection
    ###########################################
    def pressurebtnstate(self, b):
        #print("In button state fnc")
        if b.text() == "Low":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output(20, GPIO.LOW)

        if b.text() == "High":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output(20, GPIO.HIGH)

                
    #######################################            
    #Function handles mode selection
    #######################################
    def modebtnstate(self, b):
        if b.text() == "Aurora":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output(0, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH) #top needle
                GPIO.output(6, GPIO.LOW)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH) #big sphere

        if b.text() == "Ring Current":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output(0, GPIO.HIGH) #second needle
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(19, GPIO.HIGH) #little sphere (neg)
                GPIO.output(26, GPIO.LOW)

        if b.text() == "Radiation Belts":
            if b.isChecked() == True:
                #print(b.text()+" is selected")
                GPIO.output(0, GPIO.LOW)
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH) #little sphere (pos)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH) #big sphere

                
    ###########################
    #Voltae and current control
    ###########################
    def valueChangeVolt(self):
        value = (self.voltageSlider.value()/100)
        #print (value)
        voltagedac.normalized_value = value
        #pv.ChangeDutyCycle(self.voltageSlider.value())

    def valueChangeCurrent(self):
        currentdac.normalized_value = (self.currentSlider.value()/100)

        #pc.ChangeDutyCycle(self.currentSlider.value())

        
        
    ###################################
    #Timer for reading power supply
    ###################################
    def voltsTimer(self):
        v = adc.read_adc(0,gain=GAIN)
        volts = 1000 * ((v * 187.5) / (10 ** 6))
        i = adc.read_adc(1,gain=GAIN)
        current = 10 * ((i * 187.5) / (10 ** 6))
        self.voltageLabel.setText('%.2f' %(volts))
        self.currentLabel.setText('%.2f' %(current))
        

        
        
        
    ##############################    
    #Nicely power down the device
    ##############################
    def powerDown(self):
        GPIO.output(0, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        pv.ChangeDutyCycle(0)
        pc.ChangeDutyCycle(0)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) 
        GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW)


        print ("Powering Down")
        sleep(2) #fake news
        sys.exit()    
        
        
    ########################
    # PyQt5 auto generated
    ########################
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Uiowa Planeterella"))
        self.modeLabel.setText(_translate("MainWindow", "Mode"))
        self.lowButton.setText(_translate("MainWindow", "Low"))
        #self.medButton.setText(_translate("MainWindow", "Medium"))
        self.highButton.setText(_translate("MainWindow", "High"))
        self.pressureLabel.setText(_translate("MainWindow", "Pressure"))
        self.voltageLabelName.setText(_translate("MainWindow", "Voltage (V):"))
        self.hvLabel.setText(_translate("MainWindow", "High Volt: OFF"))
        self.voltageLabel.setText(_translate("MainWindow", "0"))
        self.currentLabel.setText(_translate("MainWindow", "0"))
        self.currentLabelName.setText(_translate("MainWindow", "Current (mA):"))
        self.auroraButton.setText(_translate("MainWindow", "Aurora"))
        self.radiationButton.setText(_translate("MainWindow", "Radiation Belts"))
        self.ringButton.setText(_translate("MainWindow", "Ring Current"))
        self.neonLabel.setText(_translate("MainWindow", "Neon: OFF"))

def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
