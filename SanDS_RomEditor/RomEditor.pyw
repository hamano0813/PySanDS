#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import QFile
from editors.window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = QFile('configs/custom.css')
    file.open(QFile.ReadOnly)
    stylesheet = bytearray(file.readAll()).decode('UTF-8')
    app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
