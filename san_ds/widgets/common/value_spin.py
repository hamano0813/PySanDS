#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from parsers import Numerical
from widgets.abstract import SingleObject


class ValueSpin(QSpinBox, SingleObject):
    parser_type = Numerical

    def __init__(self, parent, data_name, mapping_name=None, attach=None):
        QSpinBox.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type: Numerical = self.parser(self.parser_type, data_name)
        if self.data_type.bit is None:
            self.lineEdit().setValidator(QIntValidator(0, 0x100 ** self.data_type.length.normal_length - 1))
            self.setRange(0, 0x100 ** self.data_type.length.normal_length - 1)
            self.max_value = 0x100 ** self.data_type.length.normal_length - 1
        else:
            self.lineEdit().setValidator(QIntValidator(0, 0x2 ** (self.data_type.bit[1] - self.data_type.bit[0]) - 1))
            self.setRange(0, 0x2 ** (self.data_type.bit[1] - self.data_type.bit[0]) - 1)
            self.max_value = 0x2 ** (self.data_type.bit[1] - self.data_type.bit[0]) - 1
        self.setAlignment(Qt.AlignRight)

    def refresh_data(self):
        self.setValue(self.data_type.get_data(self.data_index))

    def save_data(self):
        self.data_type.set_data(self.data_index, self.value())

    def get_value(self):
        return self.value()

    def set_value(self, value: int):
        self.setValue(value)

    def set_max_value(self, value):
        self.max_value = value

    def textFromValue(self, value):
        if value > self.max_value:
            return '-'
        return str(value)

    def valueFromText(self, text):
        if text == '-':
            return self.max_value
        return int(text)
