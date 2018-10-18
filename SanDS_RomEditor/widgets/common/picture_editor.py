#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import (QFrame, QLabel, QComboBox, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout,
                             QStyledItemDelegate, QScrollArea)
from PyQt5.QtCore import Qt
from PIL import Image
from parsers import Picture
from configs import DATA_PARAMETER, PALETTE_PARAMETER


# noinspection PyUnresolvedReferences, PyArgumentList
class PictureEditor(QFrame):
    picture_data: Picture
    pic_path: str='./'

    def __init__(self, parent, picture_parameter: dict):
        QFrame.__init__(self, parent, flags=Qt.FramelessWindowHint)
        self.buffer = parent.buffer
        self.picture_parameter = picture_parameter

        self.picture_label = QLabel()
        self.resize_multiple = 1

        scroll = QScrollArea(self)
        scroll.setWidget(self.picture_label)

        self.name_combo = QComboBox(self)
        self.index_combo = QComboBox(self)
        self.palette_combo = QComboBox(self)
        self.resize_combo = QComboBox(self)

        self.name_combo.setFixedWidth(120)
        self.index_combo.setFixedWidth(120)
        self.palette_combo.setFixedWidth(120)
        self.resize_combo.setFixedWidth(120)

        self.name_combo.setItemDelegate(QStyledItemDelegate())
        self.index_combo.setItemDelegate(QStyledItemDelegate())
        self.palette_combo.setItemDelegate(QStyledItemDelegate())
        self.resize_combo.setItemDelegate(QStyledItemDelegate())

        self.resize_combo.addItems([f'          × {i + 1}' for i in range(4)])

        self.name_combo.currentTextChanged[str].connect(self.name_change)
        self.index_combo.currentIndexChanged.connect(self.refresh_data)
        self.palette_combo.currentIndexChanged.connect(self.refresh_data)
        self.resize_combo.currentIndexChanged.connect(self.refresh_data)

        self.name_combo.addItems(picture_parameter)

        output_button = QPushButton('導出圖片')
        input_button = QPushButton('導入圖片')
        output_button.clicked.connect(self.output_picture)
        input_button.clicked.connect(self.input_picture)

        control_layout = QVBoxLayout()
        control_layout.addWidget(QLabel('選擇圖片'), alignment=Qt.AlignLeft)
        control_layout.addWidget(self.name_combo, alignment=Qt.AlignRight)
        control_layout.addWidget(QLabel('選擇編號'), alignment=Qt.AlignLeft)
        control_layout.addWidget(self.index_combo, alignment=Qt.AlignRight)
        control_layout.addWidget(QLabel('選擇色板'), alignment=Qt.AlignLeft)
        control_layout.addWidget(self.palette_combo, alignment=Qt.AlignRight)
        control_layout.addWidget(QLabel('缩放比例'), alignment=Qt.AlignLeft)
        control_layout.addWidget(self.resize_combo, alignment=Qt.AlignRight)
        control_layout.addWidget(output_button, alignment=Qt.AlignRight)
        control_layout.addWidget(input_button, alignment=Qt.AlignRight)

        control_layout.addStretch()

        layout = QHBoxLayout()
        layout.addLayout(control_layout)
        layout.addWidget(scroll)

        self.setLayout(layout)

    def name_change(self, name: str):
        picture_setting = DATA_PARAMETER.get('圖片_' + name)
        self.index_combo.disconnect()
        self.index_combo.clear()
        self.index_combo.addItems([f'{i+1:>13d}' for i in range(picture_setting['quantity']['normal_quantity'])])
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
        self.resize_multiple = self.resize_combo.currentIndex() + 1
        self.set_picture()

    def set_picture(self):
        picture = self.picture_data.get_data(self.index_combo.currentIndex())
        width = self.picture_data.width * self.resize_multiple
        height = self.picture_data.height * self.resize_multiple
        self.picture_label.setFixedSize(width, height)
        self.picture_label.setPixmap(picture.resize((width, height)).toqpixmap())

    def output_picture(self):
        filename = QFileDialog.getSaveFileName(self, '导出图片', self.pic_path, 'BMP图像(*.bmp)')[0]
        if filename:
            self.pic_path = filename[0: filename.rfind('/') + 1]
            if self.index_combo.isEnabled():
                picture = self.picture_data.get_data(self.index_combo.currentIndex())
            else:
                picture = self.picture_data.get_data(0)
            picture.save(filename)

    def input_picture(self):
        filename = QFileDialog.getOpenFileName(self, '导入图片', self.pic_path, '*.bmp;;*.png;;*.gif;;*.tif')[0]
        if filename:
            self.pic_path = filename[0: filename.rfind('/') + 1]
            width = self.picture_data.width * self.resize_multiple
            height = self.picture_data.height * self.resize_multiple
            picture = Image.open(filename).resize((width, height))
            self.picture_data.set_data(self.index_combo.currentIndex(), picture)
            self.set_picture()
