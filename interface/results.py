from PyQt5 import QtCore, QtWidgets


class Ui_results_form(QtWidgets.QDialog):
    def __init__(self, root, label_name, information):
        super().__init__(root)
        self.main = root
        self._translate = QtCore.QCoreApplication.translate
        self.html_text = ""
        self.label_name = label_name
        self.information = information

    def setupUi(self, results_form):
        resize = 150
        results_form.setObjectName("test_results_form")
        results_form.resize(280 + resize, 192)
        results_form.setMinimumSize(QtCore.QSize(280 + resize, 192))
        results_form.setMaximumSize(QtCore.QSize(280 + resize, 192))
        results_form.setStyleSheet(self.main.CSS_style)
        self.results_label = QtWidgets.QLabel(results_form)
        self.results_label.setGeometry(QtCore.QRect(20, 10, 81, 16))
        self.results_label.setObjectName("results_label")
        self.results_box = QtWidgets.QTextBrowser(results_form)
        self.results_box.setGeometry(QtCore.QRect(20, 30, 241 + resize, 143))
        self.results_box.setFrameShadow(QtWidgets.QFrame.Raised)
        self.results_box.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.results_box.setObjectName("results_box")

        self.retranslateUi(results_form)
        QtCore.QMetaObject.connectSlotsByName(results_form)

    def retranslateUi(self, test_results_form):
        test_results_form.setWindowTitle(self._translate("results_form", "Results"))
        self.results_label.setText(self._translate("results_form", self.label_name))

    def fill_results_box(self):
        self.results_box.setText(self.information)