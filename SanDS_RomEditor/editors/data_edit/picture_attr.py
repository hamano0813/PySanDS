#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt5.QtWidgets import QGridLayout
from widgets.common import *

ICON_PARAMETER = {
    '頭像圖片': None,
    '道具圖片': None,
    'LOGO': None,
    '主背景': None,
    '主操作按鈕': None,
    '遊戲人數按鈕': None,
    '君主能力背景': None,
    '勢力選擇紋章': None,
    '劇本確認背景': None,
    '劇本設置素材': None,
    '地圖移動素材': None,
    '都市信息背景': None,
    '經典能力背景': None,
    '放浪勢力背景': None,
    '戰爭信息背景': None,
    '對話框素材': None,
    '出戰信息背景': None,
    '外交界面背景': None,
    '進度報告背景': None,
    '終止按鈕': None,
    '勢力一覽背景': None,
    '勢力一覽紋章': None,
    '戰鬥信息背景': None,
    'DS版能力背景': None,
    '收集模式素材': None,
    '武將一覽背景': None,
    '對戰模式背景': None,
    '对战模式素材': None,
    '登陸武將背景': None,
    '選擇字符素材': None,
    '選擇性別素材': None,
    '能力分配素材': None,
    '能力變更按鈕': None,
    '文字輸入素材': None,
    '大地圖背景': '春夏秋冬',
    '主選項': '選項',
    '列傳選項': '選項',
    '遊戲模式選項': '選項',
    '經典劇本選項': '選項',
    '挑戰劇本選項': '選項',
    '通信對戰選項': '選項',
    '登陸新武將選項': '選項',
    '登陸確認選項': '選項',
    '登陸編輯選項': '選項',
    '地圖紋章素材': '地圖紋章',
    '勢力菜單': '菜單',
    '放浪菜單': '菜單',
    '返回按鈕': '按鈕',
    '軍事按鈕': '按鈕',
    '人事按鈕': '按鈕',
    '外交按鈕': '按鈕',
    '情報按鈕': '按鈕',
    '開發按鈕': '按鈕',
    '計略按鈕': '按鈕',
    '商人按鈕': '按鈕',
    '特別按鈕': '按鈕',
    '委任按鈕': '按鈕',
    '官職按鈕': '按鈕',
    '資源按鈕': '按鈕',
    '機能按鈕': '按鈕',
    '艦船按鈕': '按鈕',
    '確定按鈕': '按鈕',
    '兵種按鈕': '按鈕',
    '說得按鈕': '按鈕',
    '捕縛按鈕': '按鈕',
    '操作素材1': None,
    '操作素材2': None,
    '數字盤素材': '數字盤',
    '外交界面按鈕': '外交界面',
    '戰鬥指令1': None,
    '戰鬥指令2': None,
    '戰鬥指令3': None,
    '戰鬥指令4': None,
    '戰鬥指令5': None,
    '戰鬥指令6': None,
    '戰鬥指令7': None,
    '戰鬥指令8': None,
    '戰鬥指令9': None,
    '戰鬥指令10': None,
    '戰鬥按鈕': None,
    '單挑素材': None,
    '通關圖片1': None,
    '通關圖片2': None
}


class PictureAttr(BackgroundFrame):
    # noinspection PyArgumentList
    def __init__(self, buffer):
        BackgroundFrame.__init__(self, buffer)
        picture_editor = PictureEditor(self, ICON_PARAMETER)

        layout = QGridLayout()
        layout.setContentsMargins(3, 5, 3, 5)
        layout.addWidget(picture_editor)
        self.setLayout(layout)
