#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout, QLabel
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.control_combo import ControlCombo
from widgets.common.address_spin import AddressSpin
from attributes import Address, Quantity

identity = {
    0: '君主[流浪]',
    1: '军师',
    2: '将军',
    3: '武将',
    4: '文官',
    5: '流浪跟随',
    6: '在野',
    7: '未登场',
    128: '君主',
    129: '军师[太守]',
    130: '将军[太守]',
    131: '武将[太守]',
    132: '文官[太守]',
    255: '死亡'
}

debut_offsets = [0x0, -0xC04, -0x1808, -0x240C, -0x3010, -0x3C14, 0xC04]

main_start_offset = mirror_start_offset = [0x0, 0x4, 0x8, 0xC, 0x10, 0x14, 0x18]
main_end_offset = [0x0, -0x7f75c, -0x153d24, -0x7f764, -0x7f760, -0x7f76c, -0x7f768]
mirror_end_offset = [0x0, -0x5c584, -0x129cf4, -0x5c58c, -0x5c588, -0x5c594, -0x5c590]


class CommanderDebut(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        scenario_combo = ControlCombo(self, '剧本属性_剧本名')

        scenario_debut = GridTable(self, [
            (FixedText, '武将属性_姓名'),
            (ValueSpin, '武将登场_登场年'),
            (MappingCombo, '武将登场_血缘', '武将属性_姓名', True),
            (MappingCombo, '武将登场_身份', None, identity),
            (MappingCombo, '武将登场_都市', '都市属性_名称', True),
            (ValueSpin, '武将登场_忠诚', None, 100),
            (ValueSpin, '武将登场_士兵数', None, 200),
        ], Quantity(0x301))
        scenario_combo.add_control_target(scenario_debut.model().column_objects[3].data_type.set_offset, debut_offsets)
        scenario_combo.add_control_target(scenario_debut.model().column_objects[4].data_type.set_offset, debut_offsets)
        scenario_combo.add_control_target(scenario_debut.model().column_objects[5].data_type.set_offset, debut_offsets)
        scenario_combo.add_control_target(scenario_debut.model().column_objects[6].data_type.set_offset, debut_offsets)

        scenario_city = GridTable(self, [
            (MappingCombo, '武将登场_未登场武将', '武将属性_姓名', True),
            (MappingCombo, '武将登场_登场都市', '都市属性_名称', True),
        ], Quantity(None,0x000FBC50,0x4,0x0017B3C4))
        d1_addr = AddressSpin(self, Address(0x000FBC50, -0x1FFC000), mirror_address=Address(0x0011EE28, -0x1FFC000))
        d2_addr = AddressSpin(self, Address(0x0017B3C4, -0x1FFC000), mirror_address=Address(0x0017B3C4, -0x1FFC000))
        d1_addr.setSingleStep(4)
        d2_addr.setSingleStep(4)
        scenario_city_columns = scenario_city.model().column_objects
        d1_addr.add_control_target(scenario_city_columns[0].data_type.address.set_normal_offset, lambda x: x + 2)
        d1_addr.add_control_target(scenario_city_columns[1].data_type.address.set_normal_offset, lambda x: x)
        d1_addr.control_target()
        scenario_combo.add_control_widget(d1_addr)
        scenario_combo.add_control_widget(d2_addr)
        scenario_combo.add_control_target(d1_addr.set_main_offset, main_start_offset)
        scenario_combo.add_control_target(d1_addr.set_mirror_offset, mirror_start_offset)
        scenario_combo.add_control_target(d2_addr.set_main_offset, main_end_offset)
        scenario_combo.add_control_target(d2_addr.set_mirror_offset, mirror_end_offset)

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(scenario_debut, 1, 0, 1, 1)
        layout.addWidget(QLabel('未登场配置地址'), 0, 1, 1, 1)
        layout.addWidget(d1_addr, 0, 2, 1, 1)
        layout.addWidget(d2_addr, 0, 3, 1, 1)
        layout.addWidget(scenario_city, 1, 1, 1, 3)
        self.setLayout(layout)

        scenario_combo.setCurrentIndex(1)

        print(1)
