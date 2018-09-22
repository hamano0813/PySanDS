#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *


class NpcAttr(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        npc_attribute_table = GridTable(self)
        npc_attribute_model = NormalModel(self, [
            (LineText, 'NPC屬性_姓名'),
            (MultilineText, '文本_人物列傳')
        ])
        npc_attribute_table.setModel(npc_attribute_model)
        npc_attribute_table.setItemDelegate(GridDelegate(self))

        npc_attribute_model.column_objects[1].data_type.set_start(0x302)

        npc_attribute_table.setColumnWidth(0, 70)
        npc_attribute_table.setColumnWidth(1, 260)

        layout = QGridLayout()
        layout.addWidget(npc_attribute_table)
        self.setLayout(layout)
