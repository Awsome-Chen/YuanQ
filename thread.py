from PyQt5.QtCore import QThread, pyqtSignal
from os import listdir,rename

class listen_Thread(QThread):
    Signal = pyqtSignal(str)

    def __init__(self,address,parent=None):
        super(listen_Thread, self).__init__(parent)
        self.address = address
        self.files = listdir(self.address)

    def run(self):
        while True:
            self._files = listdir(self.address)
            if len(self._files) < len(self.files):
                    # print(self._files,self.files,"_files比files小,删除了文件")
                    self.files = self._files
            elif len(self._files) > len(self.files):
                    file = list(set(self._files).difference(set(self.files)))[0]
                    # print(self._files,self.files,"_files比files大,增加了文件")
                    self.files = self._files
                    self.Signal.emit(file)
            elif set(self._files) != set(self.files):
                    # print(self._files,self.files,"_files比files一样大但不相同,修改了文件")
                    self.files = self._files