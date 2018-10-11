#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *


class FieldAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        king_model = NormalModel(self, [(MappingCombo, '劇本勢力_君主', '武將屬性_姓名', True), ])
        kings = []
        for data_offset in [0x0, -0x222, -0x444, -0x666, -0x888, -0xAAA, 0x222]:
            king_model.column_objects[0].data_type.set_offset(data_offset)
            mapping = {i: king_model.column_objects[0].get_data(king_model.createIndex(i, 0))
                       for i in range(king_model.rowCount())
                       if king_model.column_objects[0].get_data(king_model.createIndex(i, 0)) != '—'}
            mapping.update({255: '—'})
            kings.append(mapping)

        field_attr_table = GridTable(self)
        field_attr_model = NormalModel(self, [
            (LineText, '戰場屬性_戰場名'),
            (LineText, '戰場屬性_讀音'),
            (MappingCombo, '戰場屬性_劇本1', None, kings[0]),
            (MappingCombo, '戰場屬性_劇本2', None, kings[1]),
            (MappingCombo, '戰場屬性_劇本3', None, kings[2]),
            (MappingCombo, '戰場屬性_劇本4', None, kings[3]),
            (MappingCombo, '戰場屬性_劇本5', None, kings[4]),
            (MappingCombo, '戰場屬性_劇本6', None, kings[5]),
            (MappingCombo, '戰場屬性_劇本7', None, kings[6])
        ])
        field_attr_table.setModel(field_attr_model)
        field_attr_table.setItemDelegate(GridDelegate(self))
        [field_attr_table.setColumnWidth(i, 60) for i in range(0, 2)]
        [field_attr_table.setColumnWidth(i, 105) for i in range(2, 9)]

        layout = QGridLayout()
        layout.setContentsMargins(3, 5, 3, 5)
        layout.addWidget(field_attr_table, 0, 0, 1, 1)
        self.setLayout(layout)
