#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from parsers import Numerical
from widgets.abstract import SingleObject


class ValueSpin(QSpinBox, SingleObject):
    parser_type = Numerical

    def __init__(self, parent, data_name, mapping_name=None, attach=0):
        QSpinBox.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.max_value = attach
        self.data_type: Numerical = self.parser(self.parser_type, data_name)
        if self.data_type.bit is None:
            self.bit_value = 0x100 ** self.data_type.length.normal_length - 1
        else:
            self.bit_value = 0x2 ** (self.data_type.bit[1] - self.data_type.bit[0]) - 1
        if self.max_value:
            self.lineEdit().setValidator(QIntValidator(0, self.max_value + 1))
            self.setRange(0, self.max_value + 1)
        else:
            self.max_value = self.bit_value
            self.lineEdit().setValidator(QIntValidator(0, self.bit_value))
            self.setRange(0, self.bit_value)
        self.setAlignment(Qt.AlignRight)
        self.setWrapping(True)
        self.setToolTip(f'數值範圍{self.minimum()}-{self.max_value}')

    def refresh_data(self):
        self.setValue(self.data_type.get_data(self.data_index))

    def save_data(self):
        self.data_type.set_data(self.data_index, self.value())

    def get_value(self):
        if self.value() > self.max_value:
            return self.bit_value
        return self.value()

    def set_value(self, value: int):
        if value > self.max_value:
            self.setValue(self.max_value + 1)
        self.setValue(value)

    def textFromValue(self, value):
        if value > self.max_value:
            return 'ー'
        return str(value)

    def valueFromText(self, text):
        if text == 'ー':
            return self.max_value
        return int(text)
