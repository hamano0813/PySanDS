#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QComboBox
from PyQt5.QtCore import QObject, QSize
from PyQt5.QtGui import QIcon
from parsers import Character, Numerical, Picture
from configs import DATA_PARAMETER

buffer = bytearray(open(r'D:\Python\PySanDS\resource\4032.nds', 'rb').read())

a = QObject()
a.buffer = buffer
#
# data_edit = Character(a, **DATA_PARAMETER.get('武将属性_姓名'))
# number = Numerical(a, **DATA_PARAMETER.get('武将属性_武力'))
# for i in range(770):
#     print(data_edit.get_data(i),'\t', number.get_data(i))

pic = Picture(a, **DATA_PARAMETER.get('図_キャラアバター'))

app = QApplication(sys.argv)
combo = QComboBox()

for i in range(10):
    icon = QIcon(pic.get_data(i).toqpixmap())
    combo.addItem(icon, f'{i + 1:3d}.')

combo.setIconSize(QSize(*pic.get_data(0).size))
combo.show()
sys.exit(app.exec_())
