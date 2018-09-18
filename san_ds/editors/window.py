#!/usr/bin/env python
# -*- coding: utf-8 -*-

from types import MethodType
from PyQt5.QtWidgets import QMainWindow, QAction, QMenu, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from editors.commander.commander_attribute import CommanderAttribute

CHILD_MAPPING = {
    '武将属性': CommanderAttribute,

}


class MainWindow(QMainWindow):
    file_path: str = None
    buffer: bytearray = None
    child_frame = None

    def __init__(self):
        QMainWindow.__init__(self, parent=None, flags=Qt.WindowMinMaxButtonsHint | Qt.WindowCloseButtonHint)
        self.init_menu()
        self.setWindowTitle('三国志DS Rom编辑器 - by 全力全开')
        self.setMinimumSize(800, 600)

    def init_menu(self):
        load_rom = self.create_action('载入Rom', self.load_rom)
        save_rom = self.create_action('保存Rom', self.save_rom)
        save_rom.setEnabled(False)
        save_as = self.create_action('另存为', self.save_as)
        save_as.setEnabled(False)
        close_child = self.create_action('关闭窗口', self.close_child)
        exit_editor = self.create_action('退出', self.close)

        commander_attribute = self.create_action('武将属性', self.open_editor_frame)

        commander_menu = self.create_menu('武将编辑', None, [commander_attribute])
        commander_menu.setEnabled(False)

        file_menu = self.create_menu('文件', None, [load_rom, save_rom, save_as, close_child, exit_editor])
        self.menuBar().addMenu(file_menu)
        self.menuBar().addMenu(commander_menu)

    def load_rom(self):
        file_path = QFileDialog().getOpenFileName(None, '打开Rom文件', './', 'Rom文件 *.nds',
                                                  options=QFileDialog.DontResolveSymlinks)[0]
        if file_path:
            self.file_path = file_path
            self.buffer = bytearray(open(self.file_path, 'rb').read())
            self.start_edit()

    def save_rom(self):
        file = open(self.file_path, 'wb')
        file.write(self.buffer)
        file.close()
        box = QMessageBox(QMessageBox.Warning, '完毕', '保存完毕\n是否退出？')
        yes = box.addButton('确定', QMessageBox.YesRole)
        box.addButton('取消', QMessageBox.NoRole)
        box.exec_()
        if box.clickedButton() == yes:
            self.close()

    def save_as(self):
        file_path = QFileDialog().getSaveFileName(None, '另存为Rom文件', './', 'Rom文件 *.nds',
                                                  options=QFileDialog.DontResolveSymlinks)[0]
        if file_path:
            self.file_path = file_path
            self.save_rom()

    def close_child(self):
        if self.centralWidget():
            self.centralWidget().close()

    def start_edit(self):
        self.findChild(QAction, '保存Rom').setEnabled(True)
        self.findChild(QAction, '另存为').setEnabled(True)
        self.findChild(QMenu, '武将编辑').setEnabled(True)

    def create_action(self, name: str, slot: MethodType=None, icon: str=None) -> QAction:
        action = QAction(name, self)
        action.setObjectName(name)
        if slot:
            action.triggered.connect(slot)
        if icon:
            action.setIcon(QIcon(icon))
        return action

    def create_menu(self, name: str, icon: str=None, child_objects: iter=None) -> QMenu:
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
