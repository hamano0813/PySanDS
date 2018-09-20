#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
# from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.grid_table import GridTable, GridDelegate
from widgets.common.normal_model import NormalModel
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
            (FixedText, 'アイテムデータ_アイテム'),
            (ValueSpin, 'アイテムデータ_忠誠上昇', None, 100),
            (ValueSpin, 'アイテムデータ_効果１'),
            (ValueSpin, 'アイテムデータ_効果２'),
            (FixedText, '特産アイテム_効果文本'),
            (FixedText, '特産アイテム_種類'),
            (ValueSpin, '特産アイテム_武力', None, 30),
            (ValueSpin, '特産アイテム_知力', None, 30),
            (ValueSpin, '特産アイテム_政治', None, 30),
            (ValueSpin, '特産アイテム_魅力', None, 30),
            (ValueSpin, '特産アイテム_陸指', None, 30),
            (ValueSpin, '特産アイテム_水指', None, 30),
            (ValueSpin, '特産アイテム_義理', None, 30),
            (MappingCombo, '特産アイテム_寿命', None, lifetime),
            (MappingCombo, '特産アイテム_野望', None, signed),
            (MappingCombo, '特産アイテム_幸運', None, unsigned),
            (MappingCombo, '特産アイテム_冷静', None, unsigned),
            (MappingCombo, '特産アイテム_勇猛', None, unsigned),
            (MappingCombo, '特産アイテム_機動力', None, move),
            (MappingCombo, '特産アイテム_退却確実', None, retreat),
        ], Quantity(0x36))
        spec_attribute_table.setModel(spec_attribute_model)
        spec_attribute_table.setItemDelegate(GridDelegate(self))

        [spec_attribute_model.column_objects[i].data_type.set_start(0xD) for i in range(4)]
        [spec_attribute_table.setColumnWidth(i, 40) for i in range(5, 19)]
        spec_attribute_table.setColumnWidth(0, 96)
        spec_attribute_table.setColumnWidth(1, 64)
        spec_attribute_table.setColumnWidth(2, 50)
        spec_attribute_table.setColumnWidth(3, 50)
        spec_attribute_table.setColumnWidth(4, 160)
        spec_attribute_table.setColumnWidth(19, 64)

        layout = QGridLayout()
        layout.addWidget(spec_attribute_table)
        self.setLayout(layout)
