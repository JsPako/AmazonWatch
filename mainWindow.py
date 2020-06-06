# -*- coding: utf-8 -*-
# @Author: JsPako
# @Webpage: https://github.com/JsPako/AmazonWatch

import os
import webbrowser
import sys
import multiprocessing
import handler
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QSystemTrayIcon, QMenu
from aboutWindow import Ui_aboutWindow


class Ui_mainWindow(object):
    def openAbout(self):
        self.aboutWindow = QtWidgets.QMainWindow()
        self.aboutUI = Ui_aboutWindow()
        self.aboutUI.setupUi(self.aboutWindow)
        self.aboutWindow.show()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setWindowModality(QtCore.Qt.NonModal)
        mainWindow.resize(700, 500)
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
        mainWindow.setMinimumSize(QtCore.QSize(700, 500))
        mainWindow.setMaximumSize(QtCore.QSize(700, 500))
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
        self.removeButton.setGeometry(QtCore.QRect(580, 330, 101, 23))
        self.removeButton.setObjectName("removeButton")
        self.removeButton.clicked.connect(self.deleteList)
        self.refreshButton = QtWidgets.QPushButton(self.centralwidget)
        self.refreshButton.setGeometry(QtCore.QRect(580, 360, 101, 23))
        self.refreshButton.setObjectName("refreshButton")
        self.refreshButton.clicked.connect(handler.handler)
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
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(20, 10, 661, 301))
        self.tableWidget.setMaximumSize(QtCore.QSize(761, 16777215))
        self.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QtWidgets.QMenuBar(mainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuFile = QtWidgets.QMenu(self.menuBar)
        self.menuFile.setObjectName("menuFile")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        mainWindow.setMenuBar(self.menuBar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.actionDirectory = QtWidgets.QAction(mainWindow)
        self.actionDirectory.setShortcut("")
        self.actionDirectory.setIconVisibleInMenu(False)
        self.actionDirectory.setObjectName("actionDirectory")
        self.actionDirectory.triggered.connect(lambda: os.startfile(scriptDir))
        self.actionHelp = QtWidgets.QAction(mainWindow)
        self.actionHelp.setShortcut("")
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(mainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionAbout.triggered.connect(self.openAbout)
        self.actionPrefrences = QtWidgets.QAction(mainWindow)
        self.actionPrefrences.setObjectName("actionPrefrences")
        self.actionGithub = QtWidgets.QAction(mainWindow)
        self.actionGithub.setObjectName("actionGithub")
        self.actionGithub.triggered.connect(openBrowser)
        self.menuFile.addAction(self.actionGithub)
        self.menuFile.addAction(self.actionDirectory)
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menuBar.addAction(self.menuFile.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(mainWindow)
        self.updateList(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)
        mainWindow.setTabOrder(self.tableWidget, self.removeButton)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "AmazonWatch"))
        self.confirmButton.setStatusTip(_translate(
            "mainWindow", "Add this product to tracking list."))
        self.confirmButton.setText(_translate("mainWindow", "Add to list"))
        self.itemName.setStatusTip(_translate(
            "mainWindow", "Name of the product to help you keep organised."))
        self.itemName.setPlaceholderText(_translate(
            "mainWindow", "Amazon Echo Dot 3rd Gen"))
        self.itemURL.setStatusTip(_translate(
            "mainWindow", "Product amazon link. Sent to the API make sure it is correct."))
        self.itemURL.setPlaceholderText(_translate(
            "mainWindow", "https://www.amazon.co.uk/Echo-Dot-3rd-Gen-Charcoal/dp/B07PJV3JPR/"))
        self.itemNameLabel.setStatusTip(_translate(
            "mainWindow", "Name of the product to help you keep organised."))
        self.itemNameLabel.setText(_translate("mainWindow", "Product Name"))
        self.itemURLLabel.setStatusTip(_translate(
            "mainWindow", "Product amazon link. Sent to the API make sure it is correct."))
        self.itemURLLabel.setText(_translate("mainWindow", "Amazon URL"))
        self.removeButton.setStatusTip(_translate(
            "mainWindow", "Delete a product from the list."))
        self.removeButton.setText(_translate("mainWindow", "Delete"))
        self.refreshButton.setStatusTip(_translate(
            "mainWindow", "Refresh all prices."))
        self.refreshButton.setText(_translate("mainWindow", "Refresh"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("mainWindow", "Product Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("mainWindow", "URL"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("mainWindow", "Current Price"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("mainWindow", "Price Drop"))
        self.menuFile.setTitle(_translate("mainWindow", "Settings"))
        self.menuAbout.setTitle(_translate("mainWindow", "Help"))
        self.actionDirectory.setText(
            _translate("mainWindow", "File Directory"))
        self.actionDirectory.setStatusTip(
            _translate("mainWindow", "Open file directory."))
        self.actionHelp.setText(_translate("mainWindow", "Help"))
        self.actionHelp.setStatusTip(_translate("mainWindow", "Need help?"))
        self.actionAbout.setText(_translate("mainWindow", "About"))
        self.actionAbout.setStatusTip(
            _translate("mainWindow", "More information."))
        self.actionPrefrences.setText(_translate("mainWindow", "Prefrences"))
        self.actionGithub.setText(_translate(
            "mainWindow", "Github Repository"))
        self.actionGithub.setStatusTip(
            _translate("mainWindow", "Open Github."))

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
            f.write("'" + name + "," + url + "," + ",'" + "\n")
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


def apiTray():
    app = QtWidgets.QApplication(sys.argv)
    scriptDir = os.path.dirname(os.path.realpath(__file__))
    trayIcon = QSystemTrayIcon(QtGui.QIcon(scriptDir + "/resources/logo.png"))
    trayIcon.setToolTip("AmazonWatch")
    trayIcon.show()
    menu = QMenu()
    openAction = menu.addAction("Open GUI")
    openAction.triggered.connect(startGuiProcess)
    menu.addSeparator()
    actionGithub = menu.addAction("Visit Github")
    actionGithub.triggered.connect(openBrowser)
    menu.addSeparator()
    exitAction = menu.addAction("Exit")
    exitAction.triggered.connect(app.quit)
    trayIcon.setContextMenu(menu)
    sys.exit(app.exec_())


def startGui():
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())


def startGuiProcess():
    guiProcess = multiprocessing.Process(target=startGui)
    guiProcess.start()
    guiProcess.join()


def startApiProcess():
    apiProcess = multiprocessing.Process(target=apiTray)
    apiProcess.start()
    apiProcess.join()


def openBrowser():
    webbrowser.open("https://github.com/JsPako/AmazonWatch")


if __name__ == "__main__":
    startGuiProcess()
    startApiProcess()
