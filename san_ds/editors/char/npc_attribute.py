#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.multiline_text import MultilineText


class NpcAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        attribute_table = GridTable(self, [
            (FixedText, 'NPC属性_姓名'),
            (MultilineText, '文本_角色列传')
        ])
        attribute_table.model().column_objects[1].data_type.set_start(0x302)
        layout = QGridLayout()
        layout.addWidget(attribute_table)
        self.setLayout(layout)
