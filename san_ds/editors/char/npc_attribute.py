#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.fixed_text import FixedText
from widgets.common.multiline_text import MultilineText
from widgets.common.grid_table import GridTable, GridDelegate
from widgets.common.normal_model import NormalModel

class NpcAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        npc_attribute_table = GridTable(self)
        npc_attribute_model = NormalModel(self, [
            (FixedText, 'NPCデータ_名前'),
            (MultilineText, '文本_キャラ伝記')
        ])
        npc_attribute_table.setModel(npc_attribute_model)
        npc_attribute_table.setItemDelegate(GridDelegate(self))

        npc_attribute_model.column_objects[1].data_type.set_start(0x302)

        npc_attribute_table.setColumnWidth(0, 64)
        npc_attribute_table.setColumnWidth(1, 280)

        layout = QGridLayout()
        layout.addWidget(npc_attribute_table)
        self.setLayout(layout)