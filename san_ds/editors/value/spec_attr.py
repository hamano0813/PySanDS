#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *
from attributes import Quantity

lifetime = {0: '—', 1: '+1', 256: '=5 ', }

unsigned = {0: '—'}
unsigned.update({i: f'{i:+d}' for i in range(1, 16)})
unsigned.update({256: '=15'})

signed = {0: '—'}
signed.update({65536 + i: f'{i:+d}' for i in range(-1, -16, -1)})
signed.update({65280: '=0'})

move = {0: '—', 1: '+1', 2: '+2'}

retreat = {0: '—', 1: '○'}


class SpecAttr(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        spec_attr_table = GridTable(self)
        spec_attr_model = NormalModel(self, [
            (LineText, '物品屬性_物品'),
            (ValueSpin, '物品屬性_忠誠上昇', None, 100),
            (ValueSpin, '物品屬性_效果1'),
            (ValueSpin, '物品屬性_效果2'),
            (LineText, '文本_效果描述'),
            (LineText, '特產屬性_種類'),
            (ValueSpin, '特產屬性_武力', None, 30),
            (ValueSpin, '特產屬性_智力', None, 30),
            (ValueSpin, '特產屬性_政治', None, 30),
            (ValueSpin, '特產屬性_魅力', None, 30),
            (ValueSpin, '特產屬性_陸指', None, 30),
            (ValueSpin, '特產屬性_水指', None, 30),
            (ValueSpin, '特產屬性_義理', None, 30),
            (MappingCombo, '特產屬性_壽命', None, lifetime),
            (MappingCombo, '特產屬性_野望', None, signed),
            (MappingCombo, '特產屬性_幸運', None, unsigned),
            (MappingCombo, '特產屬性_冷靜', None, unsigned),
            (MappingCombo, '特產屬性_勇猛', None, unsigned),
            (MappingCombo, '特產屬性_機動力', None, move),
            (MappingCombo, '特產屬性_安全撤退', None, retreat),
        ], Quantity(0x36))
        spec_attr_table.setModel(spec_attr_model)
        spec_attr_table.setItemDelegate(GridDelegate(self))

        [spec_attr_model.column_objects[i].data_type.set_start(0xD) for i in range(4)]
        [spec_attr_table.setColumnWidth(i, 50) for i in range(5, 19)]
        spec_attr_table.setColumnWidth(0, 100)
        spec_attr_table.setColumnWidth(1, 60)
        spec_attr_table.setColumnWidth(2, 50)
        spec_attr_table.setColumnWidth(3, 50)
        spec_attr_table.setColumnWidth(4, 180)
        spec_attr_table.setColumnWidth(19, 60)

        layout = QGridLayout()
        layout.addWidget(spec_attr_table)
        self.setLayout(layout)
