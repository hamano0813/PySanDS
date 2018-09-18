#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo

family = {
    0: '00.曹操',
    1: '01.劉備',
    2: '02.孫堅',
    3: '03.袁紹',
    4: '04.袁術',
    5: '05.馬騰',
    6: '06.劉焉',
    7: '07.劉表',
    8: '08.董卓',
    9: '09.公孫瓚',
    10: '0A.張魯',
    11: '0B.孟獲',
    12: '0C.荀彧',
    255: 'ーー'
}


class SergeantAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        attribute_table = GridTable(self, [
            (FixedText, '武将属性_姓名'),
            (FixedText, '武将属性_读音'),
            (ValueSpin, '武将属性_武力', None, 100),
            (ValueSpin, '武将属性_智力', None, 100),
            (ValueSpin, '武将属性_政治', None, 100),
            (ValueSpin, '武将属性_魅力', None, 100),
            (ValueSpin, '武将属性_陆指', None, 100),
            (ValueSpin, '武将属性_水指', None, 100),
            (ValueSpin, '武将属性_野望'),
            (ValueSpin, '武将属性_幸运'),
            (ValueSpin, '武将属性_冷静'),
            (ValueSpin, '武将属性_勇猛'),
            (ValueSpin, '武将属性_相性'),
            (ValueSpin, '武将属性_义理'),
            (ValueSpin, '武将属性_生年'),
            (ValueSpin, '武将属性_寿命'),
            (MappingCombo, '武将属性_家族', None, family),
        ])
        layout = QGridLayout()
        layout.addWidget(attribute_table)
        self.setLayout(layout)
