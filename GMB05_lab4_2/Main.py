#!/usr/bin/env python3
# coding=utf-8

import re
import sys
from collections import Counter

from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUi


class Main(QDialog):
    def __init__(self):
        super(Main, self).__init__()
        loadUi('uis/main.ui', self)

        self.setWindowTitle('GMB05-lab4_2')
        self.setWindowIcon(QtGui.QIcon('images/logo.png'))

        self.btn_solve.clicked.connect(self.solve)
        self.btn_clear.clicked.connect(self.clear)

    def solve(self):
        self.textEdit_words.clear()
        txt = self.textEdit_text.toPlainText()  # получаем наш текст
        cnt = Counter(x for x in re.findall(r'[a-zA-Zа-яА-ЯёЁ\']{2,}', txt))
        self.textEdit_words.setText(str(cnt.most_common(5)))

    def clear(self):
        self.textEdit_text.clear()
        self.textEdit_words.clear()


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
