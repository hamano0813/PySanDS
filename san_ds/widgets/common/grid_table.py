#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QTableView, QStyledItemDelegate
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal, QRect, QSize
from widgets.abstract import ControlObject
from widgets.common.multiline_text import MultilineText


class GridDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        QStyledItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index: QModelIndex):
        parent.buffer = self.parent().buffer
        model = index.model()
        editor = model.column_objects[index.column()].create_editor(parent)
        return editor

    def setEditorData(self, editor, index: QModelIndex):
        value = index.model().data(index, Qt.EditRole)
        editor.set_value(value)

    def setModelData(self, editor, model, index: QModelIndex):
        index.model().setData(index, editor.get_value(), Qt.EditRole)

    def updateEditorGeometry(self, editor, option, index: QModelIndex):
        if isinstance(editor, MultilineText):
            bottom = option.rect.bottom()
            width = option.rect.width()
            rect: QRect = option.rect
            rect.setSize(QSize(width, width // 3))
            if option.rect.bottom() > editor.parent().rect().height():
                rect.setTop(bottom - width // 3)
                rect.setBottom(bottom)
            editor.setGeometry(rect)
        else:
            editor.setGeometry(option.rect)


class GridTable(QTableView, ControlObject):
    currentIndexChanged = pyqtSignal(int)

    def __init__(self, parent):
        QTableView.__init__(self, parent)
        self.control_widgets = []
        self.control_targets = []
        self.buffer = parent.buffer
        # noinspection PyUnresolvedReferences
        self.clicked[QModelIndex].connect(self.index_changed)
        self.currentIndexChanged[int].connect(self.control_index)

    def refresh_data(self):
        self.setModel(self.model())

    def index_changed(self, index: QModelIndex):
        row_index = index.row()
        self.currentIndexChanged.emit(row_index)
