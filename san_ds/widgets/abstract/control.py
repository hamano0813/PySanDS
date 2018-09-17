#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject


class ControlObject(QObject):
    control_widgets = []
    control_targets = []

    def add_control_widget(self, widget):
        self.control_widgets.append(widget)

    def add_control_target(self, method, offset_dict):
        self.control_targets.append([method, offset_dict])

    def control_index(self, index):
        for method, offset_dict in self.control_targets:
            method(offset_dict[index])
        for widget in self.control_widgets:
            widget.refresh_data()
