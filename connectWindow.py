# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'connectWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_connectWindow(object):
    def setupUi(self, connectWindow):
        from setup import searchFile
        connectWindow.setObjectName("connectWindow")
        connectWindow.resize(275, 150)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        connectWindow.setWindowIcon(QtGui.QIcon(
            scriptDir + '/resources/wifi.png'))
        self.centralwidget = QtWidgets.QWidget(connectWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ipLabel = QtWidgets.QLabel(self.centralwidget)
        self.ipLabel.setGeometry(QtCore.QRect(10, 50, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        self.portLabel = QtWidgets.QLabel(self.centralwidget)
        self.portLabel.setGeometry(QtCore.QRect(10, 80, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.portLabel.setFont(font)
        self.portLabel.setObjectName("portLabel")
        self.ipInput = QtWidgets.QLineEdit(self.centralwidget)
        self.ipInput.setGeometry(QtCore.QRect(50, 50, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ipInput.setFont(font)
        self.ipInput.setAcceptDrops(False)
        self.ipInput.setObjectName("ipInput")
        self.portInput = QtWidgets.QLineEdit(self.centralwidget)
        self.portInput.setGeometry(QtCore.QRect(50, 80, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.portInput.setFont(font)
        self.portInput.setAcceptDrops(False)
        self.portInput.setObjectName("portInput")
        self.idLabel = QtWidgets.QLabel(self.centralwidget)
        self.idLabel.setGeometry(QtCore.QRect(10, 10, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.idLabel.setFont(font)
        self.idLabel.setStatusTip("")
        self.idLabel.setObjectName("idLabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 10, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setStatusTip("")
        self.label.setWhatsThis("")
        self.label.setText(searchFile(1))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.connectButton = QtWidgets.QPushButton(self.centralwidget)
        self.connectButton.setGeometry(QtCore.QRect(140, 110, 121, 21))
        self.connectButton.setObjectName("connectButton")
        self.connectButton.clicked.connect(self.save)
        self.connectButton.clicked.connect(connectWindow.close)
        self.saveLabel = QtWidgets.QLabel(self.centralwidget)
        self.saveLabel.setGeometry(QtCore.QRect(10, 110, 121, 21))
        self.saveLabel.setObjectName("saveLabel")
        connectWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(connectWindow)
        QtCore.QMetaObject.connectSlotsByName(connectWindow)

    def retranslateUi(self, connectWindow):
        _translate = QtCore.QCoreApplication.translate
        connectWindow.setWindowTitle(_translate(
            "connectWindow", "Connect to server"))
        connectWindow.setStatusTip(_translate(
            "connectWindow", "Connect to server."))
        self.ipLabel.setText(_translate("connectWindow", "IPv4:"))
        self.portLabel.setText(_translate("connectWindow", "Port:"))
        self.idLabel.setText(_translate("connectWindow", "Your ID:"))
        self.connectButton.setText(_translate(
            "connectWindow", "Create Connection"))
        self.saveLabel.setText(_translate(
            "connectWindow", "<html><head/><body><p><span style=\" font-style:italic;\">Details saved in settings.</span></p></body></html>"))

    def save(self, connectWindow):
        import ipaddress
        import sys
        from setup import writeFile
        error = False
        portInt = False
        ipFormat = False
        ip = self.ipInput.text()
        port = self.portInput.text()

        if ip == "" or port == "" and error == False:
            error = True
            noInputMsg = QMessageBox()
            noInputMsg.setWindowTitle("Error")
            noInputMsg.setText(
                "Fields can not be left blank.\nPlease enter the details and try again.")
            noInputMsg.setIcon(QMessageBox.Critical)
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            noInputMsg.setWindowIcon(QtGui.QIcon(
                scriptDir + '/resources/error.png'))
            x = noInputMsg.exec_()

        try:
            int(port)
            portInt = True
        except ValueError:
            portInt = False
        if portInt == False and error == False:
            error = True
            portMsg = QMessageBox()
            portMsg.setWindowTitle("Error")
            portMsg.setText(
                "The entered value for port is not a number.\nEnter a number and try again.")
            portMsg.setIcon(QMessageBox.Critical)
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            portMsg.setWindowIcon(QtGui.QIcon(
                scriptDir + '/resources/error.png'))
            x = portMsg.exec_()

        try:
            ipaddress.ip_address(ip)
            ipFormat = True
        except ValueError:
            ipFormat = False

        if ipFormat == False and error == False:
            error = True
            portMsg = QMessageBox()
            portMsg.setWindowTitle("Error")
            portMsg.setText(
                "IPv4 is not valid.\nEnsure it has correct formating and try again.")
            portMsg.setIcon(QMessageBox.Critical)
            scriptDir = os.path.dirname(os.path.realpath(__file__))
            portMsg.setWindowIcon(QtGui.QIcon(
                scriptDir + '/resources/error.png'))
            x = portMsg.exec_()

        if ipFormat == True and portInt == True and error == False:
            writeFile(ip, 2)
            writeFile(port, 3)
