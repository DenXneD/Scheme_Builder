from PyQt5 import QtCore, QtWidgets


class Ui_input_form(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

    def setupUi(self, input_form):
        self.input_form = input_form
        input_form.setObjectName("input_form")
        input_form.resize(150, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(input_form.sizePolicy().hasHeightForWidth())
        input_form.setSizePolicy(sizePolicy)
        input_form.setStyleSheet(self.main.CSS_style)
        self.right_input_box = QtWidgets.QLineEdit(input_form)
        self.right_input_box.setGeometry(QtCore.QRect(90, 10, 50, 20))
        self.right_input_box.setObjectName("right_input_box")
        self.add_input_btn = QtWidgets.QPushButton(input_form)
        self.add_input_btn.setGeometry(QtCore.QRect(10, 40, 130, 25))
        self.add_input_btn.setObjectName("add_input_btn")
        self.add_input_btn.clicked.connect(self.add_input_event)
        self.input_label = QtWidgets.QLabel(input_form)
        self.input_label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.input_label.setObjectName("input_label")

        self.retranslateUi(input_form)
        QtCore.QMetaObject.connectSlotsByName(input_form)

    def retranslateUi(self, input_form):
        _translate = QtCore.QCoreApplication.translate
        input_form.setWindowTitle(_translate("input_form", "Input settings"))
        self.add_input_btn.setText(_translate("input_form", "ADD Input"))
        self.input_label.setText(_translate("input_form", "Variable name"))


    def add_input_event(self):
        self.operation_info = {"id": "Input",
                               "var_name": self.right_input_box.text()}
        self.main.add_event(self.input_form, self.operation_info)
