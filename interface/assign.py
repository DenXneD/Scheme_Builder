from PyQt5 import QtCore, QtWidgets

from interface.find_input_errors import ErrorTest


class Ui_assign_form(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

    def setupUi(self, assign_form):
        self.assign_form = assign_form
        assign_form.setObjectName("assign_form")
        assign_form.resize(150, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(assign_form.sizePolicy().hasHeightForWidth())
        assign_form.setSizePolicy(sizePolicy)
        assign_form.setStyleSheet(self.main.CSS_style)
        self.equals_assign_label = QtWidgets.QLabel(assign_form)
        self.equals_assign_label.setGeometry(QtCore.QRect(60, 10, 30, 20))
        self.equals_assign_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.equals_assign_label.setAlignment(QtCore.Qt.AlignCenter)
        self.equals_assign_label.setObjectName("equals_assign_label")
        self.add_assign_btn = QtWidgets.QPushButton(assign_form)
        self.add_assign_btn.setGeometry(QtCore.QRect(10, 40, 130, 25))
        self.add_assign_btn.setObjectName("add_assign_btn")
        self.add_assign_btn.clicked.connect(self.add_assign_event)
        self.right_assign_box = QtWidgets.QLineEdit(assign_form)
        self.right_assign_box.setGeometry(QtCore.QRect(90, 10, 50, 20))
        self.right_assign_box.setObjectName("right_assign_box")
        self.left_assign_box = QtWidgets.QLineEdit(assign_form)
        self.left_assign_box.setGeometry(QtCore.QRect(10, 10, 50, 20))
        self.left_assign_box.setObjectName("left_assign_box")

        self.retranslateUi(assign_form)
        QtCore.QMetaObject.connectSlotsByName(assign_form)

    def retranslateUi(self, assign_form):
        _translate = QtCore.QCoreApplication.translate
        assign_form.setWindowTitle(_translate("assign_form", "Assign settings"))
        self.equals_assign_label.setText(_translate("assign_form", "="))
        self.add_assign_btn.setText(_translate("assign_form", "ADD Assign"))

    def add_assign_event(self):
        var1 = self.left_assign_box.text()
        var2 = self.right_assign_box.text()
        if ErrorTest(var1).variable_is_acceptable() and\
                (ErrorTest(var2).variable_is_acceptable() or ErrorTest(var2).is_number()):
            operation_info = {"id": "Assign",
                              "var_name": var1,
                              "to_assign": var2}
            self.main.add_event(self.assign_form, operation_info)
