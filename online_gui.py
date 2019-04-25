# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import icons
import pyrebase
from time import sleep
import RPi.GPIO as GPIO
import Adafruit_ADS1x15

#initialize ADC 16 bit
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)
#adc = Adafruit_ADS1x15.ADS1115()
#GAIN = 2/3

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering

GPIO.setup(0, GPIO.OUT, initial=GPIO.LOW)  # Second Needle
GPIO.setup(5, GPIO.OUT, initial=GPIO.LOW)  # Top Needle
GPIO.setup(6, GPIO.OUT, initial=GPIO.LOW)  # Little Sphere (Pos)
GPIO.setup(19, GPIO.OUT, initial=GPIO.LOW) # Little Sphere (Neg)
GPIO.setup(26, GPIO.OUT, initial=GPIO.LOW) # Big Sphere

GPIO.setup(20, GPIO.OUT, initial=GPIO.LOW) # First Pressure
GPIO.setup(21, GPIO.OUT, initial=GPIO.LOW) # Second Pressure

##Buttons left##
#inhibit pin gpio 16 unless more gpio are needed
#i2c SCL pin 5 (gpio 2)
#i2c SDA pin 3 (gpio 3)

GPIO.setup(16, GPIO.OUT, initial=GPIO.LOW) # inhibit

GPIO.setup(12, GPIO.OUT) #PWM PIN
pv = GPIO.PWM(12,100)
pv.start(0)

GPIO.setup(13, GPIO.OUT)
pc = GPIO.PWM(13, 100)
pc.start(0)


config = {
  "apiKey": "AIzaSyAkHCx7BgKyYlZgToo2hZgM2g61RrKZYcU",
  "authDomain": "ui-planeterrella.firebaseapp.com",
  "databaseURL": "https://ui-planeterrella.firebaseio.com/",
  "storageBucket": "ui-planeterrella.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

change = 0

class firebaseThread(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        while True:
            air_pressure =  db.child("air_pressure").get().val()
            mode = db.child("mode").get().val()
            voltage = db.child("voltage").get().val()
            print ("%s" %mode)

        
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

    #change is set to zero when a mode is changed
    #def changeDetect(self):
    #    if change > 30:
    #        GPIO.output(0, GPIO.LOW)
    #        GPIO.output(5, GPIO.LOW)
    #        GPIO.output(6, GPIO.LOW)
    #        GPIO.output(19, GPIO.LOW)
    #        GPIO.output(26, GPIO.LOW)
    #        GPIO.output(16, GPIO.LOW)
    #        pv.ChangeDutyCycle(0)
    #        pc.ChangeDutyCycle(0)
    #        GPIO.output(13, GPIO.LOW)
    #        GPIO.output(12, GPIO.LOW)
    #    else:
    #        change += 5

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
        pv.ChangeDutyCycle(0)
        pc.ChangeDutyCycle(0)
        GPIO.output(13, GPIO.LOW)
        GPIO.output(12, GPIO.LOW)
        
        self.myThread.quit()
        #self.myThread.wait()
        self.myThread.terminate()

        print ("Powering Down")
        sleep(2) #fake news
        sys.exit()

        
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    

