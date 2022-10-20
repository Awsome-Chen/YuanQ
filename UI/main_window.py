from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from thread import *

from data import data

from UI import number_box
from UI import address_box

from os import rename


class Ui_MainWindow(object):
        def __init__(self,address):
                self.address = address

        def setupUi(self, MainWindow):
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(310, 75)
                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")
                self.label = QtWidgets.QLabel(self.centralwidget)
                self.label.setGeometry(QtCore.QRect(10, 10, 310, 61))
                font = QtGui.QFont()
                font.setPointSize(20)
                self.label.setFont(font)
                self.label.setObjectName("label")
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.retranslateUi(MainWindow)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

                self.numberWindow = QtWidgets.QDialog()
                self.number_ui = number_box.Ui_Dialog()
                self.number_ui.setupUi(self.numberWindow)

                self.number_ui.pushButton.clicked.connect(lambda : self.set_name(self.number_ui.lineEdit.text()))
                
                
                self.thread = listen_Thread(self.address)
                self.thread.Signal.connect(self.get_number)
                self.thread.start()

        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("YuanQ+", "YuanQ+"))
                self.label.setText(_translate("MainWindow", "YuanQ+运行中"))

        def get_number(self,file):
                self.file_name = file.split(".")[0]
                self.file_addr = file.split(".")[1]
                self.number_ui.lineEdit.clear()
                self.numberWindow.show()

        def set_name(self,number):
                try:
                        _file_name = data[number]
                except:
                        exit()
                absolute_address = self.address+"\\"+self.file_name+"."+self.file_addr
                _absolute_address = self.address+"\\"+_file_name+"."+self.file_addr
                # print("rename",absolute_address,"-->",_absolute_address)
                rename(absolute_address,_absolute_address)
                self.numberWindow.close()