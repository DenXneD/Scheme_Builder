from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class Window(QMainWindow):
    def __init__(self):
        self.i = 0
        super(Window, self).__init__()
        self.setWindowTitle("Scheme Builder")
        self.resize(200, 200)

        self.new_text = QtWidgets.QLabel(self);

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Button was pressed: " + str(self.i))
        self.main_text.move(50, 50)
        self.main_text.adjustSize()

        self.btn = QtWidgets.QPushButton(self)
        self.btn.move(50, 70)
        self.btn.clicked.connect(self.change_label)

    def change_label(self):
        self.i += 1
        self.main_text.setText("Button was pressed: " + str(self.i))


def application():
    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
