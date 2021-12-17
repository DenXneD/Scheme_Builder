from PyQt5 import QtCore, QtWidgets
from interface.find_input_errors import ErrorTest


class Ui_print_form(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

    def setupUi(self, print_form):
        self.print_form = print_form
        print_form.setObjectName("print_form")
        print_form.resize(150, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(print_form.sizePolicy().hasHeightForWidth())
        print_form.setSizePolicy(sizePolicy)
        print_form.setStyleSheet(self.main.CSS_style)
        self.print_box = QtWidgets.QLineEdit(print_form)
        self.print_box.setGeometry(QtCore.QRect(90, 10, 50, 20))
        self.print_box.setObjectName("print_box")
        self.add_print_btn = QtWidgets.QPushButton(print_form)
        self.add_print_btn.setGeometry(QtCore.QRect(10, 40, 130, 25))
        self.add_print_btn.setObjectName("add_print_btn")
        self.add_print_btn.clicked.connect(self.add_print_event)
        self.print_label = QtWidgets.QLabel(print_form)
        self.print_label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.print_label.setObjectName("print_label")

        self.retranslateUi(print_form)
        QtCore.QMetaObject.connectSlotsByName(print_form)

    def retranslateUi(self, print_form):
        _translate = QtCore.QCoreApplication.translate
        print_form.setWindowTitle(_translate("print_form", "Print settings"))
        self.add_print_btn.setText(_translate("print_form", "ADD Print"))
        self.print_label.setText(_translate("print_form", "Variable name"))

    def add_print_event(self):
        var = self.print_box.text()
        if ErrorTest(var).print_is_acceptable():
            operation_info = {"id": "Print", "var_name": self.print_box.text()}
            self.main.add_event(self.print_form, operation_info)
