#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtCore import Qt
from widgets.common import *
from parsers import Picture
from attributes import Quantity
from configs import DATA_PARAMETER

emblem_offsets = [0x0, 0x22, 0x44, 0x66, 0x88, 0xAA, 0xCC]
data_offsets = [0x0, -0x222, -0x444, -0x666, -0x888, -0xAAA, 0x222]


def header_data(self, section: int, orientation, role=Qt.DisplayRole):
    if orientation == Qt.Horizontal and role == Qt.DisplayRole:
        if section > 2:
            return self.column_objects[1].get_data(self.createIndex(section - 3, 0), Qt.DisplayRole).split('.')[
                       -1] + '\n' + \
                   self.column_objects[2].get_data(self.createIndex(section - 3, 0), Qt.DisplayRole).split('.')[-1]
        return self.column_objects[section].data_name.split('_')[-1]
    elif orientation == Qt.Vertical and role == Qt.DisplayRole:
        return section + 1


Model = type('Model', (NormalModel, ), {'headerData': header_data})


class ForceAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        picture = Picture(self, **DATA_PARAMETER.get('圖片_紋章1')).get_data(0)
        emblem_dict = {i + 1: picture.crop((10 + 10 * i, 0, 20 + 10 * i, 10)).resize((18, 18)) for i in range(21)}

        scenario_combo = ControlCombo(self, '劇本屬性_劇本標題')

        force_attr_table = GridTable(self)
        force_attr_model = Model(self, [
            (PictureCombo, '劇本勢力_紋章', None, emblem_dict),
            (MappingCombo, '劇本勢力_君主', '武將屬性_姓名', True),
            (MappingCombo, '劇本勢力_首都', '都市屬性_都市名', True),
            (ValueSpin, '劇本勢力_敵對01', None, 100),
            (ValueSpin, '劇本勢力_敵對02', None, 100),
            (ValueSpin, '劇本勢力_敵對03', None, 100),
            (ValueSpin, '劇本勢力_敵對04', None, 100),
            (ValueSpin, '劇本勢力_敵對05', None, 100),
            (ValueSpin, '劇本勢力_敵對06', None, 100),
            (ValueSpin, '劇本勢力_敵對07', None, 100),
            (ValueSpin, '劇本勢力_敵對08', None, 100),
            (ValueSpin, '劇本勢力_敵對09', None, 100),
            (ValueSpin, '劇本勢力_敵對10', None, 100),
            (ValueSpin, '劇本勢力_敵對11', None, 100),
            (ValueSpin, '劇本勢力_敵對12', None, 100),
            (ValueSpin, '劇本勢力_敵對13', None, 100),
            (ValueSpin, '劇本勢力_敵對14', None, 100),
            (ValueSpin, '劇本勢力_敵對15', None, 100),
            (ValueSpin, '劇本勢力_敵對16', None, 100),
            (ValueSpin, '劇本勢力_敵對17', None, 100),
            (ValueSpin, '劇本勢力_敵對18', None, 100),
            (ValueSpin, '劇本勢力_敵對19', None, 100),
            (ValueSpin, '劇本勢力_敵對20', None, 100),
            (ValueSpin, '劇本勢力_敵對21', None, 100),
        ], Quantity(0x15))
        force_attr_table.setModel(force_attr_model)
        force_attr_table.setItemDelegate(GridDelegate(self))

        scenario_combo.add_control_target(force_attr_model.column_objects[0].data_type.set_offset, emblem_offsets)
        [scenario_combo.add_control_target(force_attr_model.column_objects[i].data_type.set_offset, data_offsets)
         for i in range(1, 24)]
        scenario_combo.add_control_widget(force_attr_table)

        force_attr_table.setColumnWidth(0, 45)
        force_attr_table.setColumnWidth(1, 100)
        force_attr_table.setColumnWidth(2, 70)
        [force_attr_table.setColumnWidth(i, 56) for i in range(3, 24)]

        force_attr_model.dataEdited.connect(force_attr_table.refresh_data)

        layout = QGridLayout()
        layout.addWidget(scenario_combo, 0, 0, 1, 1)
        layout.addWidget(force_attr_table, 1, 0, 1, 1)
        self.setLayout(layout)
