#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *
from attributes import Quantity

city_offsets = [0x0, -0x5C0, -0xB80, -0x1140, -0x1700, -0x1CC0, 0x5C0]
choose = {0: '—', 1: '○'}


class CityAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_combo = ControlCombo(self, '劇本屬性_劇本名')

        city_attr_table = GridTable(self)
        city_attr_model = NormalModel(self, [
            (LineText, '都市屬性_都市名'),
            (LineText, '都市屬性_讀音'),
            (MappingCombo, '都市屬性_次都市', '都市屬性_都市名', True),
            (MappingCombo, '都市屬性_軍師', '武將屬性_姓名', True),
            (MappingCombo, '都市屬性_港口', None, choose),
            (MappingCombo, '都市屬性_商人', None, choose),
            (ValueSpin, '都市屬性_肥沃度'),
            (ValueSpin, '都市屬性_人口', None, 3000),
            (ValueSpin, '都市屬性_金', None, 500),
            (ValueSpin, '都市屬性_兵糧', None, 3000),
            (ValueSpin, '都市屬性_開発', None, 100),
            (ValueSpin, '都市屬性_灌漑', None, 100),
            (ValueSpin, '都市屬性_治水', None, 100),
            (ValueSpin, '都市屬性_商業', None, 9999),
            (ValueSpin, '都市屬性_税率', None, 100),
            (ValueSpin, '都市屬性_民忠', None, 100),
            (ValueSpin, '都市屬性_弩', None, 9999),
            (ValueSpin, '都市屬性_強弩', None, 9999),
            (ValueSpin, '都市屬性_軍馬', None, 9999),
            (ValueSpin, '都市屬性_闘艦', None, 99),
            (ValueSpin, '都市屬性_蒙衝', None, 99),
            (ValueSpin, '都市屬性_走舸', None, 99),
            (ValueSpin, '都市屬性_訓練', None, 100),
            (ValueSpin, '都市屬性_士気', None, 120),
        ], Quantity(0x2E))
        city_attr_table.setModel(city_attr_model)
        city_attr_table.setItemDelegate(GridDelegate(self))
        [city_attr_table.setColumnWidth(i, 75) for i in range(0, 3)]
        city_attr_table.setColumnWidth(3, 110)
        [city_attr_table.setColumnWidth(i, 50) for i in range(4, 24)]
        [city_attr_table.setColumnWidth(i, 60) for i in (7, 9, 13, 16, 17, 18)]

        [scenario_combo.add_control_target(city_attr_model.column_objects[i].data_type.set_offset, city_offsets)
         for i in range(2, 24)]
        scenario_combo.add_control_widget(city_attr_table)

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(city_attr_table, 1, 0, 1, 1)
        self.setLayout(layout)
