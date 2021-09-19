# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pptDesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(576, 388)
        MainWindow.setStyleSheet("background-color: rgb(70, 70, 70);\n"
"color: rgb(255, 255, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 10, 561, 361))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_1 = QtWidgets.QWidget()
        self.page_1.setObjectName("page_1")
        self.btnRock = QtWidgets.QPushButton(self.page_1)
        self.btnRock.setGeometry(QtCore.QRect(10, 300, 131, 51))
        self.btnRock.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 127);")
        self.btnRock.setObjectName("btnRock")
        self.btnPaper = QtWidgets.QPushButton(self.page_1)
        self.btnPaper.setGeometry(QtCore.QRect(220, 300, 131, 51))
        self.btnPaper.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 127);")
        self.btnPaper.setObjectName("btnPaper")
        self.btnScissors = QtWidgets.QPushButton(self.page_1)
        self.btnScissors.setGeometry(QtCore.QRect(420, 300, 131, 51))
        self.btnScissors.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 127);")
        self.btnScissors.setObjectName("btnScissors")
        self.label = QtWidgets.QLabel(self.page_1)
        self.label.setGeometry(QtCore.QRect(100, 60, 371, 51))
        self.label.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"color: rgb(85, 170, 255);")
        self.label.setObjectName("label")
        self.windowStart = QtWidgets.QLabel(self.page_1)
        self.windowStart.setGeometry(QtCore.QRect(10, 120, 541, 161))
        self.windowStart.setMinimumSize(QtCore.QSize(541, 161))
        self.windowStart.setMaximumSize(QtCore.QSize(541, 161))
        self.windowStart.setText("")
        self.windowStart.setObjectName("windowStart")
        self.label_5 = QtWidgets.QLabel(self.page_1)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 551, 51))
        self.label_5.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.stackedWidget.addWidget(self.page_1)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.player = QtWidgets.QLabel(self.page_2)
        self.player.setGeometry(QtCore.QRect(10, 70, 231, 251))
        self.player.setText("")
        self.player.setObjectName("player")
        self.computador = QtWidgets.QLabel(self.page_2)
        self.computador.setGeometry(QtCore.QRect(320, 70, 231, 251))
        self.computador.setText("")
        self.computador.setObjectName("computador")
        self.label_2 = QtWidgets.QLabel(self.page_2)
        self.label_2.setGeometry(QtCore.QRect(250, 110, 61, 131))
        self.label_2.setStyleSheet("color: rgb(255, 255, 127);\n"
"font: 72pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.page_2)
        self.label_3.setGeometry(QtCore.QRect(50, 320, 81, 41))
        self.label_3.setStyleSheet("color: rgb(85, 170, 255);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.page_2)
        self.label_4.setGeometry(QtCore.QRect(380, 310, 121, 51))
        self.label_4.setStyleSheet("color: rgb(255, 170, 0);")
        self.label_4.setObjectName("label_4")
        self.btnRestart = QtWidgets.QPushButton(self.page_2)
        self.btnRestart.setGeometry(QtCore.QRect(240, 250, 71, 51))
        self.btnRestart.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 127);")
        self.btnRestart.setObjectName("btnRestart")
        self.infoText = QtWidgets.QLabel(self.page_2)
        self.infoText.setGeometry(QtCore.QRect(10, 10, 541, 51))
        self.infoText.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";\n"
"\n"
"")
        self.infoText.setObjectName("infoText")
        self.stackedWidget.addWidget(self.page_2)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(410, 370, 151, 16))
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rock Paper Scissors"))
        self.btnRock.setText(_translate("MainWindow", "Rock"))
        self.btnPaper.setText(_translate("MainWindow", "Paper"))
        self.btnScissors.setText(_translate("MainWindow", "Scissors"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#ffff7f;\">Choice an option the under</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a name=\"tw-target-text\"/><span style=\" font-family:\'inherit\'; font-size:28px; color:#ffff7f;\">W</span><span style=\" font-family:\'inherit\'; font-size:28px; color:#ffff7f;\">elcome to R.P.S.</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">x</p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Player</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><a name=\"tw-target-text\"/><span style=\" font-family:\'inherit\'; font-size:28px; color:#ffaa00;\">c</span><span style=\" font-family:\'inherit\'; font-size:28px; color:#ffaa00;\">omputer</span></p></body></html>"))
        self.btnRestart.setText(_translate("MainWindow", "Restart"))
        self.infoText.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "Developed by Fábio Carvalho"))