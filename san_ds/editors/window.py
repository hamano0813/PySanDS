#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from editors.value import CharAttr, DebutAttr, NpcAttr, PropAttr, SpecAttr, ForceAttr

CHILD_MAPPING = {
    '武將修改': CharAttr,
    '登場修改': DebutAttr,
    'NPC修改': NpcAttr,
    '道具修改': PropAttr,
    '特產修改': SpecAttr,
    '勢力修改': ForceAttr,
}


class MainWindow(QMainWindow):
    file_path: str = None
    buffer: bytearray = None
    child_frame = None

    def __init__(self):
        QMainWindow.__init__(self, parent=None, flags=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.init_menu()
        self.setWindowTitle('三國志DS Rom修改器')
        self.setMinimumSize(1280, 720)

    def init_menu(self):
        load_rom = self.create_action('載入Rom', self.load_rom)
        save_rom = self.create_action('保存Rom', self.save_rom)
        save_rom.setEnabled(False)
        save_as = self.create_action('另存為', self.save_as)
        save_as.setEnabled(False)
        close_child = self.create_action('關閉窗口', self.close_child)
        exit_editor = self.create_action('退出', self.close)
        file_menu = self.create_menu('主菜單', None, [load_rom, save_rom, save_as, close_child, exit_editor])
        
        char_attr = self.create_action('武將修改', self.open_editor_frame)
        npc_attr = self.create_action('NPC修改', self.open_editor_frame)
        debut_attr = self.create_action('登場修改', self.open_editor_frame)
        prop_attr = self.create_action('道具修改', self.open_editor_frame)
        spec_attr = self.create_action('特產修改', self.open_editor_frame)
        force_attr = self.create_action('勢力修改', self.open_editor_frame)

        data_menu = self.create_menu('數值修改', None,
                                     [char_attr, npc_attr, debut_attr, prop_attr, spec_attr, force_attr])
        data_menu.setEnabled(False)

        self.menuBar().addMenu(file_menu)
        self.menuBar().addMenu(data_menu)

    def load_rom(self):
        file_path = QFileDialog().getOpenFileName(None, '載入Rom文件', './', 'Rom文件 *.nds',
                                                  options=QFileDialog.DontResolveSymlinks)[0]
        if file_path:
            self.file_path = file_path
            self.buffer = bytearray(open(self.file_path, 'rb').read())
            self.start_edit()

    def save_rom(self):
        file = open(self.file_path, 'wb')
        file.write(self.buffer)
        file.close()
        box = QMessageBox(QMessageBox.Warning, '完成', '保存Rom完畢\n是否退出？')
        yes = box.addButton('確定', QMessageBox.YesRole)
        box.addButton('取消', QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.close()

    def save_as(self):
        file_path = QFileDialog().getSaveFileName(None, '保存Rom文件', './', 'Rom文件 *.nds',
                                                  options=QFileDialog.DontResolveSymlinks)[0]
        if file_path:
            self.file_path = file_path
            self.save_rom()

    def close_child(self):
        if self.centralWidget():
            self.centralWidget().close()

    def start_edit(self):
        self.findChild(QAction, '保存Rom').setEnabled(True)
        self.findChild(QAction, '另存為').setEnabled(True)
        self.findChild(QMenu, '數值修改').setEnabled(True)

    def create_action(self, name: str, slot: MethodType = None, icon: str = None) -> QAction:
        action = QAction(name, self)
        action.setObjectName(name)
        if slot:
            action.triggered.connect(slot)
        if icon:
            action.setIcon(QIcon(icon))
        return action

    def create_menu(self, name: str, icon: str = None, child_objects: iter = None) -> QMenu:
        menu = QMenu(name, self)
        menu.setObjectName(name)
        if icon:
            menu.setIcon(QIcon(icon))
        if child_objects:
            for child_object in child_objects:
                if isinstance(child_object, QAction):
                    menu.addAction(child_object)
                elif isinstance(child_object, QMenu):
                    menu.addMenu(child_object)
                elif child_object is None:
                    menu.addSeparator()
        return menu

    def open_editor_frame(self):
        frame_name = self.sender().objectName()
        child_frame = CHILD_MAPPING[frame_name](self.buffer)
        self.setCentralWidget(child_frame)
