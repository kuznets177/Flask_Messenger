# pip install PyQt5
# pyuic5 messenger.ui
# pyuic5 messenger.ui -o clientui.py

from PyQt5 import QtWidgets
import clientui


class ExampleApp(QtWidgets.QmainWindow, clientui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = ExampleApp()
    window.show()
    app.exec_()