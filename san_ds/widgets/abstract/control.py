#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QObject


class ControlObject(QObject):
    def add_control_widget(self, widget):
        self.control_widgets.append(widget)

    def add_control_target(self, method, offsets):
        self.control_targets.append([method, offsets])

    def control_index(self, index):
        for method, offsets in self.control_targets:
            method(offsets[index])
        for widget in self.control_widgets:
            widget.refresh_data()
