#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject, Qt, QModelIndex, QVariant
from parsers import Character, Numerical, Picture
from configs import DATA_PARAMETER
from widgets.common import FixedText


class ColumnObject(QObject):
    mapping: dict = None

    def __init__(self, parent, editor, data_name: str, mapping_name: str = None, attach=None):
        QObject.__init__(self, parent)
        self.editor = editor
        self.data_name = data_name
        self.mapping_name = mapping_name
        self.attach = attach
        self.data_parser = self.parser(self.editor.parser_type, data_name)
        self.mapping_parser = self.parser(Character, mapping_name)
        self.refresh_data()

    def refresh_data(self):
        self.mapping = self.get_mapping()

    def get_mapping(self):
        mapping = {}
        if self.mapping_parser:
            mapping.update(self.mapping_parser.mapping())
        if isinstance(self.attach, dict):
            mapping.update(self.attach)
        elif self.attach is True:
            mapping.update({0x100 ** self.data_parser.length.normal_length - 1: 'ーー'})
        return mapping

    def parser(self, parser_type, parameter_name):
        parameter = DATA_PARAMETER.get(parameter_name)
        if not parameter:
            return None
        return parser_type(self.parent(), **parameter)

    def get_data(self, index: QModelIndex, role=Qt.DisplayRole):
        if role == Qt.DisplayRole:
            if isinstance(self.data_parser, Picture):
                return str(index.row()) + 'Picture'
            data = self.data_parser.get_data(index.row())
            if self.mapping:
                return self.mapping.get(data) if self.mapping.get(data) is not None else QVariant()
            return str(data)
        if role == Qt.EditRole:
            return self.data_parser.get_data(index.row())
        if role == Qt.TextAlignmentRole:
            if isinstance(self.data_parser, Character):
                return Qt.AlignLeft | Qt.AlignVCenter
            elif isinstance(self.data_parser, Numerical):
                if self.mapping:
                    return Qt.AlignRight | Qt.AlignVCenter
                return Qt.AlignLeft | Qt.AlignVCenter
        return QVariant()

    def set_data(self, index: QModelIndex, data, role=Qt.EditRole):
        if index.isValid() and role == Qt.EditRole:
            self.data_parser.set_data(index.row(), data)

    @property
    def widget_width(self):
        if self.editor == FixedText:
            return self.data_parser.length.normal_length * 8
        else:
            return 20
