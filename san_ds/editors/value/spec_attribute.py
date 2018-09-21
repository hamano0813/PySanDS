#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *
from attributes import Quantity

lifetime = {0: 'ー', 1: '+1', 256: '=5 ', }

unsigned = {0: 'ー'}
unsigned.update({i: f'{i:+d}' for i in range(1, 16)})
unsigned.update({256: '=15'})

signed = {0: 'ー'}
signed.update({65536 + i: f'{i:+d}' for i in range(-1, -16, -1)})
signed.update({65280: '=0'})

move = {0: 'ー', 1: '+1', 2: '+2'}

retreat = {0: 'ー', 1: '√'}


class SpecAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        spec_attribute_table = GridTable(self)
        spec_attribute_model = NormalModel(self, [
            (FixedText, '物品屬性_物品'),
            (ValueSpin, '物品屬性_忠誠上昇', None, 100),
            (ValueSpin, '物品屬性_效果1'),
            (ValueSpin, '物品屬性_效果2'),
            (FixedText, '文本_道具效果'),
            (FixedText, '特產屬性_種類'),
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
        spec_attribute_table.setModel(spec_attribute_model)
        spec_attribute_table.setItemDelegate(GridDelegate(self))

        [spec_attribute_model.column_objects[i].data_type.set_start(0xD) for i in range(4)]
        [spec_attribute_table.setColumnWidth(i, 40) for i in range(5, 19)]
        spec_attribute_table.setColumnWidth(0, 90)
        spec_attribute_table.setColumnWidth(1, 60)
        spec_attribute_table.setColumnWidth(2, 50)
        spec_attribute_table.setColumnWidth(3, 50)
        spec_attribute_table.setColumnWidth(4, 150)
        spec_attribute_table.setColumnWidth(19, 56)

        layout = QGridLayout()
        layout.addWidget(spec_attribute_table)
        self.setLayout(layout)
