#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *

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
    255: '—'
}


class CharAttr(BackgroundFrame):
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)

        char_attr_table = GridTable(self)
        char_attr_model = NormalModel(self, [
            (LineText, '武將屬性_姓名'),
            (LineText, '武將屬性_讀音'),
            (ValueSpin, '武將屬性_武力', None, 100),
            (ValueSpin, '武將屬性_智力', None, 100),
            (ValueSpin, '武將屬性_政治', None, 100),
            (ValueSpin, '武將屬性_魅力', None, 100),
            (ValueSpin, '武將屬性_陸指', None, 100),
            (ValueSpin, '武將屬性_水指', None, 100),
            (ValueSpin, '武將屬性_野望'),
            (ValueSpin, '武將屬性_幸運'),
            (ValueSpin, '武將屬性_冷靜'),
            (ValueSpin, '武將屬性_勇猛'),
            (ValueSpin, '武將屬性_相性'),
            (ValueSpin, '武將屬性_義理', None, 100),
            (ValueSpin, '武將屬性_生年'),
            (ValueSpin, '武將屬性_壽命'),
            (MappingCombo, '武將屬性_家族', None, family),
            (MultilineText, '文本_人物列傳')
        ])
        char_attr_table.setModel(char_attr_model)
        char_attr_table.setItemDelegate(GridDelegate(self))

        [char_attr_table.setColumnWidth(i, 60) for i in range(2)]
        [char_attr_table.setColumnWidth(i, 45) for i in range(2, 16)]
        char_attr_table.setColumnWidth(16, 90)
        char_attr_table.setColumnWidth(17, 230)

        layout = QGridLayout()
        layout.addWidget(char_attr_table)
        self.setLayout(layout)
