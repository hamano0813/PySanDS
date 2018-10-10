#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt

T_HEIGHT = 30


class TitleLabel(QLabel):
    def __init__(self, *args):
        super(TitleLabel, self).__init__(*args)
        self.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.setFixedHeight(T_HEIGHT)
        self.setIndent(10)
