#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QListWidget
from parsers import Character
from widgets.abstract import ControlObject
from configs import DATA_PARAMETER


class ControlList(QListWidget, ControlObject):
    def __init__(self, parent, data_name):
        QListWidget.__init__(self, parent)
        self.addItems(Character(parent, **DATA_PARAMETER.get(data_name)).sequence())
        self.setCurrentRow(0)
        # noinspection PyUnresolvedReferences
        self.currentRowChanged[int].connect(self.control_index)

    def refresh_data(self):
        pass
