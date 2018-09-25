#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *


class FieldAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        field_attr_table = GridTable(self)
        field_attr_model = NormalModel(self, [
            (LineText, '戰場屬性_戰場名'),
            (LineText, '戰場屬性_讀音'),
        ])
        field_attr_table.setModel(field_attr_model)
        field_attr_table.setItemDelegate(GridDelegate(self))
        [field_attr_table.setColumnWidth(i, 60) for i in range(0, 2)]

        layout = QGridLayout()
        layout.addWidget(field_attr_table, 0, 0, 1, 1)
        self.setLayout(layout)
