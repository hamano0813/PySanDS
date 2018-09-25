#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *

skill_offsets = [0x0, 0x00006C28, 0x0000D850, 0x00014478, 0x0001B0A0, 0x00021CC8, 0x000288F0]


class SkillAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_combo = ControlCombo(self, '劇本屬性_劇本名')

        skill_attr_table = GridTable(self)
        skill_attr_model = NormalModel(self, [
            (LineText, '武將屬性_姓名'),
            (ValueSpin, '武將戰技_戰鬥系'),
            (ValueSpin, '武將戰技_不意'),
            (ValueSpin, '武將戰技_突擊'),
            (ValueSpin, '武將戰技_牽制'),
            (ValueSpin, '武將戰技_一騎'),
            (ValueSpin, '武將戰技_受流'),
            (ValueSpin, '武將戰技_彈返'),
            (ValueSpin, '武將戰技_單騎'),
            (ValueSpin, '武將戰技_騎突'),
            (ValueSpin, '武將戰技_用兵系'),
            (ValueSpin, '武將戰技_壁越'),
            (ValueSpin, '武將戰技_威嚇'),
            (ValueSpin, '武將戰技_一齊'),
            (ValueSpin, '武將戰技_齊射'),
            (ValueSpin, '武將戰技_門射'),
            (ValueSpin, '武將戰技_火矢'),
            (ValueSpin, '武將戰技_狙擊'),
            (ValueSpin, '武將戰技_連弩'),
            (ValueSpin, '武將戰技_軍學系'),
            (ValueSpin, '武將戰技_鎮火'),
            (ValueSpin, '武將戰技_火計'),
            (ValueSpin, '武將戰技_伏兵'),
            (ValueSpin, '武將戰技_偽令'),
            (ValueSpin, '武將戰技_同討'),
            (ValueSpin, '武將戰技_論破'),
            (ValueSpin, '武將戰技_落穴'),
            (ValueSpin, '武將戰技_大火'),
            (ValueSpin, '武將戰技_掌握系'),
            (ValueSpin, '武將戰技_挑發'),
            (ValueSpin, '武將戰技_說得'),
            (ValueSpin, '武將戰技_治療'),
            (ValueSpin, '武將戰技_鼓舞'),
            (ValueSpin, '武將戰技_誘引'),
            (ValueSpin, '武將戰技_祈禱'),
            (ValueSpin, '武將戰技_衝車'),
            (ValueSpin, '武將戰技_生存'),
        ])
        skill_attr_table.setModel(skill_attr_model)
        skill_attr_table.setItemDelegate(GridDelegate(self))
        skill_attr_table.setColumnWidth(0, 60)
        [skill_attr_table.setColumnWidth(i, 45) for i in range(1, 37)]

        [scenario_combo.add_control_target(skill_attr_model.column_objects[i].data_type.set_offset, skill_offsets)
         for i in range(1, 37)]
        scenario_combo.add_control_widget(skill_attr_table)

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(skill_attr_table, 1, 0, 1, 1)
        self.setLayout(layout)
