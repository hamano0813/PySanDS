#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout, QLabel
from widgets.common import *
from attributes import Address, Quantity

person_identity = {0: '君主[放浪]', 1: '軍師', 2: '将軍', 3: '武將', 4: '文官', 5: '放浪', 6: '在野', 7: '未登場',
                   128: '君主', 129: '軍師[太守]', 130: '将軍[太守]', 131: '武將[太守]', 132: '文官[太守]', 255: '死亡'}
debut_offsets = [0x0, -0xC04, -0x1808, -0x240C, -0x3010, -0x3C14, 0xC04]

start_offsets = [0x0, 0x4, 0x8, 0xC, 0x10, 0x14, 0x18]
end_main_offsets = [0x0, -0x7f75c, -0x153d24, -0x7f764, -0x7f760, -0x7f76c, -0x7f768]
end_mirror_offsets = [0x0, -0x5c584, -0x129cf4, -0x5c58c, -0x5c588, -0x5c594, -0x5c590]
start_ranges = [(), (), (), (), (), (), ()]
end_ranges = [(), (), (), (), (), (), ()]


class DebutAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        self.scenario_combo = ControlCombo(self, '劇本屬性_劇本名')

        debut_attr_table = GridTable(self)
        debut_attr_model = NormalModel(self, [
            (LineText, '武將屬性_姓名'),
            (ValueSpin, '武將登場_登場年'),
            (MappingCombo, '武將登場_血緣', '武將屬性_姓名', True),
            (MappingCombo, '武將登場_身份', None, person_identity),
            (MappingCombo, '武將登場_所在都市', '都市屬性_都市名', True),
            (ValueSpin, '武將登場_忠誠', None, 100),
            (ValueSpin, '武將登場_兵数', None, 200),
        ], Quantity(0x301))
        debut_attr_table.setModel(debut_attr_model)
        debut_attr_table.setItemDelegate(GridDelegate(self))

        [self.scenario_combo.add_control_target(debut_attr_model.column_objects[i].data_type.set_offset, debut_offsets)
         for i in range(3, 7)]
        self.scenario_combo.add_control_widget(debut_attr_table)

        [debut_attr_table.setColumnWidth(i, width) for i, width in enumerate([60, 45, 100, 80, 70, 45, 45])]

        self.debut_city_table = GridTable(self)
        debut_city_model = PointerModel(self, [
            (MappingCombo, '武將登場_未登場武將', '武將屬性_姓名', True),
            (MappingCombo, '武將登場_登場都市', '都市屬性_都市名', True)
        ])
        self.start_address = AddressSpin(self, Address(0x000FBC50, -0x1FFC000), Address(0x0011EE28, -0x1FFC000))
        self.end_address = AddressSpin(self, Address(0x0017B3C4, -0x1FFC000), Address(0x0017B3C4, -0x1FFC000))
        self.start_address.setSingleStep(4)
        self.end_address.setSingleStep(4)

        self.scenario_combo.add_control_target(self.start_address.set_main_offset, start_offsets)
        self.scenario_combo.add_control_target(self.start_address.set_mirror_offset, start_offsets)
        self.scenario_combo.add_control_target(self.end_address.set_main_offset, end_main_offsets)
        self.scenario_combo.add_control_target(self.end_address.set_mirror_offset, end_mirror_offsets)
        self.scenario_combo.add_control_widget(self.start_address)
        self.scenario_combo.add_control_widget(self.end_address)
        self.start_address.valueChanged.connect(self.new_model)
        self.end_address.valueChanged.connect(self.new_model)

        self.debut_city_table.setModel(debut_city_model)
        self.debut_city_table.setItemDelegate(GridDelegate(self))

        self.debut_city_table.setColumnWidth(0, 100)
        self.debut_city_table.setColumnWidth(1, 70)

        layout = QGridLayout()
        layout.addWidget(self.scenario_combo, 0, 0, 1, 5)
        layout.addWidget(debut_attr_table, 2, 0, 1, 1)
        layout.addWidget(QLabel('開始地址'), 1, 1, 1, 1)
        layout.addWidget(self.start_address, 1, 2, 1, 1)
        layout.addWidget(QLabel('結束地址'), 1, 3, 1, 1)
        layout.addWidget(self.end_address, 1, 4, 1, 1)
        layout.addWidget(self.debut_city_table, 2, 1, 1, 4)
        self.setLayout(layout)

    def new_model(self):
        model = PointerModel(self, [
            (MappingCombo, '武將登場_未登場武將', '武將屬性_姓名', True),
            (MappingCombo, '武將登場_登場都市', '都市屬性_都市名', True)
        ])
        model.column_objects[0].data_type.address.set_normal_offset(self.start_address.value() + 2)
        model.column_objects[1].data_type.address.set_normal_offset(self.start_address.value())
        model.column_objects[0].data_type.quantity.set_normal_quantity(
            (self.end_address.value() - self.start_address.value()) // 4)
        model.column_objects[1].data_type.quantity.set_normal_quantity(
            (self.end_address.value() - self.start_address.value()) // 4)
        self.debut_city_table.setModel(model)
        self.debut_city_table.setItemDelegate(GridDelegate(self))
