#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFrame, QLabel, QComboBox, QGridLayout
from PyQt5.QtCore import Qt
from PIL import Image
from parsers import Picture
from configs import DATA_PARAMETER, PALETTE_PARAMETER


# noinspection PyUnresolvedReferences
class PictureEditor(QFrame):
    picture_data: Picture

    def __init__(self, parent, picture_parameter: dict):
        QFrame.__init__(self, parent, flags=Qt.FramelessWindowHint)
        self.buffer = parent.buffer
        self.picture_parameter = picture_parameter

        self.picture_label = QLabel()
        self.resize_multiple = 1

        self.name_combo = QComboBox(self)
        self.index_combo = QComboBox(self)
        self.palette_combo = QComboBox(self)

        self.name_combo.currentTextChanged[str].connect(self.name_change)
        self.index_combo.currentIndexChanged.connect(self.refresh_data)
        self.palette_combo.currentIndexChanged.connect(self.refresh_data)

        self.name_combo.addItems(picture_parameter)

        layout = QGridLayout()
        layout.addWidget(QLabel('選擇圖片'), 0, 0, 1, 1)
        layout.addWidget(self.name_combo, 1, 0, 1, 1)
        layout.addWidget(QLabel('選擇編號'), 0, 1, 1, 1)
        layout.addWidget(self.index_combo, 1, 1, 1, 1)
        layout.addWidget(QLabel('選擇色板'), 0, 2, 1, 1)
        layout.addWidget(self.palette_combo, 1, 2, 1, 1)
        layout.addWidget(self.picture_label, 2, 0, 1, 5)
        layout.addWidget(QLabel(), 3, 0, 1, 1)

        self.setLayout(layout)

    def name_change(self, name: str):
        picture_setting = DATA_PARAMETER.get('圖片_' + name)
        self.index_combo.disconnect()
        self.index_combo.clear()
        if picture_setting:
            self.index_combo.addItems([f'{i+1:>3d}' for i in range(picture_setting['quantity']['normal_quantity'])])
            self.index_combo.setEnabled(True)
        else:
            self.index_combo.setEnabled(False)
        self.index_combo.currentIndexChanged.connect(self.refresh_data)

        if self.picture_parameter.get(name):
            palette_setting = PALETTE_PARAMETER.get('色板_' + self.picture_parameter.get(name))
        else:
            palette_setting = ()
        self.palette_combo.disconnect()
        self.palette_combo.clear()
        if palette_setting:
            self.palette_combo.addItems([f'0x{address:08X}' for address in palette_setting])
            self.palette_combo.setEnabled(True)
        else:
            self.palette_combo.setEnabled(False)
        self.palette_combo.currentIndexChanged.connect(self.refresh_data)
        self.refresh_data()

    def refresh_data(self):
        picture_setting = DATA_PARAMETER.get('圖片_' + self.name_combo.currentText())
        self.picture_data = Picture(self, **picture_setting)
        if self.palette_combo.isEnabled():
            self.picture_data.palette.set_normal_offset(int(self.palette_combo.currentText(), 16))
        if self.index_combo.isEnabled():
            picture = self.picture_data.get_data(self.index_combo.currentIndex())
        else:
            picture = self.picture_data.get_data(0)
        self.set_picture(picture)

    def set_picture(self, picture: Image.Image):
        width = self.picture_data.width * self.resize_multiple
        height = self.picture_data.height * self.resize_multiple
        self.picture_label.setFixedSize(width, height)
        picture.resize((width, height))
        self.picture_label.setPixmap(picture.toqpixmap())
