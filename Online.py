# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
import busio
import board
import adafruit_mcp4725
from PyQt5 import QtCore, QtGui, QtWidgets
import icons
import pyrebase
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

GPIO.setup(0, GPIO.OUT, initial=GPIO.LOW)  # Second Needle
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # Top Needle
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # Little Sphere (Pos)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Neg)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Big Sphere

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # First Pressure
#GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Neon dont need in online mode

##Buttons left##
#inhibit pin gpio 16 unless more gpio are needed
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # inhibit

#GPIO.setup(12, GPIO.OUT) #PWM PIN
#pv = GPIO.PWM(12,100)
#pv.start(0)

#GPIO.setup(13, GPIO.OUT)
#pc = GPIO.PWM(13, 100)
#pc.start(0)

i2c = busio.I2C(board.SCL, board.SDA)
currentdac = adafruit_mcp4725.MCP4725(i2c, address=0x62)
voltagedac = adafruit_mcp4725.MCP4725(i2c, address=0x63)

config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

#change = 0

class firebaseThread(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            air_pressure =  db.child("air_pressure").get().val()
            mode = db.child("mode").get().val()
            voltage = int(db.child("Voltage_Control2").get().val())
            current = int(db.child("Current_Control2").get().val())
            inhibit = int(db.child("inhibit2").get().val())
            QtWidgets.QApplication.processEvents() #waits for things to finish            

            
            ################################
            # Inhibit
            ################################
            if(inhibit):
                GPIO.output(16, GPIO.HIGH)
            else:
                GPIO.output(16, GPIO.LOW)
                         
            #################################
            # voltage control
            #################################
            if (mode == "Aurora"):
                #gpio stuff
                GPIO.output(0, GPIO.LOW)
                GPIO.output(5, GPIO.HIGH) #top needle
                GPIO.output(6, GPIO.LOW)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH) #big sphere
                print ("%s" %mode)
            elif (mode == "Ring"):
                GPIO.output(0, GPIO.HIGH) #second needle
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(19, GPIO.HIGH) #little sphere (neg)
                GPIO.output(26, GPIO.LOW)
                print ("%s" %mode)
            elif (mode == "Belt"):
                GPIO.output(0, GPIO.LOW)
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH) #little sphere (pos)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH) #big sphere
                print ("%s" %mode)
            else:
                print ("Invalid mode type passed: %s " %(mode))
                
            QtWidgets.QApplication.processEvents()#just keeping things smooth
    
            #################################
            # air_pressure control
            #################################
            if (air_pressure == "Low"):
                print ("%s\n" %air_pressure)
                GPIO.output(20, GPIO.LOW)

            elif (air_pressure == "High"):
                print ("%s\n" %air_pressure)
                GPIO.output(20, GPIO.HIGH)


            QtWidgets.QApplication.processEvents()#just keeping things smooth

            #################################
            # Change duty cycles
            # current and voltage are both values
            # 0-100 as sent by firebase
            #################################
            #pv.ChangeDutyCycle(voltage)
            #pc.ChangeDutyCycle(current) 
            currentdac.normalized_value = (current/100)
            voltagedac.normalized_value = (voltage/100)

            QtWidgets.QApplication.processEvents()

            #################################
            # Update firebase from adc
            #################################
            v = adc.read_adc(0,gain=GAIN)
            volts = int(1000 * ((v * 187.5) / (10 ** 6)))
            db.update({"voltage": volts})
            
            i = adc.read_adc(1,gain=GAIN)
            milliamps = round((10 * ((i * 187.5) / (10 ** 6))),2)
            db.update({"current": milliamps})
          
            
            QtWidgets.QApplication.processEvents()
            sleep(1)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 1200)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
               
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
        self.powerButton.clicked.connect(self.powerDown)
        self.powerButton.setObjectName("powerButton") 
        
        self.hvButton = QtWidgets.QPushButton(self.centralwidget)
        self.hvButton.setGeometry(QtCore.QRect(50, 1060, 151, 61))
        self.hvButton.setText("")
        self.hvButton.setObjectName("hvButton")
        self.hvButton.setCheckable(True)
        self.hvButton.toggle()
        self.hvButton.clicked.connect(lambda:self.buttonToggle(self.hvButton))
        self.hvButton.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
        self.hvButton.setIconSize(QtCore.QSize(1060,61))
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.myThread = firebaseThread()
        self.myThread.start()
        
        
        #timer
        #self.timer = QtCore.QTimer()
        #self.timer.setInterval(5000) #5 seconds
        #self.timer.timeout.connect(self.changeDetect)
        #self.timer.start()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
   

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Online Mode "))

    def powerDown(self):
        GPIO.output(0, GPIO.LOW)
        GPIO.output(5, GPIO.LOW)
        GPIO.output(6, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)
        GPIO.output(26, GPIO.LOW)
        GPIO.output(16, GPIO.LOW)
        #pv.ChangeDutyCycle(0)
        #pc.ChangeDutyCycle(0)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) 
                
        self.myThread.quit()
        #self.myThread.wait()
        self.myThread.terminate()

        print ("Powering Down")
        sleep(2) #fake news
        sys.exit()

        
    def buttonToggle(self, b):
        if self.hvButton.isChecked():
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVOFF.png"))
            GPIO.output(16, GPIO.LOW)
        else:
            self.hvButton.setIcon(QtGui.QIcon(":/HV/HVON.png"))
            GPIO.output(16, GPIO.HIGH)    
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    

