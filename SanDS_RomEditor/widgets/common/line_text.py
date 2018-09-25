#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from parsers import Character
from widgets.abstract import SingleObject
from configs import CODE_ALIASES, EXPAND_CHARACTER, CHARACTER_PATH


class LineText(QLineEdit, SingleObject):
    parser_type = Character

    def __init__(self, parent, data_name, mapping_name=None, attach=None):
        QLineEdit.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type: Character = self.parser(self.parser_type, data_name)
        char_file = open(CHARACTER_PATH, 'r', encoding='UTF-8')
        regex_char = char_file.read() + EXPAND_CHARACTER
        char_file.close()
        self.setValidator(QRegExpValidator(QRegExp(f'[{regex_char}\\n\\r]+')))
        offset = self.data_type.record * self.parent().parent().currentIndex().row()
        self.set_tip(f'最大字節長度{self.data_type.length(self.data_type.buffer, offset)}')
        self.textEdited.connect(self.set_tip)

    def set_tip(self, tips: str = None):
        if tips.startswith('最大字節長度'):
            self.setToolTip(tips)
        else:
            max_len = self.data_type.length(self.data_type.buffer,
                                            self.data_type.record * self.parent().parent().currentIndex().row())
            current_len = len(self.displayText().encode(CODE_ALIASES))
            self.setToolTip(f'最大字節長度{max_len}\n當前字節長度{current_len}')

    def refresh_data(self):
        self.setText(self.data_type.get_data(self.data_index))

    def save_data(self):
        self.data_type.set_data(self.data_index, self.text())
        self.refresh_data()

    def get_value(self):
        return self.displayText()

    def set_value(self, text):
        self.setText(text)
