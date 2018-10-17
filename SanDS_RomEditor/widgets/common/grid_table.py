#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QApplication, QTableView, QStyledItemDelegate, QAbstractButton, QStyleOptionHeader, QStyle,
                             QStylePainter)
from PyQt5.QtCore import Qt, QModelIndex, pyqtSignal, QRect, QSize, QEvent
from PyQt5.QtGui import QKeyEvent
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
        self.keyPressEvent = self.key_press(self.keyPressEvent)
        self.setToolTip('選中內容后\nCtrl+C 複製\nCtrl+V 黏貼')
        self.verticalHeader().setMinimumWidth(40)
        self.verticalHeader().setDefaultAlignment(Qt.AlignCenter)
        corner_button: QAbstractButton = self.findChild(QAbstractButton)
        corner_button.setText('◢')
        corner_button.installEventFilter(self)
        option = QStyleOptionHeader()
        option.text = corner_button.text()

    def refresh_data(self):
        self.reset()
        self.horizontalHeader().reset()

    def index_changed(self, index: QModelIndex):
        row_index = index.row()
        self.currentIndexChanged.emit(row_index)

    def key_press(self, func):
        # noinspection PyArgumentList
        def wrapper(event: QKeyEvent):
            if event.key() == Qt.Key_C and event.modifiers() == Qt.ControlModifier:
                QApplication.clipboard().setText(self.model().copy_range(self.selectedIndexes()))
            elif event.key() == Qt.Key_V and event.modifiers() == Qt.ControlModifier:
                self.model().paste_range(self.selectedIndexes(), QApplication.clipboard().text())
                self.reset()
            else:
                func(event)

        return wrapper

    def eventFilter(self, obj, event):
        if event.type() != QEvent.Paint or not isinstance(obj, QAbstractButton):
            return False
        option: QStyleOptionHeader = QStyleOptionHeader()
        option.initFrom(obj)
        style_state = QStyle.State_None
        if obj.isEnabled():
            style_state |= QStyle.State_Enabled
        if obj.isActiveWindow():
            style_state |= QStyle.State_Active
        if obj.isDown():
            style_state |= QStyle.State_Sunken
        option.state = style_state
        option.rect = obj.rect()
        option.text = obj.text()
        option.position = QStyleOptionHeader.OnlyOneSection
        painter = QStylePainter(obj)
        painter.drawControl(QStyle.CE_Header, option)
        return True
