#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication
from editors.window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyleSheet('''*{font: 12pt '宋体';}''')
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
