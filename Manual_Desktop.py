# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Manual.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
import icons
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 351)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.modeLabel = QtWidgets.QLabel(self.centralwidget)
        self.modeLabel.setGeometry(QtCore.QRect(510, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.modeLabel.setFont(font)
        self.modeLabel.setObjectName("modeLabel")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(430, 0, 20, 581))
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
        self.verticalLayout_2.addWidget(self.lowButton)
        self.medButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.medButton.setFont(font)
        self.medButton.setChecked(True)
        self.medButton.setObjectName("medButton")
        self.verticalLayout_2.addWidget(self.medButton)
        self.highButton = QtWidgets.QRadioButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.highButton.setFont(font)
        self.highButton.setObjectName("highButton")
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
        self.verticalLayout.addWidget(self.auroraButton)
        self.radiationButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.radiationButton.setFont(font)
        self.radiationButton.setObjectName("radiationButton")
        self.verticalLayout.addWidget(self.radiationButton)
        self.ringButton = QtWidgets.QRadioButton(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.ringButton.setFont(font)
        self.ringButton.setObjectName("ringButton")
        self.verticalLayout.addWidget(self.ringButton)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(670, 0, 20, 581))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
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
        self.voltageLabelName = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabelName.setGeometry(QtCore.QRect(160, 10, 131, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.voltageLabelName.setFont(font)
        self.voltageLabelName.setObjectName("voltageLabelName")
        
        self.hvButton = QtWidgets.QPushButton(self.centralwidget)
        self.hvButton.setGeometry(QtCore.QRect(20, 260, 91, 41))
        self.hvButton.setText("")
        self.hvButton.setObjectName("hvButton")
        ###### toggle stuff ######
        self.hvButton.setCheckable(True)
        self.hvButton.toggle()
        self.hvButton.clicked.connect(lambda:self.buttonToggle(self.hvButton))
        self.hvButton.setIcon(QtGui.QIcon(":/HV/HVON.png"))
        self.hvButton.setIconSize(QtCore.QSize(290,41)) ##size of buttonToggle
        ########################################################
        self.hvLabel = QtWidgets.QLabel(self.centralwidget)
        self.hvLabel.setGeometry(QtCore.QRect(120, 260, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.hvLabel.setFont(font)
        self.hvLabel.setObjectName("hvLabel")
        
        self.voltageLabel = QtWidgets.QLabel(self.centralwidget)
        self.voltageLabel.setGeometry(QtCore.QRect(300, 10, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.voltageLabel.setFont(font)
        self.voltageLabel.setObjectName("voltageLabel")
        self.currentLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentLabel.setGeometry(QtCore.QRect(300, 110, 131, 51))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currentLabel.setFont(font)
        self.currentLabel.setObjectName("currentLabel")
        
        self.currentLabelName = QtWidgets.QLabel(self.centralwidget)
        self.currentLabelName.setGeometry(QtCore.QRect(160, 110, 131, 45))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.currentLabelName.setFont(font)
        self.currentLabelName.setObjectName("currentLabelName")
        
        self.voltageSlider = QtWidgets.QSlider(self.centralwidget)
        self.voltageSlider.setGeometry(QtCore.QRect(140, 60, 211, 41))
        self.voltageSlider.setOrientation(QtCore.Qt.Horizontal)
        self.voltageSlider.setObjectName("voltageSlider")
        self.currentSlider = QtWidgets.QSlider(self.centralwidget)
        self.currentSlider.setGeometry(QtCore.QRect(140, 161, 211, 41))
        self.currentSlider.setOrientation(QtCore.Qt.Horizontal)
        self.currentSlider.setObjectName("currentSlider")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

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
        self.voltageLabelName.setText(_translate("MainWindow", "Voltage:"))
        self.hvLabel.setText(_translate("MainWindow", "High Voltage ON"))
        self.voltageLabel.setText(_translate("MainWindow", "0"))
        self.currentLabel.setText(_translate("MainWindow", "0"))
        self.currentLabelName.setText(_translate("MainWindow", "Current:"))

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

