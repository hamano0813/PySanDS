#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtGui import QIcon
from widgets.window.title_label import TitleLabel

I_WIDTH = 30


class IconLabel(TitleLabel):
    def __init__(self, *args):
        super(IconLabel, self).__init__(*args)
        self.setFixedWidth(I_WIDTH)

    def set_icon(self, icon: QIcon):
        pixmap = icon.pixmap(28, 28)
        self.setPixmap(pixmap)
