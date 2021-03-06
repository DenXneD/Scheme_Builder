from PyQt5 import QtCore, QtWidgets

from interface.find_input_errors import ErrorTest


class Ui_thread_name_form(QtWidgets.QDialog):
    def __init__(self, root, **kwargs):
        super().__init__(root, **kwargs)
        self.main = root

    def setupUi(self, thread_name_form):
        self.thread_name_form = thread_name_form
        thread_name_form.setObjectName("input_form")
        thread_name_form.resize(150, 75)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(thread_name_form.sizePolicy().hasHeightForWidth())
        thread_name_form.setSizePolicy(sizePolicy)
        thread_name_form.setStyleSheet(self.main.CSS_style)
        self.thread_name_box = QtWidgets.QLineEdit(thread_name_form)
        self.thread_name_box.setGeometry(QtCore.QRect(90, 10, 50, 20))
        self.thread_name_box.setObjectName("thread_name_box")
        self.add_thread_name_btn = QtWidgets.QPushButton(thread_name_form)
        self.add_thread_name_btn.setGeometry(QtCore.QRect(10, 40, 130, 25))
        self.add_thread_name_btn.setObjectName("add_thread_name_btn")
        self.add_thread_name_btn.clicked.connect(self.add_event)
        self.input_label = QtWidgets.QLabel(thread_name_form)
        self.input_label.setGeometry(QtCore.QRect(10, 10, 71, 21))
        self.input_label.setObjectName("thread_name_label")
        self.retranslateUi(thread_name_form)
        QtCore.QMetaObject.connectSlotsByName(thread_name_form)

    def retranslateUi(self, thread_name_form):
        _translate = QtCore.QCoreApplication.translate
        thread_name_form.setWindowTitle(_translate("thread_name_form", "Input settings"))
        self.add_thread_name_btn.setText(_translate("thread_name_form", "ADD Thread"))
        self.input_label.setText(_translate("thread_name_form", "Thread name"))

    def add_event(self):
        item = QtWidgets.QListWidgetItem()
        new_thread_name = self.thread_name_box.text()
        if ErrorTest(new_thread_name).variable_is_acceptable():
            item.setText(new_thread_name)
            self.main.threads.append({"thread_name": item.text(), "operations": []})
            self.main.update_thread_list()
            self.main.thread_list.setCurrentItem(self.main.thread_list.item(self.main.thread_list.count() - 1))
            self.thread_name_form.close()
