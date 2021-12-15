# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'assign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


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
        assign_form.setStyleSheet("QWidget {\n"
                                    "  background-color: #2a1a41;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton {\n"
                                    "  border-radius: 4px;\n"
                                    "  background-color: #8EDBCE;\n"
                                    "  font: \"Roboto Mono\";\n"
                                    "  font-size: 12px;\n"
                                    "  color: black;\n"
                                    "  transition: background-color 1000ms linear;\n"
                                    "}\n"
                                    "\n"
                                    "QPushButton:hover {\n"
                                    "  background-color: #CDF9EF;\n"
                                    "}\n"
                                    "\n"
                                    "QLabel {\n"
                                    "  color: #4bd1e8;\n"
                                    "}\n"
                                    "\n"
                                    "QLineEdit {\n"
                                    "  border-radius: 1px;\n"
                                    "  border: 1px solid white;\n"
                                    "  background-color: #4bd1e8\n"
                                    "}\n"
                                    "\n"
                                    "")
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
        operation_info = {"id": "Assign",
                          "var_name": self.left_assign_box.text(),
                          "to_assign": self.right_assign_box.text()}
        list_text = (operation_info["id"] + ": " +
                     operation_info["var_name"] + " = " +
                     operation_info["to_assign"])
        self.main.add_event(self.assign_form, operation_info, list_text)
