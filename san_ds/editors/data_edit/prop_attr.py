#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *
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
    65535: '—',
}


class PropAttr(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        prop_attr_table = GridTable(self)
        prop_attr_model = NormalModel(self, [
            (LineText, '物品屬性_物品'),
            (ValueSpin, '物品屬性_忠誠上昇', None, 100),
            (ValueSpin, '物品屬性_效果1'),
            (ValueSpin, '物品屬性_效果2'),
            (MappingCombo, '道具歸屬_劇本1', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本2', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本3', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本4', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本5', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本6', '武將屬性_姓名', npc),
            (MappingCombo, '道具歸屬_劇本7', '武將屬性_姓名', npc),
        ], Quantity(0xD))
        prop_attr_table.setModel(prop_attr_model)
        prop_attr_table.setItemDelegate(GridDelegate(self))

        prop_attr_table.setColumnWidth(0, 100)
        prop_attr_table.setColumnWidth(1, 60)
        prop_attr_table.setColumnWidth(2, 50)
        prop_attr_table.setColumnWidth(3, 50)
        [prop_attr_table.setColumnWidth(i, 110) for i in range(4, 11)]

        layout = QGridLayout()
        layout.addWidget(prop_attr_table)
        self.setLayout(layout)
