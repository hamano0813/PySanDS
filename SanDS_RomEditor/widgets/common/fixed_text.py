#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QRegExp, QFile, QIODevice
from PyQt5.QtGui import QRegExpValidator
from parsers import Character
from widgets.abstract import SingleObject
from configs import *


class FixedText(QLineEdit, SingleObject):
    parser_type = Character

    def __init__(self, parent, data_name, mapping_name=None, attach=None):
        QLineEdit.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_parser: Character = self.parser(self.parser_type, data_name)
        char_file = QFile(':/character.txt')
        char_file.open(QIODevice.ReadOnly | QIODevice.Text)
        regex_char = bytearray(char_file.readAll()).decode('UTF-8') + EXPAND_CHARACTER
        self.setValidator(QRegExpValidator(QRegExp(f'[{regex_char}\\n\\r]+')))

    def refresh_data(self):
        self.setText(self.data_parser.get_data(self.data_index))

    def save_data(self):
        self.data_parser.set_data(self.data_index, self.text())
        self.refresh_data()

    def get_value(self):
        return self.displayText()

    def set_value(self, text):
        self.setText(text)
