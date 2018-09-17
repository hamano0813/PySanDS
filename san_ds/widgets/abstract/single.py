#!/usr/bin/env python
# -*- coding: utf-8 -*-


from PyQt5.QtCore import QObject
from configs import DATA_PARAMETER


class SingleObject(QObject):
    data_index = 0
    data_name = mapping_name = attach = None

    def parser(self, parser_type, name: str):
        parameter = DATA_PARAMETER.get(name)
        if not parameter:
            return None
        return parser_type(self.parent(), **parameter)

    def set_data_index(self, index: int):
        self.data_index = index
        self.refresh_data()

    def refresh_data(self):
        pass

    def save_data(self):
        pass

    def get_value(self):
        pass

    def set_value(self, data):
        pass
