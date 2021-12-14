import sys
from PyQt5 import QtWidgets
from interface import main_window

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = main_window.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.implement_secondary_windows()
    MainWindow.show()
    sys.exit(app.exec_())



