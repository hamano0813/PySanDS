#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from attributes import Quantity

lifetime = {
    0: 'ー',
    1: '+1',
    256: '=5 ',
}

unsigned = {0: 'ー'}
unsigned.update({i : f'{i:+d}' for i in range(1, 16)})
unsigned.update({256: '=15'})

signed = {0: 'ー'}
signed.update({65536 + i: f'{i:+d}' for i in range(-1, -16, -1)})
signed.update({65280: '=0'})


class SpecAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        attribute_table = GridTable(self, [
            (FixedText, '物品属性_名称'),
            (ValueSpin, '物品属性_忠诚', None, 100),
            (ValueSpin, '特产效果_武力', None, 30),
            (ValueSpin, '特产效果_智力', None, 30),
            (ValueSpin, '特产效果_政治', None, 30),
            (ValueSpin, '特产效果_魅力', None, 30),
            (ValueSpin, '特产效果_陆指', None, 30),
            (ValueSpin, '特产效果_水指', None, 30),
            (ValueSpin, '特产效果_义理', None, 30),
            (MappingCombo, '特产效果_寿命', None, lifetime),
            (MappingCombo, '特产效果_野望', None, signed),
            (MappingCombo, '特产效果_幸运', None, unsigned),
            (MappingCombo, '特产效果_冷静', None, unsigned),
            (MappingCombo, '特产效果_勇猛', None, unsigned),

        ], Quantity(0x36))

        [attribute_table.model().column_objects[i].data_type.set_start(0xD) for i in range(2)]

        layout = QGridLayout()
        layout.addWidget(attribute_table)
        self.setLayout(layout)
