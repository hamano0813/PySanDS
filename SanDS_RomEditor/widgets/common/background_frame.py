#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt


class BackgroundFrame(QFrame):
    def __init__(self, buffer: bytearray):
        QFrame.__init__(self, parent=None, flags=Qt.FramelessWindowHint)
        self.buffer = buffer
        self.setMouseTracking(True)
