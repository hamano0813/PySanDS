#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QPushButton

T_B_WIDTH = 40


class TitleButton(QPushButton):
    def __init__(self, *args):
        super(TitleButton, self).__init__(*args)
        self.setFixedWidth(T_B_WIDTH)
        self.setStyleSheet("""
        QTitleButton{background-color: rgba(0, 0, 0, 0);
                     color: black;
                     border: 0px;
                     font-family: 'Webdings';}
        QTitleButton#MinButton:hover{background-color: #D0D0D1;}
        QTitleButton#MaxButton:hover{background-color: #D0D0D1;}
        QTitleButton#CloseButton:hover{background-color: #D32424; color: white;}
        """)
