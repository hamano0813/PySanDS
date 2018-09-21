#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *
from parsers import Picture
from attributes import Quantity
from configs import DATA_PARAMETER

emblem_offsets = [0x0, 0x22, 0x44, 0x66, 0x88, 0xAA, 0xCC]
data_offsets = [0x0, -0x222, -0x444, -0x666, -0x888, -0xAAA, 0x222]


class ScenarioData(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        picture = Picture(self, **DATA_PARAMETER.get('図_紋章1')).get_data(0)
        emblem_dict = {i + 1: picture.crop((10 + 10 * i, 0 ,20 + 10 * i, 10)) for i in range(21)}

        scenario_combo = ControlCombo(self, 'シナリオデータ_シナリオ名')

        scenario_data_table = GridTable(self)
        scenario_data_model = NormalModel(self, [
            (PictureCombo, 'シナリオデータ_紋章', None, emblem_dict),
            (MappingCombo, 'シナリオデータ_君主', '武将データ_名前', True),
            (MappingCombo, 'シナリオデータ_首都', '都市データ_都市名', True),
            (ValueSpin, 'シナリオデータ_敵対01', None, 100),
            (ValueSpin, 'シナリオデータ_敵対02', None, 100),
            (ValueSpin, 'シナリオデータ_敵対03', None, 100),
            (ValueSpin, 'シナリオデータ_敵対04', None, 100),
            (ValueSpin, 'シナリオデータ_敵対05', None, 100),
            (ValueSpin, 'シナリオデータ_敵対06', None, 100),
            (ValueSpin, 'シナリオデータ_敵対07', None, 100),
            (ValueSpin, 'シナリオデータ_敵対08', None, 100),
            (ValueSpin, 'シナリオデータ_敵対09', None, 100),
            (ValueSpin, 'シナリオデータ_敵対10', None, 100),
            (ValueSpin, 'シナリオデータ_敵対11', None, 100),
            (ValueSpin, 'シナリオデータ_敵対12', None, 100),
            (ValueSpin, 'シナリオデータ_敵対13', None, 100),
            (ValueSpin, 'シナリオデータ_敵対14', None, 100),
            (ValueSpin, 'シナリオデータ_敵対15', None, 100),
            (ValueSpin, 'シナリオデータ_敵対16', None, 100),
            (ValueSpin, 'シナリオデータ_敵対17', None, 100),
            (ValueSpin, 'シナリオデータ_敵対18', None, 100),
            (ValueSpin, 'シナリオデータ_敵対19', None, 100),
            (ValueSpin, 'シナリオデータ_敵対20', None, 100),
            (ValueSpin, 'シナリオデータ_敵対21', None, 100),
        ], Quantity(0x15))
        scenario_data_table.setModel(scenario_data_model)
        scenario_data_table.setItemDelegate(GridDelegate(self))

        scenario_combo.add_control_target(scenario_data_model.column_objects[0].data_type.set_offset, emblem_offsets)
        [scenario_combo.add_control_target(scenario_data_model.column_objects[i].data_type.set_offset, data_offsets)
         for i in range(1, 24)]
        scenario_data_table.setColumnWidth(0, 60)
        scenario_data_table.setColumnWidth(1, 100)
        scenario_data_table.setColumnWidth(2, 72)
        [scenario_data_table.setColumnWidth(i, 40) for i in range(3, 24)]

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(scenario_data_table, 1, 0, 1, 1)
        self.setLayout(layout)
