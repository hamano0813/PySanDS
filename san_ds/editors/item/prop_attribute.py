#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
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
        attribute_table = GridTable(self, [
            (FixedText, '物品属性_名称'),
            (ValueSpin, '物品属性_忠诚', None, 100),
            (ValueSpin, '道具属性_效果1'),
            (ValueSpin, '道具属性_效果2'),
            (MappingCombo, '道具归属_剧本1', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本2', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本3', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本4', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本5', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本6', '武将属性_姓名', npc),
            (MappingCombo, '道具归属_剧本7', '武将属性_姓名', npc),
        ], Quantity(0xD))
        layout = QGridLayout()
        layout.addWidget(attribute_table)
        self.setLayout(layout)
