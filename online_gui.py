# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'online.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import icons

class Thread(QtCore.QThread):

    def __init__(self):
        QtCore.QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        i=0
        while (i != 60):
            air_pressure = 	db.child("air_pressure").get().val()
            mode = db.child("mode").get().val()
            voltage = db.child("voltage").get().val()
            #########################
            # work done based on mode (5 GPIO)
            #
            # Current setup Little sphere is connected positive and negative
            # 1 & 7, 12 & 5, 11 & 6 are dead (off) postion
            # 2 & 8  = Top Needle, Big Sphere   		Aurora
            # 3 & 9  = Second Needle, Little sphere- 	Belts (auroral lobe)
            # 4 & 10 = Little sphere+, Big Sphere 		Ring Current
            #########################
            if (mode == "Aurora"):
                #gpio stuff
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH)
                print (mode)
                print ("\n")

            elif (mode == "Belt"):
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.HIGH)
                GPIO.output(13, GPIO.LOW)
                GPIO.output(19, GPIO.HIGH)
                GPIO.output(26, GPIO.LOW)
                print (mode)
                print ("\n")

            elif (mode == "Ring"):
                GPIO.output(5, GPIO.LOW)
                GPIO.output(6, GPIO.LOW)
                GPIO.output(13, GPIO.HIGH)
                GPIO.output(19, GPIO.LOW)
                GPIO.output(26, GPIO.HIGH)
                print (mode)
                print ("\n")

            else:
                print ("Invalid mode type passed: %s " %(mode)) 

            #################################
            # Work done based on air_pressure
            #################################
            if (air_pressure == "Low"):
                print (air_pressure)

            elif (air_pressure == "Medium"):
                print (air_pressure)

            elif (air_pressure == "High"):
                print (air_pressure)

            else:
                print ("Invalid air_pressure type passed: %s" %(air_pressure)) 


            ################
            #voltage control
            #
            #will have to do some math to figure out relation between changing pwm frequenzy and voltage increment
            ################

            #p.ChangeDutyCycle(voltage)

            sleep(1)
            i += 1
                    

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(899, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.powerButton = QtWidgets.QPushButton(self.centralwidget)
        self.powerButton.setGeometry(QtCore.QRect(10, 10, 101, 91))
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
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 120, 351, 91))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.myThread = Thread()
        self.myThread.start()
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Online Mode "))

    # Nicely power down the device
    # def powerDown(self):
        # GPIO.output (21, GPIO.LOW)
        # GPIO.output (20, GPIO.LOW)
        # GPIO.output (16, GPIO.LOW)
        # p.ChangeDutyCycle(0)
        
        ## self.myThread.quit()
        ## self.mythread.wait()
        ## self.mythread.terminate()
        
        # print ("Powering Down")
        # sleep(2) #fake news
        # sys.exit()
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()
    

