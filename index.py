import datetime
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QMessageBox

import main


class Index:
    def __init__(self):
        self.file_path = ''

        self.ui = uic.loadUi("ui.ui")
        self.ui.btn_open.clicked.connect(self.open_file)
        self.ui.btn_start.clicked.connect(self.start)
        self.ui.btn_stop.clicked.connect(self.stop)
        self.ui.btn_start.setEnabled(False)
        self.ui.btn_stop.setEnabled(False)

    def show(self):
        self.ui.show()

    def open_file(self):
        self.file_path = QFileDialog.getOpenFileName()[0]
        if self.file_path == '':
            self.ui.textBrowser.append('未选择文件')
        else:
            self.ui.textBrowser.append(f'已选择文件 {self.file_path}')
            self.ui.btn_start.setEnabled(True)

    def start(self):
        if self.file_path == '':
            QMessageBox.information(self.ui, "提示", "未选择文件")
            return

        self.runner = main.Checker()
        self.runner.open_account(self.file_path, self.__on_finish)
        self.ui.textBrowser.append('开始查询...')
        self.ui.btn_stop.setEnabled(True)

    def stop(self):
        self.runner.stop()
        self.ui.textBrowser.append('正在停止...')

    def __on_finish(self, text):
        self.ui.textBrowser.append(text)
        self.ui.btn_start.setEnabled(self.file_path != '')
        self.ui.btn_stop.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    index = Index()
    index.show()
    sys.exit(app.exec())
