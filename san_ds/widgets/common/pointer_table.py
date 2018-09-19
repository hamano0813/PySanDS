#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QObject, Qt, QModelIndex, QVariant, QAbstractTableModel, pyqtSignal
from attributes import Address
from parsers import Character, Numerical, Picture
from configs import DATA_PARAMETER
from widgets.abstract import ControlObject
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.grid_table import GridDelegate
from attributes import Quantity


class ColumnObject(QObject):
    mapping: dict = None

    def __init__(self, parent, editor, data_name: str, mapping_name: str = None, attach=None):
        QObject.__init__(self, parent)
        self.offset = 0
        self.editor = editor
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type = self.pointer_parser(self.editor.parser_type, data_name)
        self.mapping_type = self.parser(Character, mapping_name)
        self.refresh_data()

    def set_offset(self, offset):
        self.offset = offset

    def parser(self, parser_type, parameter_name):
        parameter = DATA_PARAMETER.get(parameter_name)
        if not parameter:
            return None
        return parser_type(self.parent(), **parameter)

    def pointer_parser(self, parser_type, parameter_name):
        parameter = DATA_PARAMETER.get(parameter_name)
        parameter['address'] = {'normal_offset': Address(**parameter.get('address'))(self.parent().buffer, self.offset)}
        return parser_type(self.parent(), **parameter)

    def refresh_data(self):
        self.mapping = self.get_mapping()

    def get_mapping(self):
        mapping = {}
        if self.mapping_type:
            mapping.update(self.mapping_type.mapping())
        if isinstance(self.attach, dict):
            mapping.update(self.attach)
        elif self.attach is True:
            mapping.update({0x100 ** self.data_type.length.normal_length - 1: 'ーー'})
        elif isinstance(self.attach, int):
            number = {i: i for i in range(self.attach + 1)}
            number.update({0x100 ** self.data_type.length.normal_length - 1: 'ー'})
            mapping.update(number)
        return mapping

    def get_data(self, index: QModelIndex, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if isinstance(self.data_type, Picture):
                return str(index.row()) + 'Picture'
            data = self.data_type.get_data(index.row())
            if self.mapping:
                return self.mapping.get(data) if self.mapping.get(data) is not None else QVariant()
            return str(data)
        if role == Qt.EditRole:
            return self.data_type.get_data(index.row())
        if role == Qt.TextAlignmentRole:
            if isinstance(self.data_type, Character):
                return Qt.AlignLeft | Qt.AlignVCenter
            elif isinstance(self.data_type, Numerical):
                if self.editor == MappingCombo:
                    return Qt.AlignLeft | Qt.AlignVCenter
                return Qt.AlignRight | Qt.AlignVCenter
        return QVariant()

    def set_data(self, index: QModelIndex, data, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.data_type.set_data(index.row(), data)

    @property
    def widget_width(self):
        if self.editor == FixedText:
            return self.data_type.length.normal_length * 8
        elif self.editor == ValueSpin:
            if self.data_type.bit is None:
                max_value = 0x100 ** self.data_type.length.normal_length - 1
            else:
                max_value = 0x2 ** (self.data_type.bit[1] - self.data_type.bit[0]) - 1
            return len(str(max_value)) * 7 + 25
        elif self.editor == MappingCombo:
            if self.mapping_type:
                return max(len(i.split('.')[0]) + 1 + len(i.split('.')[-1]) * 2 for i in self.mapping.values()) * 7 + 25
            return max(len(i.split('.')[0]) + 1 + len(i.split('.')[-1]) * 2 for i in self.mapping.values()) * 7 + 10
        else:
            return 50

    def create_editor(self, parent):
        return self.editor(parent, self.data_name, self.mapping_name, self.attach)


class PointerModel(QAbstractTableModel):
    def __init__(self, parent, column_settings: iter, quantity: Quantity = None):
        QAbstractTableModel.__init__(self, parent)
        self.column_objects = [ColumnObject(parent, *settings) for settings in column_settings]
        self.quantity = quantity

    def rowCount(self, parent=None, *args, **kwargs):
        if self.quantity:
            return self.quantity(self.parent().buffer, 0)
        return self.column_objects[0].data_type.real_quantity

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.column_objects)

    def headerData(self, section: int, orientation, role=Qt.DisplayRole):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self.column_objects[section].data_name.split('_')[-1]
        elif orientation == Qt.Vertical and role == Qt.DisplayRole:
            return section + 1

    def data(self, index: QModelIndex, role=None):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole:
            if self.column_objects[index.column()].get_data(index, Qt.EditRole) is None:
                return QVariant()
            return self.column_objects[index.column()].get_data(index, role)
        if role == Qt.EditRole:
            return self.column_objects[index.column()].get_data(index, role)
        if role == Qt.TextAlignmentRole:
            return self.column_objects[index.column()].get_data(index, role)

    def setData(self, index: QModelIndex, data_value, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.column_objects[index.column()].set_data(index, data_value, role)

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return QVariant()
        if self.column_objects[index.column()].get_data(index, Qt.EditRole) is None:
            return Qt.ItemIsEnabled
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable


class PointerTable(QTableView, ControlObject):
    currentIndexChanged = pyqtSignal(int)

    def __init__(self, parent, column_settings: iter, quantity: Quantity = None):
        QTableView.__init__(self, parent)
        self.control_widgets = []
        self.control_targets = []
        self.buffer = parent.buffer
        self.quantity = quantity
        self.column_settings = column_settings
        self.setModel = self.set_width(self.setModel)
        self.setModel(PointerModel(self, self.column_settings, self.quantity))
        self.setItemDelegate(GridDelegate(self))
        # noinspection PyUnresolvedReferences
        self.clicked[QModelIndex].connect(self.index_changed)
        self.currentIndexChanged[int].connect(self.control_index)

    def refresh_data(self):
        self.setModel(self.model())

    def index_changed(self, index: QModelIndex):
        row_index = index.row()
        self.currentIndexChanged.emit(row_index)

    def set_width(self, func):
        def wrapper(model: PointerModel):
            func(model)
            for idx, widget in enumerate(model.column_objects):
                self.setColumnWidth(idx, widget.widget_width + 1)
            for idx in range(model.rowCount()):
                self.setRowHeight(idx, 26)

        return wrapper
