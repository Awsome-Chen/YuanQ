from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(526, 62)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 9, 331, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(440, 10, 75, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "地址："))
        self.pushButton.setText(_translate("Dialog", "确认"))

# if __name__ == "__main__":
#         app = QtWidgets.QApplication(sys.argv)
#         baseW = QtWidgets.QDialog()
#         ui = Ui_Dialog()
#         ui.setupUi(baseW)
#         baseW.show()
#         ui.pushButton.clicked.connect(lambda : print(ui.lineEdit.text()))
#         sys.exit(app.exec_())