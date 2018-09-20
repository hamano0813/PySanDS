#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common.background_frame import BackgroundFrame
from widgets.common.grid_table import GridTable
from widgets.common.fixed_text import FixedText
from widgets.common.value_spin import ValueSpin
from widgets.common.mapping_combo import MappingCombo
from widgets.common.multiline_text import MultilineText

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


class CharAttribute(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        attribute_table = GridTable(self, [
            (FixedText, '武将データ_名前'),
            (FixedText, '武将データ_読み'),
            (ValueSpin, '武将データ_武力', None, 100),
            (ValueSpin, '武将データ_知力', None, 100),
            (ValueSpin, '武将データ_政治', None, 100),
            (ValueSpin, '武将データ_魅力', None, 100),
            (ValueSpin, '武将データ_陸指', None, 100),
            (ValueSpin, '武将データ_水指', None, 100),
            (ValueSpin, '武将データ_野望'),
            (ValueSpin, '武将データ_幸運'),
            (ValueSpin, '武将データ_冷静'),
            (ValueSpin, '武将データ_勇猛'),
            (ValueSpin, '武将データ_相性'),
            (ValueSpin, '武将データ_義理'),
            (ValueSpin, '武将データ_生年'),
            (ValueSpin, '武将データ_寿命'),
            (MappingCombo, '武将データ_家族', None, family),
            (MultilineText, '文本_キャラ伝記')
        ])
        layout = QGridLayout()
        layout.addWidget(attribute_table)
        self.setLayout(layout)
