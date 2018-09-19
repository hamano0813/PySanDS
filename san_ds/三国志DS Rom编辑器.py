#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from editors.window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''*{font: 9pt '微软雅黑'}''')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
