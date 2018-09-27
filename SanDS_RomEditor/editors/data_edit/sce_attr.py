#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *


class SceAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_attr_table = GridTable(self)
        scenario_attr_model = NormalModel(self, [
            (LineText, '劇本屬性_劇本標題'),
            (LineText, '劇本屬性_劇本名'),
            (ValueSpin, '劇本屬性_劇本年', None, 350),
            (ValueSpin, '劇本屬性_開始年', None, 350),
            (ValueSpin, '劇本屬性_開始月', None, 12),
            (ValueSpin, '劇本屬性_勢力數', None, 19),
            (ValueSpin, '劇本屬性_旗幟數', None, 21),
            (ValueSpin, '劇本屬性_玩家數', None, 8),
            (MappingCombo, '劇本屬性_獻帝位置', '都市屬性_都市名', True),
        ])
        scenario_attr_table.setModel(scenario_attr_model)
        scenario_attr_table.setItemDelegate(GridDelegate(self))
        scenario_attr_table.setColumnWidth(0, 200)
        scenario_attr_table.setColumnWidth(1, 160)
        [scenario_attr_table.setColumnWidth(i, 50) for i in range(2, 8)]
        scenario_attr_table.setColumnWidth(8, 70)

        layout = QGridLayout()
        layout.addWidget(scenario_attr_table, 0, 0, 1, 1)
        self.setLayout(layout)
