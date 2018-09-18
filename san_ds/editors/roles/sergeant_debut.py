#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.control_combo import ControlCombo
from attributes import Quantity

person_identity = {0: '君主[流浪]', 1: '军师', 2: '将军', 3: '武将', 4: '文官', 5: '流浪跟随', 6: '在野', 7: '未登场',
                   128: '君主', 129: '军师[太守]', 130: '将军[太守]', 131: '武将[太守]', 132: '文官[太守]', 255: '死亡'}
debut_offsets = [0x0, -0xC04, -0x1808, -0x240C, -0x3010, -0x3C14, 0xC04]


class SergeantDebut(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_combo = ControlCombo(self, '剧本属性_剧本名')

        scenario_debut = GridTable(self, [
            (FixedText, '武将属性_姓名'),
            (ValueSpin, '武将登场_登场年'),
            (MappingCombo, '武将登场_血缘', '武将属性_姓名', True),
            (MappingCombo, '武将登场_身份', None, person_identity),
            (MappingCombo, '武将登场_都市', '都市属性_名称', True),
            (ValueSpin, '武将登场_忠诚', None, 100),
            (ValueSpin, '武将登场_士兵数', None, 200),
        ], Quantity(0x301))
        [scenario_combo.add_control_target(scenario_debut.model().column_objects[i].data_type.set_offset, debut_offsets)
         for i in range(3, 7)]

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(scenario_debut, 1, 0, 1, 1)
        self.setLayout(layout)
