# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EstablishWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EstablishWindow(object):
    def setupUi(self, EstablishWindow):
        EstablishWindow.setObjectName("EstablishWindow")
        EstablishWindow.resize(300, 150)
        self.information = QtWidgets.QLabel(EstablishWindow)
        self.information.setGeometry(QtCore.QRect(10, 10, 281, 51))
        self.information.setTextFormat(QtCore.Qt.AutoText)
        self.information.setScaledContents(False)
        self.information.setAlignment(QtCore.Qt.AlignCenter)
        self.information.setObjectName("information")
        self.connectButton = QtWidgets.QPushButton(EstablishWindow)
        self.connectButton.setGeometry(QtCore.QRect(170, 100, 91, 23))
        self.connectButton.setObjectName("connectButton")
        self.serverIP_input = QtWidgets.QLineEdit(EstablishWindow)
        self.serverIP_input.setGeometry(QtCore.QRect(40, 70, 221, 20))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.serverIP_input.sizePolicy().hasHeightForWidth())
        self.serverIP_input.setSizePolicy(sizePolicy)
        self.serverIP_input.setInputMethodHints(QtCore.Qt.ImhNone)
        self.serverIP_input.setAlignment(QtCore.Qt.AlignCenter)
        self.serverIP_input.setObjectName("serverIP_input")
        self.helpButton = QtWidgets.QPushButton(EstablishWindow)
        self.helpButton.setGeometry(QtCore.QRect(40, 100, 91, 23))
        self.helpButton.setObjectName("helpButton")

        self.retranslateUi(EstablishWindow)
        QtCore.QMetaObject.connectSlotsByName(EstablishWindow)

    def retranslateUi(self, EstablishWindow):
        _translate = QtCore.QCoreApplication.translate
        EstablishWindow.setWindowTitle(_translate(
            "EstablishWindow", "Establish Connection"))
        self.information.setText(_translate("EstablishWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Enter the server </span><span style=\" font-size:11pt; font-weight:600;\">IPv4</span><span style=\" font-size:11pt;\"> to establish</span></p><p align=\"center\"><span style=\" font-size:11pt;\">a connection with the server.</span></p></body></html>"))
        self.connectButton.setText(_translate("EstablishWindow", "Connect"))
        self.serverIP_input.setPlaceholderText(
            _translate("EstablishWindow", "0.0.0.0"))
        self.helpButton.setText(_translate("EstablishWindow", "Help"))


def start():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EstablishWindow = QtWidgets.QWidget()
    ui = Ui_EstablishWindow()
    ui.setupUi(EstablishWindow)
    EstablishWindow.show()
    sys.exit(app.exec_())
