#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.grid_table import GridTable, GridDelegate
from widgets.common.normal_model import NormalModel
from attributes import Quantity

npc = {
    838: '838.華陀',
    839: '839.司馬徽',
    840: '840.許子将',
    841: '841.干吉',
    842: '842.左慈',
    843: '843.管輅',
    844: '844.紫虚上人',
    845: '845.李意',
    846: '846.吉平',
    847: '847.献帝',
    65535: 'ーー',
}


class PropAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        prop_attribute_table = GridTable(self)
        prop_attribute_model = NormalModel(self, [
            (FixedText, 'アイテムデータ_アイテム'),
            (ValueSpin, 'アイテムデータ_忠誠上昇', None, 100),
            (ValueSpin, 'アイテムデータ_効果１'),
            (ValueSpin, 'アイテムデータ_効果２'),
            (MappingCombo, '基本アイテム_シナリオ１', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ２', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ３', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ４', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ５', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ６', '武将データ_名前', npc),
            (MappingCombo, '基本アイテム_シナリオ７', '武将データ_名前', npc),
        ], Quantity(0xD))
        prop_attribute_table.setModel(prop_attribute_model)
        prop_attribute_table.setItemDelegate(GridDelegate(self))

        prop_attribute_table.setColumnWidth(0, 96)
        prop_attribute_table.setColumnWidth(1, 64)
        prop_attribute_table.setColumnWidth(2, 50)
        prop_attribute_table.setColumnWidth(3, 50)
        [prop_attribute_table.setColumnWidth(i, 112) for i in range(4, 11)]

        layout = QGridLayout()
        layout.addWidget(prop_attribute_table)
        self.setLayout(layout)
