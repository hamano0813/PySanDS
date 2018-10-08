#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QComboBox, QStyledItemDelegate
from parsers import Character
from widgets.abstract import ControlObject
from configs import DATA_PARAMETER


class ControlCombo(QComboBox, ControlObject):
    def __init__(self, parent, data_name):
        QComboBox.__init__(self, parent)
        self.control_widgets = []
        self.control_targets = []
        self.addItems(Character(parent, **DATA_PARAMETER.get(data_name)).sequence())
        self.setCurrentIndex(0)
        # noinspection PyUnresolvedReferences
        self.currentIndexChanged[int].connect(self.control_index)
        self.setItemDelegate(QStyledItemDelegate())

    def refresh_data(self):
        pass
