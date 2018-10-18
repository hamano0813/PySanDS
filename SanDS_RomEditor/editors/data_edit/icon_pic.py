#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *

ICON_PARAMETER = {
    '頭像圖片': None,
    '道具圖片': None,
    'LOGO': None,
}


class IconPic(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        picture_editor = PictureEditor(self, ICON_PARAMETER)

        layout = QGridLayout()
        layout.setContentsMargins(3, 5, 3, 5)
        layout.addWidget(picture_editor)
        self.setLayout(layout)
