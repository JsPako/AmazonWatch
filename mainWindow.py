# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!

import os
import webbrowser
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from connectWindow import Ui_connectWindow
from aboutWindow import Ui_aboutWindow
from setup import searchFile, deleteFile


class Ui_mainWindow(object):
    def openConnectWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_connectWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def openAboutWindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_aboutWindow()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(800, 500)
        scriptDir = os.path.dirname(os.path.realpath(__file__))
        mainWindow.setWindowIcon(QtGui.QIcon(
            scriptDir + '/resources/logo.png'))
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setMinimumSize(QtCore.QSize(800, 500))
        mainWindow.setMaximumSize(QtCore.QSize(800, 500))
        mainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.confirmButton = QtWidgets.QPushButton(self.centralwidget)
        self.confirmButton.setGeometry(QtCore.QRect(360, 420, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confirmButton.setFont(font)
        self.confirmButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.confirmButton.setObjectName("confirmButton")
        self.confirmButton.clicked.connect(self.addList)
        self.itemName = QtWidgets.QLineEdit(self.centralwidget)
        self.itemName.setGeometry(QtCore.QRect(130, 340, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.itemName.setFont(font)
        self.itemName.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.itemName.setAcceptDrops(False)
        self.itemName.setObjectName("itemName")
        self.itemURL = QtWidgets.QLineEdit(self.centralwidget)
        self.itemURL.setGeometry(QtCore.QRect(130, 380, 361, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.itemURL.setFont(font)
        self.itemURL.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.itemURL.setAcceptDrops(False)
        self.itemURL.setObjectName("itemURL")
        self.validateButton = QtWidgets.QPushButton(self.centralwidget)
        self.validateButton.setGeometry(QtCore.QRect(200, 420, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.validateButton.setFont(font)
        self.validateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.validateButton.setObjectName("validateButton")
        self.itemNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemNameLabel.setGeometry(QtCore.QRect(20, 340, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.itemNameLabel.setFont(font)
        self.itemNameLabel.setScaledContents(False)
        self.itemNameLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemNameLabel.setObjectName("itemNameLabel")
        self.itemURLLabel = QtWidgets.QLabel(self.centralwidget)
        self.itemURLLabel.setGeometry(QtCore.QRect(20, 380, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.itemURLLabel.setFont(font)
        self.itemURLLabel.setScaledContents(False)
        self.itemURLLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.itemURLLabel.setObjectName("itemURLLabel")
        self.removeButton = QtWidgets.QPushButton(self.centralwidget)
        self.removeButton.setGeometry(QtCore.QRect(680, 320, 101, 23))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.clicked.connect(self.deleteList)
        self.serverFrame = QtWidgets.QFrame(self.centralwidget)
        self.serverFrame.setGeometry(QtCore.QRect(530, 360, 241, 91))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,
                         QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0, 128))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,
                         QtGui.QPalette.PlaceholderText, brush)
        self.serverFrame.setPalette(palette)
        self.serverFrame.setAutoFillBackground(True)
        self.serverFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.serverFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.serverFrame.setObjectName("serverFrame")
        self.statusLabel = QtWidgets.QLabel(self.serverFrame)
        self.statusLabel.setGeometry(QtCore.QRect(10, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.statusLabel.setFont(font)
        self.statusLabel.setObjectName("statusLabel")
        self.currentStatus = QtWidgets.QLabel(self.serverFrame)
        self.currentStatus.setGeometry(QtCore.QRect(120, 0, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.currentStatus.setFont(font)
        if searchFile(2) == "":
            self.currentStatus.setText("Disconnected")
        else:
            self.currentStatus.setText("Connected")
        self.currentStatus.setObjectName("currentStatus")
        self.ipLabel = QtWidgets.QLabel(self.serverFrame)
        self.ipLabel.setGeometry(QtCore.QRect(10, 30, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ipLabel.setFont(font)
        self.ipLabel.setObjectName("ipLabel")
        self.currentIP = QtWidgets.QLabel(self.serverFrame)
        self.currentIP.setGeometry(QtCore.QRect(70, 30, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.currentIP.setFont(font)
        self.currentIP.setText(searchFile(2))
        self.currentIP.setObjectName("currentIP")
        self.updateButton = QtWidgets.QPushButton(self.serverFrame)
        self.updateButton.setGeometry(QtCore.QRect(160, 60, 71, 23))
        self.updateButton.clicked.connect(self.updateLabel)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.updateButton.setFont(font)
        self.updateButton.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.updateButton.setObjectName("updateButton")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 761, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(761, 16777215))
        self.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menuBar)
        self.menuHelp.setObjectName("menuHelp")
        mainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtWidgets.QAction(mainWindow)
        self.actionConnect.setIconVisibleInMenu(False)
        self.actionConnect.setObjectName("actionConnect")
        self.actionDisconnect = QtWidgets.QAction(mainWindow)
        self.actionDisconnect.setIconVisibleInMenu(False)
        self.actionDisconnect.setObjectName("actionDisconnect")
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionConnect)
        self.menuFile.addAction(self.actionDisconnect)
        self.menuHelp.addAction(self.actionHelp)
        self.menuHelp.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        self.updateList(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AmazonWatch"))
        self.confirmButton.setStatusTip(_translate(
            "mainWindow", "Add this product to tracking list."))
        self.confirmButton.setText(_translate("mainWindow", "Confirm"))
        self.itemName.setStatusTip(_translate(
            "mainWindow", "Name of the product to help you keep organised. Does not get sent to server."))
        self.itemName.setPlaceholderText(_translate(
            "mainWindow", "Amazon Echo Dot 3rd Gen"))
        self.itemURL.setStatusTip(_translate(
            "mainWindow", "Amazon Link to the item. Gets sent to server."))
        self.itemURL.setPlaceholderText(_translate(
            "mainWindow", "https://www.amazon.co.uk/Echo-Dot-3rd-Gen-Charcoal/dp/B07PJV3JPR/"))
        self.validateButton.setStatusTip(_translate(
            "mainWindow", "Check if the URL entered is valid."))
        self.validateButton.setText(_translate("mainWindow", "Validate URL"))
        self.itemNameLabel.setStatusTip(_translate(
            "mainWindow", "Name of the product to help you keep organised. Does not get sent to server."))
        self.itemNameLabel.setText(_translate("mainWindow", "Product Name"))
        self.itemURLLabel.setStatusTip(_translate(
            "mainWindow", "Amazon Link to the item. Gets sent to server."))
        self.itemURLLabel.setText(_translate("mainWindow", "Amazon URL"))
        self.removeButton.setStatusTip(_translate(
            "mainWindow", "Delete a product from the list."))
        self.removeButton.setText(_translate("mainWindow", "Delete"))
        self.serverFrame.setStatusTip(
            _translate("mainWindow", "Server Status"))
        self.statusLabel.setText(_translate(
            "mainWindow", "Connection Status:"))
        self.ipLabel.setText(_translate("mainWindow", "Server IP:"))
        self.updateButton.setStatusTip(_translate(
            "mainWindow", "Add this product to tracking list."))
        self.updateButton.setText(_translate("mainWindow", "Update"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "URL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Current Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Price Drop"))
        self.menuFile.setTitle(_translate("mainWindow", "Connect"))
        self.menuHelp.setTitle(_translate("mainWindow", "Help"))
        self.actionConnect.setText(_translate(
            "mainWindow", "Connect to Server"))
        self.actionConnect.setStatusTip(_translate(
            "mainWindow", "New connection to server."))
        self.actionConnect.setShortcut(_translate("mainWindow", "Ctrl+N"))
        self.actionConnect.triggered.connect(self.openConnectWindow)
        self.actionDisconnect.setText(_translate("mainWindow", "Disconnect"))
        self.actionDisconnect.setStatusTip(
            _translate("mainWindow", "Disconnect from server."))
        self.actionDisconnect.triggered.connect(self.deleteData)
        self.actionDisconnect.setShortcut(_translate("mainWindow", "Ctrl+X"))
        self.actionHelp.setText(_translate("mainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("mainWindow", "Need help?"))
        self.actionHelp.setShortcut(_translate("mainWindow", "Ctrl+H"))
        self.actionHelp.triggered.connect(lambda: webbrowser.open(
            'https://github.com/JsPako/AmazonWatch'))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionAbout.triggered.connect(self.openAboutWindow)
        self.actionAbout.setStatusTip(
            _translate("mainWindow", "More information."))

    def updateLabel(self, mainWindow):
        currentIP = searchFile(2)
        if currentIP != "":
            self.currentStatus.setText("Connected")
            self.currentIP.setText(currentIP)
        else:
            self.currentStatus.setText("Disconnected")
            self.currentIP.setText(currentIP)

    def deleteData(self, mainWindow):
        deleteFile(2)
        deleteFile(3)
        Ui_mainWindow.updateLabel(self, mainWindow)

    def addList(self, mainWindow):
        error = False
        name = self.itemName.text()
        url = self.itemURL.text()
        if name == "" or url == "" and error == False:
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
        with open("list.txt", "r") as f:
            for line in f:
                if url in line and error == False:
                    error = True
                    noInputMsg = QMessageBox()
                    noInputMsg.setWindowTitle("Error")
                    noInputMsg.setText(
                        "The URL you have entered is already in the database.\nYou cannot use the same URL twice.")
                    noInputMsg.setIcon(QMessageBox.Critical)
                    scriptDir = os.path.dirname(os.path.realpath(__file__))
                    noInputMsg.setWindowIcon(QtGui.QIcon(
                        scriptDir + '/resources/error.png'))
                    x = noInputMsg.exec_()
        if error == False:
            rowPosition = self.tableWidget.rowCount()
            self.tableWidget.insertRow(rowPosition)
            self.tableWidget.setItem(
                rowPosition, 0, QtWidgets.QTableWidgetItem(name))
            self.tableWidget.setItem(
                rowPosition, 1, QtWidgets.QTableWidgetItem(url))
            f = open("list.txt", "a+")
            f.write("'" + name + "," + url + "," + ",'\n")
            f.close()
            self.itemName.setText("")
            self.itemURL.setText("")

    def deleteList(self, mainWindow):
        selected = self.tableWidget.currentRow()
        self.tableWidget.removeRow(selected)
        lineList = []
        with open("list.txt", "r") as f:
            data = f.readlines()
            f.close()
            with open("list.txt", "w") as f:
                for line in data:
                    if line != data[selected]:
                        lineList.append(line)
                f.writelines(lineList)
                f.close()

    def updateList(self, mainWindow):
        with open("list.txt", "r") as f:
            file = f.readlines()
            for line in file:
                lines = line.split("'")
                data = lines[1].split(",")
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(
                    rowPosition, 0, QtWidgets.QTableWidgetItem(data[0]))
                self.tableWidget.setItem(
                    rowPosition, 1, QtWidgets.QTableWidgetItem(data[1]))
                self.tableWidget.setItem(
                    rowPosition, 2, QtWidgets.QTableWidgetItem(data[2]))
                self.tableWidget.setItem(
                    rowPosition, 3, QtWidgets.QTableWidgetItem(data[3]))
            f.close()


def startUi():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
