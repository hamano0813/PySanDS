#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QMenuBar, QToolBar, QFrame
from PyQt5.QtCore import Qt, QPoint, QRect
from PyQt5.QtGui import QResizeEvent, QPixmap, QPainter, QMouseEvent, QIcon
from widgets.window import IconLabel, TitleLabel, TitleButton, T_HEIGHT, T_B_WIDTH, I_WIDTH
from configs.resource import *

F_WIDTH = 5
PADDING = 5


class QUnFrameWindow(QWidget):
    def __init__(self):
        super(QUnFrameWindow, self).__init__(None, Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move_drag_position = 0
        self._move_drag = self._corner_drag = self._bottom_drag = self._right_drag = False
        self._right_rect = self._bottom_rect = self._corner_rect = []

        icon_label = IconLabel(self)
        icon_label.setObjectName('Icon')
        icon_label.setMouseTracking(True)
        icon_label.move(F_WIDTH + 1, F_WIDTH)
        self.setWindowIcon = self._set_icon(self.setWindowIcon)

        title_label = TitleLabel(self)
        title_label.setObjectName('Title')
        title_label.setMouseTracking(True)
        title_label.move(I_WIDTH + F_WIDTH + 1, F_WIDTH)
        self.setWindowTitle = self._set_title(self.setWindowTitle)

        min_button = TitleButton(b'\xef\x80\xb0'.decode('utf-8'), self)
        min_button.setWhatsThis('MinMaxButton')
        min_button.setObjectName('MinButton')
        min_button.setToolTip('最小化')
        min_button.setMouseTracking(True)
        min_button.setFixedHeight(T_HEIGHT)
        min_button.clicked.connect(self.showMinimized)

        max_button = TitleButton(b'\xef\x80\xb1'.decode('utf-8'), self)
        max_button.setWhatsThis('MinMaxButton')
        max_button.setObjectName('MaxButton')
        max_button.setToolTip('最大化')
        max_button.setMouseTracking(True)
        max_button.setFixedHeight(T_HEIGHT)
        max_button.clicked.connect(self.charge_button)

        close_button = TitleButton(b'\xef\x81\xb2'.decode('utf-8'), self)
        close_button.setWhatsThis('CloseButton')
        close_button.setObjectName('CloseButton')
        close_button.setToolTip('关闭窗口')
        close_button.setMouseTracking(True)
        close_button.setFixedHeight(T_HEIGHT)
        close_button.clicked.connect(self.close)

        dummy_label = TitleLabel()
        dummy_label.setObjectName('Dummy')

        main_layout = QVBoxLayout()
        main_layout.setSpacing(0)
        main_layout.addWidget(dummy_label, alignment=Qt.AlignCenter)
        main_layout.addStretch()

        self.setLayout(main_layout)

        self.setMinimumSize(320, 240)
        self.setMouseTracking(True)

    def centralWidget(self):
        return self._centralWidget

    def setCentralWidget(self, widget):
        if self._centralWidget:
            self._centralWidget.close()

    def _set_title(self, func):
        def wrapper(*args):
            self.findChild(TitleLabel, 'Title').setText(*args)
            return func(*args)

        return wrapper

    def _set_icon(self, func):
        def wrapper(*args):
            self.findChild(IconLabel, 'Icon').set_icon(*args)
            return func(*args)

        return wrapper

    def charge_button(self):
        button: TitleButton = self.findChild(TitleButton, 'MaxButton')
        if button.text() == b'\xef\x80\xb2'.decode('utf-8'):
            self.showNormal()
            button.setText(b'\xef\x80\xb1'.decode('utf-8'))
            button.setToolTip('最大化')
        else:
            self.showMaximized()
            button.setText(b'\xef\x80\xb2'.decode('utf-8'))
            button.setToolTip('恢复')

    def resizeEvent(self, event: QResizeEvent):
        self.findChild(TitleLabel, 'Title').setFixedWidth(self.width() - F_WIDTH * 2 - I_WIDTH)
        self._right_rect = [QPoint(x, y) for x in range(self.width() - PADDING, self.width() + 1)
                            for y in range(1, self.height() - PADDING)]
        self._bottom_rect = [QPoint(x, y) for x in range(1, self.width() - PADDING)
                             for y in range(self.height() - PADDING, self.height() + 1)]
        self._corner_rect = [QPoint(x, y) for x in range(self.width() - PADDING, self.width() + 1)
                             for y in range(self.height() - PADDING, self.height() + 1)]

        self.findChild(TitleButton, 'CloseButton').move(self.width() - T_B_WIDTH - F_WIDTH + 1, F_WIDTH)
        self.findChild(TitleButton, 'MinButton').move(self.width() - (T_B_WIDTH + 1) * 3 - F_WIDTH + 2, F_WIDTH)
        self.findChild(TitleButton, 'MaxButton').move(self.width() - (T_B_WIDTH + 1) * 2 - F_WIDTH + 2, F_WIDTH)

    def mousePressEvent(self, event: QMouseEvent):
        if (event.button() == Qt.LeftButton) and (event.pos() in self._corner_rect):
            self._corner_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._right_rect):
            self._right_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.pos() in self._bottom_rect):
            self._bottom_drag = True
            event.accept()
        elif (event.button() == Qt.LeftButton) and (event.y() < T_HEIGHT + F_WIDTH - 1):
            self._move_drag = True
            self.move_drag_position = event.globalPos() - self.pos()
            event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if event.pos() in self._corner_rect:
            self.setCursor(Qt.SizeFDiagCursor)
        elif event.pos() in self._bottom_rect:
            self.setCursor(Qt.SizeVerCursor)
        elif event.pos() in self._right_rect:
            self.setCursor(Qt.SizeHorCursor)
        else:
            self.setCursor(Qt.ArrowCursor)
        if Qt.LeftButton and self._right_drag:
            self.resize(event.pos().x(), self.height())
            event.accept()
        elif Qt.LeftButton and self._bottom_drag:
            self.resize(self.width(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._corner_drag:
            self.resize(event.pos().x(), event.pos().y())
            event.accept()
        elif Qt.LeftButton and self._move_drag:
            self.move(event.globalPos() - self.move_drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        self._move_drag = self._corner_drag = self._bottom_drag = self._right_drag = False

    def drawShadow(self, painter):
        borders = [':frame/frame-left-top.png', ':frame/frame-left-bottom.png', ':frame/frame-right-top.png',
                   ':frame/frame-right-bottom.png', ':frame/frame-top.png', ':frame/frame-bottom.png',
                   ':frame/frame-left.png', ':frame/frame-right.png']

        painter.drawPixmap(0, 0, F_WIDTH, F_WIDTH,
                           QPixmap(borders[0]))
        painter.drawPixmap(self.width() - F_WIDTH, 0, F_WIDTH, F_WIDTH,
                           QPixmap(borders[2]))
        painter.drawPixmap(0, self.height() - F_WIDTH, F_WIDTH, F_WIDTH,
                           QPixmap(borders[1]))
        painter.drawPixmap(self.width() - F_WIDTH, self.height() - F_WIDTH, F_WIDTH, F_WIDTH,
                           QPixmap(borders[3]))
        painter.drawPixmap(0, F_WIDTH, F_WIDTH, self.height() - 2 * F_WIDTH,
                           QPixmap(borders[6]).scaled(F_WIDTH, self.height() - 2 * F_WIDTH))
        painter.drawPixmap(self.width() - F_WIDTH, F_WIDTH, F_WIDTH, self.height() - 2 * F_WIDTH,
                           QPixmap(borders[7]).scaled(F_WIDTH, self.height() - 2 * F_WIDTH))
        painter.drawPixmap(F_WIDTH, 0, self.width() - 2 * F_WIDTH, F_WIDTH,
                           QPixmap(borders[4]).scaled(self.width() - 2 * F_WIDTH, F_WIDTH))
        painter.drawPixmap(F_WIDTH, self.height() - F_WIDTH, self.width() - 2 * F_WIDTH, F_WIDTH,
                           QPixmap(borders[5]).scaled(self.width() - 2 * F_WIDTH, F_WIDTH))

    def paintEvent(self, event):
        painter = QPainter(self)
        self.drawShadow(painter)
        painter.setPen(Qt.NoPen)
        painter.setBrush(Qt.white)
        rect = QRect(F_WIDTH, F_WIDTH, self.width() - 2 * F_WIDTH, self.height() - 2 * F_WIDTH)
        painter.drawRect(rect)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyleSheet("""
    TitleLabel {
    background-color: rgba(200,200,200,50);
    font-family: 'Microsoft YaHei UI', '微软雅黑', monospace;
    }
    TitleLabel#Dummy {
    background-color: rgba(0,0,0,0);
    }
    TitleButton{
    background-color: rgba(0, 0, 0, 0);
    color: black;
    border: 0px;
    font-family: 'Webdings';
    }
    TitleButton#MinButton:hover{
    background-color: #D0D0D1;
    }
    TitleButton#MaxButton:hover{
    background-color: #D0D0D1;
    }
    TitleButton#CloseButton:hover{
    background-color: #D32424;
    color: white;
    }
    """)
    w = QUnFrameWindow()
    w.setWindowTitle('三国志DS Rom编辑器')
    w.setWindowIcon(QIcon(r':icon/icon.png'))
    w.show()
    sys.exit(app.exec_())
