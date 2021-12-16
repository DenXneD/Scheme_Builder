from interface import assign, if_, input, print, results, thread_name
from PyQt5 import QtCore, QtGui, QtWidgets
from server.application import SpringsModel


class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.threads = []
        self.CSS_style = ("QWidget {\n"
                          "  background-color: #2a1a41;\n"  # #2a1a41
                          "  font: \"Roboto Mono\";\n"
                          "  font-size: 11px;\n"
                          "}\n"
                          "QPushButton {\n"
                          "  border-radius: 4px;\n"
                          "  background-color: #8EDBCE;\n"
                          "  color: black;\n"
                          "}\n"
                          "QPushButton:hover {\n"
                          "  background-color: #CDF9EF;\n"
                          "}\n"
                          "QPushButton#del_thread_btn, QPushButton#del_block_btn {\n"
                          "  border-radius: 1px;\n"
                          "}\n"
                          "QPushButton#add_thread_btn, QPushButton#add_block_btn {\n"
                          "  border-radius: 1px;\n"
                          "}\n"
                          "QPushButton#del_thread_btn:hover, QPushButton#del_block_btn:hover {\n"
                          "  background-color: #F08583;\n"
                          "}\n"
                          "QPushButton#add_thread_btn:hover, QPushButton#add_block_btn:hover {\n"
                          "  background-color: #67F09D;\n"
                          "}\n"
                          "QLabel {\n"
                          "  color: #4bd1e8;\n"
                          "}\n"
                          "QLabel#logo {\n"
                          "  font: 13px;\n"
                          "}\n"
                          "QComboBox {\n"
                          "  border: 1px solid black;\n"
                          "  background-color: #4bd1e8\n"
                          "}\n"
                          "QComboBox QAbstractItemView{\n"
                          "  background-color: #4bd1e8\n"
                          "}\n"
                          "QListWidget {\n"
                          "  border: 1px solid black;\n"
                          "  border-radius: 4px;\n"
                          "  background-color: #4bd1e8\n"
                          "}\n"
                          "QLineEdit {\n"
                          "  border-radius: 1px;\n"
                          "  border: 1px solid #8EDBCE;\n"
                          "  background-color: #4bd1e8\n"
                          "}\n"
                          "QTextBrowser {\n"
                          "  border-radius: 4px;\n"
                          "  background-color: #4bd1e8;\n"
                          "}\n"
                          "")
        self.window_size = (380, 510)
        self.components_geometry = {"add_thread_btn": (349, 49, 23, 23),
                                    "del_thread_btn": (319, 49, 23, 23),
                                    "add_block_btn": (219, 49, 23, 23),
                                    "del_block_btn": (189, 49, 23, 23),
                                    "gen_code_btn": (120, 10, 121, 31),
                                    "test_threads_btn": (250, 10, 121, 31),
                                    "save_threads_btn": (250, 430, 121, 31),
                                    "load_threads_btn": (250, 470, 121, 31),
                                    "block_label": (10, 50, 51, 21),
                                    "thread_label": (250, 50, 61, 21),
                                    "logo": (10, 10, 111, 31),
                                    "thread_list": (250, 80, 121, 341),
                                    "blocks_list": (10, 80, 231, 421),
                                    "block_comboBox": (70, 50, 111, 22)}

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.NonModal)
        MainWindow.setEnabled(True)
        MainWindow.resize(*self.window_size)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(*self.window_size))
        MainWindow.setMaximumSize(QtCore.QSize(*self.window_size))
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        MainWindow.setWindowOpacity(1.0)
        MainWindow.setStyleSheet(self.CSS_style)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")
        self.add_thread_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_thread_btn.setGeometry(QtCore.QRect(*self.components_geometry["add_thread_btn"]))
        self.add_thread_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_thread_btn.setObjectName("add_thread_btn")
        self.add_thread_btn.clicked.connect(self.add_thread_event)
        self.del_thread_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_thread_btn.setGeometry(QtCore.QRect(*self.components_geometry["del_thread_btn"]))
        self.del_thread_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_thread_btn.setObjectName("del_thread_btn")
        self.del_thread_btn.clicked.connect(self.del_thread_event)
        self.add_block_btn = QtWidgets.QPushButton(self.centralwidget)
        self.add_block_btn.setGeometry(QtCore.QRect(*self.components_geometry["add_block_btn"]))
        self.add_block_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.add_block_btn.setObjectName("add_block_btn")
        self.add_block_btn.clicked.connect(self.add_block_event)
        self.del_block_btn = QtWidgets.QPushButton(self.centralwidget)
        self.del_block_btn.setGeometry(QtCore.QRect(*self.components_geometry["del_block_btn"]))
        self.del_block_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.del_block_btn.setObjectName("del_block_btn")
        self.del_block_btn.clicked.connect(self.del_block_event)
        self.gen_code_btn = QtWidgets.QPushButton(self.centralwidget)
        self.gen_code_btn.setGeometry(QtCore.QRect(*self.components_geometry["gen_code_btn"]))
        self.gen_code_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.gen_code_btn.setObjectName("gen_code_btn")
        self.gen_code_btn.clicked.connect(self.gen_code_event)
        self.test_threads_btn = QtWidgets.QPushButton(self.centralwidget)
        self.test_threads_btn.setGeometry(QtCore.QRect(*self.components_geometry["test_threads_btn"]))
        self.test_threads_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.test_threads_btn.setObjectName("test_threads_btn")
        self.test_threads_btn.clicked.connect(self.test_threads_event)
        self.save_threads_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_threads_btn.setGeometry(QtCore.QRect(*self.components_geometry["save_threads_btn"]))
        self.save_threads_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save_threads_btn.setObjectName("save_threads_btn")
        self.save_threads_btn.clicked.connect(self.save_threads_event)
        self.load_threads_btn = QtWidgets.QPushButton(self.centralwidget)
        self.load_threads_btn.setGeometry(QtCore.QRect(*self.components_geometry["load_threads_btn"]))
        self.load_threads_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.load_threads_btn.setObjectName("load_threads_btn")
        self.load_threads_btn.clicked.connect(self.load_threads_event)
        self.block_label = QtWidgets.QLabel(self.centralwidget)
        self.block_label.setEnabled(False)
        self.block_label.setGeometry(QtCore.QRect(*self.components_geometry["block_label"]))
        self.block_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.block_label.setStyleSheet("")
        self.block_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.block_label.setLineWidth(1)
        self.block_label.setAlignment(QtCore.Qt.AlignCenter)
        self.block_label.setObjectName("block_label")
        self.thread_label = QtWidgets.QLabel(self.centralwidget)
        self.thread_label.setEnabled(False)
        self.thread_label.setGeometry(QtCore.QRect(*self.components_geometry["thread_label"]))
        self.thread_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.thread_label.setStyleSheet("")
        self.thread_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.thread_label.setLineWidth(1)
        self.thread_label.setAlignment(QtCore.Qt.AlignCenter)
        self.thread_label.setObjectName("thread_label")
        self.logo = QtWidgets.QLabel(self.centralwidget)
        self.logo.setEnabled(False)
        self.logo.setGeometry(QtCore.QRect(*self.components_geometry["logo"]))
        self.logo.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.logo.setStyleSheet("")
        self.logo.setFrameShadow(QtWidgets.QFrame.Plain)
        self.logo.setLineWidth(1)
        # self.logo.setAlignment(QtCore.Qt.AlignCenter)
        self.logo.setObjectName("logo")
        self.thread_list = QtWidgets.QListWidget(self.centralwidget)
        self.thread_list.setGeometry(QtCore.QRect(*self.components_geometry["thread_list"]))
        self.thread_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.thread_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.thread_list.setObjectName("thread_list")
        self.thread_list.itemClicked.connect(self.update_blocks_list)
        self.blocks_list = QtWidgets.QListWidget(self.centralwidget)
        self.blocks_list.setGeometry(QtCore.QRect(*self.components_geometry["blocks_list"]))
        self.blocks_list.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.blocks_list.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.blocks_list.setObjectName("blocks_list")
        self.block_comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.block_comboBox.setGeometry(QtCore.QRect(*self.components_geometry["block_comboBox"]))
        self.block_comboBox.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.block_comboBox.setObjectName("block_comboBox")
        self.block_comboBox.addItem("")
        self.block_comboBox.addItem("")
        self.block_comboBox.addItem("")
        self.block_comboBox.addItem("")
        self.block_comboBox.addItem("")
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scheme Builder"))
        self.del_block_btn.setText(_translate("MainWindow", "-"))
        self.block_label.setText(_translate("MainWindow", "Thread"))
        self.gen_code_btn.setText(_translate("MainWindow", "GENERATE CODE"))
        self.logo.setText(_translate("MainWindow", "SCHEME BUILDER"))
        self.thread_label.setText(_translate("MainWindow", "THREADS"))
        self.save_threads_btn.setText(_translate("MainWindow", "SAVE THREADS"))
        self.test_threads_btn.setText(_translate("MainWindow", "TEST THREADS"))
        self.add_thread_btn.setText(_translate("MainWindow", "+"))
        __sortingEnabled = self.thread_list.isSortingEnabled()
        self.thread_list.setSortingEnabled(False)
        self.thread_list.setSortingEnabled(__sortingEnabled)
        self.add_block_btn.setText(_translate("MainWindow", "+"))
        self.block_comboBox.setItemText(0, _translate("MainWindow", "Assign"))
        self.block_comboBox.setItemText(1, _translate("MainWindow", "Print"))
        self.block_comboBox.setItemText(2, _translate("MainWindow", "Input"))
        self.block_comboBox.setItemText(3, _translate("MainWindow", "If"))
        self.block_comboBox.setItemText(4, _translate("MainWindow", "End if"))
        self.del_thread_btn.setText(_translate("MainWindow", "-"))
        __sortingEnabled = self.blocks_list.isSortingEnabled()
        self.blocks_list.setSortingEnabled(False)
        self.blocks_list.setSortingEnabled(__sortingEnabled)
        self.load_threads_btn.setText(_translate("MainWindow", "LOAD THREADS"))

    def add_thread_event(self):
        self.thread_name_form = QtWidgets.QWidget()
        self.thread_name_ui = thread_name.Ui_thread_name_form(self)
        self.thread_name_ui.setupUi(self.thread_name_form)
        self.thread_name_form.show()

    def del_thread_event(self):
        id_to_delete = self.get_current_thread_id()
        if id_to_delete != -1:
            self.threads.pop(id_to_delete)
            self.update_thread_list()
        if self.thread_list.count() != 0 and id_to_delete == self.thread_list.count():
            self.thread_list.setCurrentItem(self.thread_list.item(id_to_delete - 1))
            self.update_blocks_list()
        elif self.thread_list.count() != 0 and id_to_delete >= 0:
            self.thread_list.setCurrentItem(self.thread_list.item(id_to_delete))
            self.update_blocks_list()

    def add_block_event(self):
        if self.thread_list.count() != 0:
            if self.block_comboBox.currentIndex() == 0:
                self.assign_form = QtWidgets.QWidget()
                self.assign_ui = assign.Ui_assign_form(self)
                self.assign_ui.setupUi(self.assign_form)
                self.assign_form.show()

            elif self.block_comboBox.currentIndex() == 1:
                self.print_form = QtWidgets.QWidget()
                self.print_ui = print.Ui_print_form(self)
                self.print_ui.setupUi(self.print_form)
                self.print_form.show()
            elif self.block_comboBox.currentIndex() == 2:
                self.input_form = QtWidgets.QWidget()
                self.input_ui = input.Ui_input_form(self)
                self.input_ui.setupUi(self.input_form)
                self.input_form.show()
            elif self.block_comboBox.currentIndex() == 3:
                self.if_form = QtWidgets.QWidget()
                self.if_ui = if_.Ui_if_form(self)
                self.if_ui.setupUi(self.if_form)
                self.if_form.show()
            elif self.block_comboBox.currentIndex() == 4:
                index = self.get_current_thread_id()
                if index != -1:
                    operation_info = {"id": "End if"}
                    list_text = (operation_info["id"])
                    thread_index = self.get_current_thread_id()
                    block_index = self.get_current_block_id() + 1
                    if thread_index != -1:
                        self.threads[thread_index]["operations"].insert(block_index, operation_info)
                        item = QtWidgets.QListWidgetItem()
                        item.setText(list_text)
                        self.threads[thread_index]["operations_text"].insert(block_index, item.text())
                        self.update_blocks_list()
                        self.blocks_list.setCurrentItem(self.blocks_list.item(self.blocks_list.count() - 1))

    def del_block_event(self):
        id_to_delete = self.get_current_block_id()
        current_thread_id = self.get_current_thread_id()
        if id_to_delete != -1:
            self.threads[current_thread_id]["operations"].pop(id_to_delete)
            self.update_blocks_list()
        if self.blocks_list.count() != 0 and id_to_delete == self.blocks_list.count():
            self.blocks_list.setCurrentItem(self.blocks_list.item(id_to_delete - 1))
        elif self.blocks_list.count() != 0 and id_to_delete >= 0:
            self.blocks_list.setCurrentItem(self.blocks_list.item(id_to_delete))

    def gen_code_event(self):
        if self.thread_list.count() != 0:
            pass
        threads_for_server = self.reform_threads_list()
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Сохранить файл",
                                                             "threads.py",
                                                             "Python Files(*.py)")
        try:
            gen_code_string = SpringsModel.generate_springs_python_file(filename, threads_for_server)
            self.result_window("Generated Code", gen_code_string)
        except:
            self.result_window("Generated Code", "Code generation failed")

    # TODO merge Test Treads with server function
    def test_threads_event(self):
        # threads_for_server = self.reform_threads_list()
        # data = SpringsModel.test_springs(threads_for_server)

        data = "1. Thread1 - OK\n2. Thread - ERROR in block 3; If: e == 5; variable 'e' is not defined"
        self.result_window("Test result", data)

    def save_threads_event(self):
        file_for_save = self.reform_threads_list()
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Сохранить файл",
                                                             "threads.pickle",
                                                             "Pickle Files(*.pickle)")
        try:
            SpringsModel.save_springs_to_pickle_file(filename, file_for_save)
            self.result_window("Saving results", "Threads successfully saved")
        except:
            self.result_window("Saving results", "Threads saving failed")

    def load_threads_event(self):
        filename, ok = QtWidgets.QFileDialog.getSaveFileName(self,
                                                             "Загрузить файл",
                                                             "threads.pickle",
                                                             "Pickle Files(*.pickle)")
        try:
            self.threads = SpringsModel.load_springs_from_pickle_file(filename)
            self.result_window("Saving results", "Threads successfully loaded")
        except:
            self.result_window("Saving results", "Threads load failed")

        self.update_blocks_list()

    def get_current_thread_id(self):
        list_len = self.thread_list.count()
        for index in range(list_len):
            if self.thread_list.item(index) == self.thread_list.currentItem():
                return index
        return -1

    def get_current_block_id(self):
        list_len = self.blocks_list.count()
        for index in range(list_len):
            if self.blocks_list.item(index) == self.blocks_list.currentItem():
                return index
        return -1

    def update_thread_list(self):
        self.thread_list.clear()
        index = 0
        for thread in self.threads:
            item = QtWidgets.QListWidgetItem()
            item.setText(str(index + 1) + ". " + thread["thread_name"])
            index += 1
            self.thread_list.addItem(item)

        if self.thread_list.count() != 0:
            self.block_label.setText(self.threads[self.get_current_thread_id()]["thread_name"])
        else:
            self.block_label.setText("Thread")
        self.update_blocks_list()

    def update_blocks_list(self):
        index = self.get_current_thread_id()
        self.blocks_list.clear()
        if index != -1:
            for operation in self.threads[index]["operations"]:
                item = QtWidgets.QListWidgetItem()
                operation_name = self.make_operation_name(operation)
                item.setText(operation_name)
                self.blocks_list.addItem(item)

    @staticmethod
    def make_operation_name(operation):
        operation_text = ""
        if operation["id"] == "Input":
            operation_text = operation["id"] + ": " + operation["var_name"]
        elif operation["id"] == "Assign":
            operation_text = (operation["id"] + ": " +
                              operation["var_name"] + " = " +
                              operation["to_assign"])
        elif operation["id"] == "If":
            operation_text = (operation["id"] + ": " +
                              operation["var_name"] + " " +
                              operation["sign"] + " " +
                              operation["to_compare"])
        elif operation["id"] == "Print":
            operation_text = operation["id"] + ": " + operation["var_name"]
        return operation_text

    def add_event(self, form, operation_info):
        thread_index = self.get_current_thread_id()
        block_index = self.get_current_block_id() + 1
        if thread_index != -1:
            self.threads[thread_index]["operations"].insert(block_index, operation_info)
            item = QtWidgets.QListWidgetItem()
            operation_name = self.make_operation_name(operation_info)
            item.setText(operation_name)
            self.update_blocks_list()
            self.blocks_list.setCurrentItem(self.blocks_list.item(self.blocks_list.count() - 1))
        form.close()

    def reform_threads_list(self):
        result = []
        for index in range(len(self.threads)):
            result.append(
                {"id": index,
                 "thread_name": self.threads[index]["thread_name"],
                 "operations": self.threads[index]["operations"]})
        return result

    def result_window(self, label_name, information):
        self.results_form = QtWidgets.QWidget()
        self.results_ui = results.Ui_results_form(self, label_name, information)
        self.results_ui.setupUi(self.results_form)
        self.results_ui.fill_results_box()
        self.results_form.show()

    @staticmethod
    def save_file(filename, file):
        f = open(filename, "w")
        f.write(file)
        f.close()
