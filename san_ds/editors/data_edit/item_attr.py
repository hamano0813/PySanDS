#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *


class ItemAttr(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        item_attr_table = GridTable(self)
        item_attr_model = NormalModel(self, [
            (LineText, '文本_物品名稱'),
            (LineText, '文本_物品讀音'),
            (LineText, '文本_物品類別'),
            (MultilineText, '文本_物品能力'),
            (MultilineText, '文本_物品描述'),
        ])
        item_attr_table.setModel(item_attr_model)
        item_attr_table.setItemDelegate(GridDelegate(self))

        item_attr_table.setColumnWidth(0, 100)
        item_attr_table.setColumnWidth(1, 120)
        item_attr_table.setColumnWidth(2, 70)
        item_attr_table.setColumnWidth(3, 150)
        item_attr_table.setColumnWidth(4, 260)

        layout = QGridLayout()
        layout.addWidget(item_attr_table)
        self.setLayout(layout)
