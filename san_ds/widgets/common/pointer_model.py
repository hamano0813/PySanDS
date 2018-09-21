#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, Qt, QModelIndex, QVariant, QAbstractTableModel
from PyQt5.QtGui import QIcon
from PIL import Image
from parsers import Character, Numerical
from configs import DATA_PARAMETER
from attributes import Address, Quantity


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
        data = self.data_type.get_data(index.row())
        if role == Qt.DecorationRole:
            if isinstance(self.mapping.get(data), Image.Image):
                return QIcon(self.mapping.get(data).toqpixmap())
        if role == Qt.DisplayRole:
            if self.mapping:
                if isinstance(self.mapping.get(data), Image.Image):
                    return QVariant()
                return self.mapping.get(data) if self.mapping.get(data) is not None else QVariant()
            return str(data)
        if role == Qt.EditRole:
            return self.data_type.get_data(index.row())
        if role == Qt.TextAlignmentRole:
            if isinstance(self.data_type, Character):
                return Qt.AlignLeft | Qt.AlignVCenter
            elif isinstance(self.data_type, Numerical):
                if isinstance(self.attach, dict) or self.mapping_name:
                    return Qt.AlignLeft | Qt.AlignVCenter
                return Qt.AlignRight | Qt.AlignVCenter
        return QVariant()

    def set_data(self, index: QModelIndex, data, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.data_type.set_data(index.row(), data)

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
        if role == Qt.DecorationRole:
            return self.column_objects[index.column()].get_data(index, role)
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
