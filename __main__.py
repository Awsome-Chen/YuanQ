from PyQt5 import QtWidgets

import main_window
import address_box

import sys

def transfer_address(address):
        addressWindow.close()
        ui = main_window.Ui_MainWindow(address)
        ui.setupUi(baseW)
        baseW.show()

if __name__ == "__main__":
        app = QtWidgets.QApplication(sys.argv)
        baseW = QtWidgets.QWidget()
        addressWindow = QtWidgets.QDialog()

        address_ui = address_box.Ui_Dialog()
        address_ui.setupUi(addressWindow)
        addressWindow.show()
        address_ui.pushButton.clicked.connect(lambda : transfer_address(address_ui.lineEdit.text()))

        sys.exit(app.exec_())