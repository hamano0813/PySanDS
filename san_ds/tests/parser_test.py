#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject
from parsers import Character, Numerical, Picture
from configs import DATA_PARAMETER

buffer = bytearray(open(r'D:\Python\PySanDS\resource\4032.nds', 'rb').read())

a = QObject()
a.buffer = buffer

char = Character(a, **DATA_PARAMETER.get('武将属性_姓名'))
number = Numerical(a, **DATA_PARAMETER.get('武将属性_武力'))
for i in range(770):
    print(char.get_data(i),'\t', number.get_data(i))

pic = Picture(a, **DATA_PARAMETER.get('图片_武将头像'))
pic.get_data(0).show()
