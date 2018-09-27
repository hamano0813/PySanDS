#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *

king = {i: f'君主{i+1:02d}' for i in range(20)}
king.update({255: '—'})


class FieldAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        field_attr_table = GridTable(self)
        field_attr_model = NormalModel(self, [
            (LineText, '戰場屬性_戰場名'),
            (LineText, '戰場屬性_讀音'),
            (MappingCombo, '戰場屬性_劇本1', None, king),
            (MappingCombo, '戰場屬性_劇本2', None, king),
            (MappingCombo, '戰場屬性_劇本3', None, king),
            (MappingCombo, '戰場屬性_劇本4', None, king),
            (MappingCombo, '戰場屬性_劇本5', None, king),
            (MappingCombo, '戰場屬性_劇本6', None, king),
            (MappingCombo, '戰場屬性_劇本7', None, king)
        ])
        field_attr_table.setModel(field_attr_model)
        field_attr_table.setItemDelegate(GridDelegate(self))
        [field_attr_table.setColumnWidth(i, 60) for i in range(0, 2)]
        [field_attr_table.setColumnWidth(i, 70) for i in range(2, 9)]

        layout = QGridLayout()
        layout.addWidget(field_attr_table, 0, 0, 1, 1)
        self.setLayout(layout)
