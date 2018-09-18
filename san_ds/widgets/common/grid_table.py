#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableView, QStyledItemDelegate
from PyQt5.QtCore import QAbstractTableModel, Qt, QModelIndex, QVariant, pyqtSignal
from widgets.abstract import ColumnObject, ControlObject
from attributes import Quantity


class GridModel(QAbstractTableModel):
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


class GridDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index: QModelIndex):
        parent.buffer = self.parent().buffer
        model: GridModel = index.model()
        editor = model.column_objects[index.column()].create_editor(parent)
        return editor

    def setEditorData(self, editor, index: QModelIndex):
        value = index.model().data(index, Qt.EditRole)
        editor.set_value(value)

    def setModelData(self, editor, model: GridModel, index: QModelIndex):
        index.model().setData(index, editor.get_value(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index: QModelIndex):
        editor.setGeometry(option.rect)


class GridTable(QTableView, ControlObject):
    currentIndexChanged = pyqtSignal(int)

    def __init__(self, parent, column_settings: iter, quantity: Quantity = None):
        QTableView.__init__(self, parent)
        self.control_widgets = []
        self.control_targets = []
        self.buffer = parent.buffer
        self.quantity = quantity
        self.column_settings = column_settings
        self.setModel = self.set_width(self.setModel)
        self.setModel(GridModel(self, self.column_settings, self.quantity))
        self.setItemDelegate(GridDelegate(self))
        # noinspection PyUnresolvedReferences
        self.clicked[QModelIndex].connect(self.index_changed)
        self.currentIndexChanged[int].connect(self.control_index)

    def refresh_data(self):
        self.clicked(self.model().createIndex(0, 0))

    def index_changed(self, index: QModelIndex):
        row_index = index.row()
        self.currentIndexChanged.emit(row_index)

    def set_width(self, func):
        def wrapper(model: GridModel):
            func(model)
            for idx, widget in enumerate(model.column_objects):
                self.setColumnWidth(idx, widget.widget_width + 1)
            for idx in range(model.rowCount()):
                self.setRowHeight(idx, 26)

        return wrapper
