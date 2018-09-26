#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, Qt, QModelIndex, QVariant, QAbstractTableModel, pyqtSignal
from PIL import Image
from parsers import Character, Numerical
from configs import DATA_PARAMETER
from attributes import Address, Quantity
from widgets.common import LineText, MultilineText


class ColumnObject(QObject):
    mapping: dict = None

    def __init__(self, parent, editor, data_name: str, mapping_name: str = None, attach=None):
        QObject.__init__(self, parent)
        self.editor = editor
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_type = self.pointer_parser(self.editor.parser_type, data_name)
        self.mapping_type = self.parser(Character, mapping_name)
        self.refresh_data()

    def parser(self, parser_type, parameter_name):
        parameter = DATA_PARAMETER.get(parameter_name)
        if not parameter:
            return None
        return parser_type(self.parent(), **parameter)

    def pointer_parser(self, parser_type, parameter_name):
        parameter = DATA_PARAMETER.get(parameter_name)
        parameter['address'] = {'normal_offset': Address(**parameter.get('address'))(self.parent().buffer, 0)}
        parameter['quantity'] = {'normal_quantity': Quantity(**parameter.get('quantity'))(self.parent().buffer, 0)}
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
            mapping.update({0x100 ** self.data_type.length.normal_length - 1: '—'})
        elif isinstance(self.attach, int):
            number = {i: i for i in range(self.attach + 1)}
            number.update({0x100 ** self.data_type.length.normal_length - 1: '—'})
            mapping.update(number)
        return mapping

    def get_data(self, index: QModelIndex, role=Qt.DisplayRole):
        data = self.data_type.get_data(index.row())
        if role == Qt.DecorationRole:
            if isinstance(self.mapping.get(data), Image.Image):
                return self.mapping.get(data).toqpixmap()
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
    dataEdited = pyqtSignal()

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
            self.dataEdited.emit()

    def flags(self, index: QModelIndex):
        if not index.isValid():
            return QVariant()
        if self.column_objects[index.column()].get_data(index, Qt.EditRole) is None:
            return Qt.ItemIsEnabled
        return Qt.ItemIsEditable | Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def paste_data(self, index: QModelIndex, value):
        if self.column_objects[index.column()].editor in (LineText, MultilineText):
            _value = str(value).replace('_', '\n') if value is not None else self.data(index, Qt.EditRole)
        else:
            try:
                _value = int(value) if value is not None else 0
            except ValueError:
                _value = self.data(index, Qt.EditRole)
        self.setData(index, _value, Qt.EditRole)

    def paste_range(self, select_range: list, text_data: str):
        if select_range and text_data:
            start_row = min([index.row() for index in select_range])
            start_column = min([index.column() for index in select_range])
            max_row = self.rowCount() - start_row
            max_column = self.columnCount() - start_column
            data = [row.split('\t')[: max_column] for row in text_data.split('\n') if row][: max_row]
            for rid, row_data in enumerate(data):
                for cid, value in enumerate(row_data):
                    idx = self.createIndex(start_row + rid, start_column + cid)
                    self.paste_data(idx, value)

    def copy_range(self, select_range):
        if select_range:
            r = range(max([index.row() for index in select_range]) - min([index.row() for index in select_range]) + 1)
            c = max([index.column() for index in select_range]) - min([index.column() for index in select_range]) + 1
            return '\n'.join(['\t'.join([str(self.data(select_range[c * rid + cid], Qt.EditRole)).replace('\n', '_')
                                         for cid in range(c)]) for rid in r])
