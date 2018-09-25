#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
from parsers import Numerical, Picture
from widgets.abstract import SingleObject


class PictureCombo(QComboBox, SingleObject):
    parser_type = Numerical

    def __init__(self, parent, data_name, mapping_name, attach=None):
        QComboBox.__init__(self, parent)
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type: Numerical = self.parser(self.parser_type, data_name)
        self.mapping_type: Picture = self.parser(Picture, mapping_name)
        [self.addItem(QIcon(pic.toqpixmap()), '') for code, pic in self.mapping.items()]
        self.setIconSize(QSize(*list(self.mapping.values())[0].size))
        self.setMaxVisibleItems(10)

    @property
    def mapping(self):
        mapping = {}
        if self.mapping_type:
            mapping.update(self.mapping_type.mapping())
        if isinstance(self.attach, dict):
            mapping.update(self.attach)
        return mapping

    def refresh_data(self):
        self.setCurrentIndex(list(self.mapping.keys()).index(self.data_type.get_data(self.data_index)))

    def save_data(self):
        self.data_type.set_data(self.data_index, list(self.mapping.keys())[self.currentIndex()])

    def get_value(self):
        return list(self.mapping.keys())[self.currentIndex()]

    def set_value(self, value):
        self.setCurrentIndex(list(self.mapping.keys()).index(value))
