#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QFrame
from PyQt5.QtCore import Qt
from widgets.common.address_spin import AddressSpin


class QuantitySpin(QFrame):
    def __init__(self, parent, main_pointers, offset, record_length: int=0x4, sub_pointers=None):
        QFrame.__init__(self, parent, flags=Qt.FramelessWindowHint)
        self.main_pointer_primary = main_pointers[0]
        if len(main_pointers) is 2:
            self.main_pointer_mirror = main_pointers[1]
        if sub_pointers:
            self.sub_pointer_primary = sub_pointers[0]
        if len(sub_pointers) is 2:
            self.sub_pointer_mirror = sub_pointers[1]
        self.record_length = record_length
