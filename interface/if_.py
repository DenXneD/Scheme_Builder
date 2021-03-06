from PyQt5 import QtCore, QtGui, QtWidgets

from interface.find_input_errors import ErrorTest


class Ui_if_form(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

    def setupUi(self, if_form):
        self.if_form = if_form
        if_form.setObjectName("if_form")
        if_form.resize(160, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(if_form.sizePolicy().hasHeightForWidth())
        if_form.setSizePolicy(sizePolicy)
        if_form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        if_form.setStyleSheet(self.main.CSS_style)
        self.left_if_box = QtWidgets.QLineEdit(if_form)
        self.left_if_box.setGeometry(QtCore.QRect(10, 10, 51, 21))
        self.left_if_box.setObjectName("left_if_box")
        self.right_if_box = QtWidgets.QLineEdit(if_form)
        self.right_if_box.setGeometry(QtCore.QRect(100, 10, 51, 21))
        self.right_if_box.setObjectName("right_if_box")
        self.add_if_btn = QtWidgets.QPushButton(if_form)
        self.add_if_btn.setGeometry(QtCore.QRect(10, 40, 141, 25))
        self.add_if_btn.setObjectName("add_if_btn")
        self.add_if_btn.clicked.connect(self.add_if_event)
        self.if_comboBox = QtWidgets.QComboBox(if_form)
        self.if_comboBox.setGeometry(QtCore.QRect(60, 10, 41, 21))
        self.if_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.if_comboBox.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.if_comboBox.setObjectName("if_comboBox")
        self.if_comboBox.addItem("")
        self.if_comboBox.addItem("")
        self.if_comboBox.addItem("")
        self.if_comboBox.addItem("")

        self.retranslateUi(if_form)
        QtCore.QMetaObject.connectSlotsByName(if_form)

    def retranslateUi(self, if_form):
        _translate = QtCore.QCoreApplication.translate
        if_form.setWindowTitle(_translate("if_form", "If settings"))
        self.add_if_btn.setText(_translate("if_form", "ADD If"))
        self.if_comboBox.setItemText(0, _translate("if_form", "=="))
        self.if_comboBox.setItemText(1, _translate("if_form", "<"))
        self.if_comboBox.setItemText(2, _translate("if_form", ">"))
        self.if_comboBox.setItemText(3, _translate("if_form", "!="))

    def add_if_event(self):
        var1 = self.left_if_box.text()
        var2 = self.right_if_box.text()
        if (ErrorTest(var1).variable_is_acceptable() or ErrorTest(var1).is_number()) and\
                (ErrorTest(var2).variable_is_acceptable() or ErrorTest(var2).is_number()):
            operation_info = {"id": "If",
                              "var_name": self.left_if_box.text(),
                              "sign": self.if_comboBox.currentText(),
                              "to_compare": self.right_if_box.text()}
            self.main.add_event(self.if_form, operation_info)
