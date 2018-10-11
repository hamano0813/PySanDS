#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QSpinBox
from attributes import Address


class AddressSpin(QSpinBox):
    def __init__(self, parent, main_address: Address, mirror_address: Address = None):
        QSpinBox.__init__(self, parent)
        self.main_offset = 0
        self.mirror_offset = 0
        self.control_widgets = []
        self.control_targets = []
        self.main_address = main_address
        self.mirror_address = mirror_address
        self.setFixedWidth(90)
        self.setRange(0, 0x7FFFFFFF)
        # noinspection PyUnresolvedReferences
        self.valueChanged[int].connect(self.set_address)
        self.get_address()

    def add_control_target(self, method, func):
        self.control_targets.append([method, func])

    def control_target(self):
        for method, func in self.control_targets:
            method(func(self.value()))
        for widget in self.control_widgets:
            widget.refresh_data()

    def add_control_widget(self, widget):
        self.control_widgets.append(widget)

    def refresh_data(self):
        self.get_address()

    def set_main_offset(self, offset):
        self.main_offset = offset

    def set_mirror_offset(self, offset):
        self.mirror_offset = offset

    def get_address(self):
        self.setValue(self.main_address(self.parent().buffer, self.main_offset))

    def set_address(self, address_offset):
        self.main_address(self.parent().buffer, self.main_offset, address_offset)
        if self.mirror_address:
            self.mirror_address(self.parent().buffer, self.mirror_offset, address_offset)
        self.control_target()

    def textFromValue(self, value):
        return f'0x{value:08X}'

    def valueFromText(self, text):
        return int(text, 16)
