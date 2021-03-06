#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate
from parsers import Numerical, Character
from widgets.abstract import SingleObject


class MappingCombo(QComboBox, SingleObject):
    parser_type = Numerical

    def __init__(self, parent, data_name, mapping_name, attach=None):
        QComboBox.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type: Numerical = self.parser(self.parser_type, data_name)
        self.mapping_type: Character = self.parser(Character, mapping_name)
        self.addItems(self.mapping.values())
        self.setMaxVisibleItems(15)
        self.setItemDelegate(QStyledItemDelegate())

    @property
    def mapping(self):
        mapping = {}
        if self.mapping_type:
            mapping.update(self.mapping_type.mapping())
        if isinstance(self.attach, dict):
            mapping.update(self.attach)
        elif self.attach is True:
            mapping.update({0x100 ** self.data_type.length.normal_length - 1: '—'})
        return mapping

    def refresh_data(self):
        self.setCurrentText(self.mapping.get(self.data_type.get_data(self.data_index), '—'))

    def save_data(self):
        self.data_type.set_data(self.data_index, list(self.mapping.keys())[self.currentIndex()])

    def get_value(self):
        return list(self.mapping.keys())[self.currentIndex()]

    def set_value(self, value):
        self.setCurrentText(self.mapping.get(value, '—'))
