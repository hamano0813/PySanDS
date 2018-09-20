#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.control_combo import ControlCombo
from widgets.common.grid_table import GridTable, GridDelegate
from widgets.common.normal_model import NormalModel

from attributes import Quantity

person_identity = {0: '君主[放浪]', 1: '軍師', 2: '将軍', 3: '武将', 4: '文官', 5: '放浪', 6: '在野', 7: '未登場',
                   128: '君主', 129: '軍師[太守]', 130: '将軍[太守]', 131: '武将[太守]', 132: '文官[太守]', 255: '死亡'}
debut_offsets = [0x0, -0xC04, -0x1808, -0x240C, -0x3010, -0x3C14, 0xC04]


class CharDebut(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_combo = ControlCombo(self, 'シナリオデータ_シナリオ名')

        scenario_debut_table = GridTable(self)
        scenario_debut_model = NormalModel(self, [
            (FixedText, '武将データ_名前'),
            (ValueSpin, '武将登場_登場年'),
            (MappingCombo, '武将登場_血縁', '武将データ_名前', True),
            (MappingCombo, '武将登場_身份', None, person_identity),
            (MappingCombo, '武将登場_所在都市', '都市データ_都市名', True),
            (ValueSpin, '武将登場_忠誠', None, 100),
            (ValueSpin, '武将登場_兵数', None, 200),
        ], Quantity(0x301))
        scenario_debut_table.setModel(scenario_debut_model)
        scenario_debut_table.setItemDelegate(GridDelegate(self))

        [scenario_combo.add_control_target(scenario_debut_model.column_objects[i].data_type.set_offset, debut_offsets)
         for i in range(3, 7)]

        [scenario_debut_table.setColumnWidth(i, width) for i, width in enumerate([64, 50, 112, 84, 80, 40, 40])]

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(scenario_debut_table, 1, 0, 1, 1)
        self.setLayout(layout)
