#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QTextCursor
from parsers import Character
from widgets.abstract import SingleObject
from configs import EXPAND_CHARACTER


class MultilineText(QTextEdit, SingleObject):
    parser_type = Character

    def __init__(self, parent, data_name, mapping_name=None, attach=None):
        QTextEdit.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type: Character = self.parser(self.parser_type, data_name)
        char_file = open('./configs/character.txt', 'r', encoding='UTF-8')
        regex_char = char_file.read() + EXPAND_CHARACTER
        char_file.close()
        self.reg_exp = QRegExp(f'[{regex_char}\\n\\r]+')
        self.textChanged.connect(self.check_reg_exp)

    def check_reg_exp(self):
        temp = ''.join([i if not self.reg_exp.indexIn(i) else '' for i in self.toPlainText()])
        print(self.toPlainText())
        if not temp == self.toPlainText():
            self.setText(temp)
            self.moveCursor(QTextCursor.End, QTextCursor.MoveAnchor)

    def refresh_data(self):
        self.setText(self.data_type.get_data(self.data_index))

    def save_data(self):
        self.data_type.set_data(self.data_index, self.toPlainText())
        self.refresh_data()

    def get_value(self):
        return self.toPlainText()

    def set_value(self, text):
        self.setText(text)
