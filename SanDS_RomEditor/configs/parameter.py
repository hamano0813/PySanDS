#!/usr/bin/env python
# -*- coding: utf-8 -*-


DATA_PARAMETER = {
    '武將屬性_姓名': {
        'address': {'normal_offset': 0x001108B3},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_讀音': {
        'address': {'normal_offset': 0x001108BC},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_野望': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武將屬性_幸運': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武將屬性_冷靜': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武將屬性_勇猛': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武將屬性_壽命': {
        'address': {'normal_offset': 0x001108A8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 7)},
    '武將屬性_陸指': {
        'address': {'normal_offset': 0x001108A9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_水指': {
        'address': {'normal_offset': 0x001108AA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_武力': {
        'address': {'normal_offset': 0x001108AB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_智力': {
        'address': {'normal_offset': 0x001108AC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_政治': {
        'address': {'normal_offset': 0x001108AD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_魅力': {
        'address': {'normal_offset': 0x001108AE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_相性': {
        'address': {'normal_offset': 0x001108AF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_義理': {
        'address': {'normal_offset': 0x001108B0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_家族': {
        'address': {'normal_offset': 0x001108B1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武將屬性_生年': {
        'address': {'normal_offset': 0x001108B2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},

    'NPC屬性_姓名': {
        'address': {'normal_offset': 0x0011A530, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0xA},
        'record': 0x4},

    '武將登場_登場年': {
        'address': {'normal_offset': 0x001291F8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_血緣': {
        'address': {'normal_offset': 0x001291FA},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_兵数': {
        'address': {'normal_offset': 0x0010F09C},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_身份': {
        'address': {'normal_offset': 0x0010F09D},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_忠誠': {
        'address': {'normal_offset': 0x0010F09E},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_所在都市': {
        'address': {'normal_offset': 0x0010F09F},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武將登場_登場都市': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},
    '武將登場_未登場武將': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFBFFE},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},

    '武將戰技_戰鬥系': {
        'address': {'normal_offset': 0x01D5D8D1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_不意': {
        'address': {'normal_offset': 0x01D5D8D2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_突擊': {
        'address': {'normal_offset': 0x01D5D8D3},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_牽制': {
        'address': {'normal_offset': 0x01D5D8D4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_一騎': {
        'address': {'normal_offset': 0x01D5D8D5},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_受流': {
        'address': {'normal_offset': 0x01D5D8D6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_彈返': {
        'address': {'normal_offset': 0x01D5D8D7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_單騎': {
        'address': {'normal_offset': 0x01D5D8D8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_騎突': {
        'address': {'normal_offset': 0x01D5D8D9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_用兵系': {
        'address': {'normal_offset': 0x01D5D8DA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_壁越': {
        'address': {'normal_offset': 0x01D5D8DB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_威嚇': {
        'address': {'normal_offset': 0x01D5D8DC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_一齊': {
        'address': {'normal_offset': 0x01D5D8DD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_齊射': {
        'address': {'normal_offset': 0x01D5D8DE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_門射': {
        'address': {'normal_offset': 0x01D5D8DF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_火矢': {
        'address': {'normal_offset': 0x01D5D8E0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_狙擊': {
        'address': {'normal_offset': 0x01D5D8E1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_連弩': {
        'address': {'normal_offset': 0x01D5D8E2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_軍學系': {
        'address': {'normal_offset': 0x01D5D8E3},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_鎮火': {
        'address': {'normal_offset': 0x01D5D8E4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_火計': {
        'address': {'normal_offset': 0x01D5D8E5},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_伏兵': {
        'address': {'normal_offset': 0x01D5D8E6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_偽令': {
        'address': {'normal_offset': 0x01D5D8E7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_同討': {
        'address': {'normal_offset': 0x01D5D8E8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_論破': {
        'address': {'normal_offset': 0x01D5D8E9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_落穴': {
        'address': {'normal_offset': 0x01D5D8EA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_大火': {
        'address': {'normal_offset': 0x01D5D8EB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_掌握系': {
        'address': {'normal_offset': 0x01D5D8EC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_挑發': {
        'address': {'normal_offset': 0x01D5D8ED},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_說得': {
        'address': {'normal_offset': 0x01D5D8EE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_治療': {
        'address': {'normal_offset': 0x01D5D8EF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_鼓舞': {
        'address': {'normal_offset': 0x01D5D8F0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_誘引': {
        'address': {'normal_offset': 0x01D5D8F1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_祈禱': {
        'address': {'normal_offset': 0x01D5D8F2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_衝車': {
        'address': {'normal_offset': 0x01D5D8F3},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},
    '武將戰技_生存': {
        'address': {'normal_offset': 0x01D5D8F4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x24},

    '都市屬性_都市名': {
        'address': {'normal_offset': 0x0011B15A},
        'length': {'normal_length': 0x6},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},
    '都市屬性_讀音': {
        'address': {'normal_offset': 0x0011B163},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},
    '都市屬性_次都市': {
        'address': {'normal_offset': 0x0011D4E0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_軍師': {
        'address': {'normal_offset': 0x0011D4E2},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_港口': {
        'address': {'normal_offset': 0x0011D4EA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20,
        'bit': (7, 8)},
    '都市屬性_商人': {
        'address': {'normal_offset': 0x0011D4EB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20,
        'bit': (4, 5)},
    '都市屬性_肥沃度': {
        'address': {'normal_offset': 0x0011D4EA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20,
        'bit': (0, 4)},
    '都市屬性_人口': {
        'address': {'normal_offset': 0x0011D4E4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_金': {
        'address': {'normal_offset': 0x0011D4E6},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_兵糧': {
        'address': {'normal_offset': 0x0011D4E8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_開発': {
        'address': {'normal_offset': 0x0011D4ED},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_灌漑': {
        'address': {'normal_offset': 0x0011D4EE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_治水': {
        'address': {'normal_offset': 0x0011D4EF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_商業': {
        'address': {'normal_offset': 0x0011D4F0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_税率': {
        'address': {'normal_offset': 0x0011D4F2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_民忠': {
        'address': {'normal_offset': 0x0011D4F3},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_弩': {
        'address': {'normal_offset': 0x0011D4F4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_強弩': {
        'address': {'normal_offset': 0x0011D4F6},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_軍馬': {
        'address': {'normal_offset': 0x0011D4F8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_闘艦': {
        'address': {'normal_offset': 0x0011D4FA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_蒙衝': {
        'address': {'normal_offset': 0x0011D4FB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_走舸': {
        'address': {'normal_offset': 0x0011D4FC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_訓練': {
        'address': {'normal_offset': 0x0011D4FD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '都市屬性_士気': {
        'address': {'normal_offset': 0x0011D4FE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x20},
    '戰場屬性_戰場名': {
        'address': {'normal_offset': 0x00126F62},
        'length': {'normal_length': 0x6},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},
    '戰場屬性_讀音': {
        'address': {'normal_offset': 0x00126F69},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},
    '戰場屬性_劇本1': {
        'address': {'normal_offset': 0x00126EBC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本2': {
        'address': {'normal_offset': 0x00126EBD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本3': {
        'address': {'normal_offset': 0x00126EBE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本4': {
        'address': {'normal_offset': 0x00126EBF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本5': {
        'address': {'normal_offset': 0x00126EC0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本6': {
        'address': {'normal_offset': 0x00126EC1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},
    '戰場屬性_劇本7': {
        'address': {'normal_offset': 0x00126EC2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x7},

    '劇本屬性_劇本標題': {
        'address': {'normal_offset': 0x0012B0E8, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x20},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x4},
    '劇本屬性_劇本名': {
        'address': {'normal_offset': 0x000FBC34, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x1B},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x4},
    '劇本屬性_劇本年': {
        'address': {'normal_offset': 0x000FC150},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x2},
    '劇本屬性_開始年': {
        'address': {'normal_offset': 0x001275B8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x22},
    '劇本屬性_開始月': {
        'address': {'normal_offset': 0x001275BA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x22},
    '劇本屬性_勢力數': {
        'address': {'normal_offset': 0x000FBCCC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x1},
    '劇本屬性_旗幟數': {
        'address': {'normal_offset': 0x001275BB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x22},
    '劇本屬性_玩家數': {
        'address': {'normal_offset': 0x000FBCD4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x1},
    '劇本屬性_獻帝位置': {
        'address': {'normal_offset': 0x00120240},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x1},

    '文本_人物列傳': {
        'address': {'normal_offset': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'length': {'normal_length': 148, 'main_pointer': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'quantity': {'normal_quantity': 0x30C},
        'record': 0x4},
    '文本_效果描述': {
        'address': {'normal_offset': 0x0002F6EC, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0002F6EC, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x4},
    '文本_物品名稱': {
        'address': {'normal_offset': 0x0017D15C, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0017D15C, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x14},
    '文本_物品讀音': {
        'address': {'normal_offset': 0x0017D160, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0017D160, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x14},
    '文本_物品類別': {
        'address': {'normal_offset': 0x0017D164, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0017D164, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x14},
    '文本_物品能力': {
        'address': {'normal_offset': 0x0017D168, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0017D168, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x14},
    '文本_物品描述': {
        'address': {'normal_offset': 0x0017D16C, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0017D16C, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x14},

    '物品屬性_物品': {
        'address': {'normal_offset': 0x0011AC99},
        'length': {'normal_length': 0xC},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '物品屬性_忠誠上昇': {
        'address': {'normal_offset': 0x0011AC96},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '物品屬性_效果1': {
        'address': {'normal_offset': 0x0011AC97},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '物品屬性_效果2': {
        'address': {'normal_offset': 0x0011AC98},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '道具歸屬_劇本1': {
        'address': {'normal_offset': 0x0011E060},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本2': {
        'address': {'normal_offset': 0x0011E062},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本3': {
        'address': {'normal_offset': 0x0011E064},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本4': {
        'address': {'normal_offset': 0x0011E066},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本5': {
        'address': {'normal_offset': 0x0011E068},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本6': {
        'address': {'normal_offset': 0x0011E06A},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具歸屬_劇本7': {
        'address': {'normal_offset': 0x0011E06C},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},

    '特產屬性_種類': {
        'address': {'normal_offset': 0x0011A5C0, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0011A5C0, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x4},
    '特產屬性_武力': {
        'address': {'normal_offset': 0x000E88A8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_智力': {
        'address': {'normal_offset': 0x000E88A4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_政治': {
        'address': {'normal_offset': 0x000E88B0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_魅力': {
        'address': {'normal_offset': 0x000E88AC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_陸指': {
        'address': {'normal_offset': 0x000E88C4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_水指': {
        'address': {'normal_offset': 0x000E88C8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_壽命': {
        'address': {'normal_offset': 0x000E88F0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_義理': {
        'address': {'normal_offset': 0x000E88CC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_野望': {
        'address': {'normal_offset': 0x000E88D4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_幸運': {
        'address': {'normal_offset': 0x000E88D0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_冷靜': {
        'address': {'normal_offset': 0x000E88D8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_勇猛': {
        'address': {'normal_offset': 0x000E88DC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_機動力': {
        'address': {'normal_offset': 0x000E88EC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特產屬性_安全撤退': {
        'address': {'normal_offset': 0x000E88F4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},

    '劇本勢力_紋章': {
        'address': {'normal_offset': 0x001275BC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1},
    '劇本勢力_君主': {
        'address': {'normal_offset': 0x0012ACA2},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_首都': {
        'address': {'normal_offset': 0x0012ACA4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對01': {
        'address': {'normal_offset': 0x0012ACA6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對02': {
        'address': {'normal_offset': 0x0012ACA7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對03': {
        'address': {'normal_offset': 0x0012ACA8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對04': {
        'address': {'normal_offset': 0x0012ACA9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對05': {
        'address': {'normal_offset': 0x0012ACAA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對06': {
        'address': {'normal_offset': 0x0012ACAB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對07': {
        'address': {'normal_offset': 0x0012ACAC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對08': {
        'address': {'normal_offset': 0x0012ACAD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對09': {
        'address': {'normal_offset': 0x0012ACAE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對10': {
        'address': {'normal_offset': 0x0012ACAF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對11': {
        'address': {'normal_offset': 0x0012ACB0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對12': {
        'address': {'normal_offset': 0x0012ACB1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對13': {
        'address': {'normal_offset': 0x0012ACB2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對14': {
        'address': {'normal_offset': 0x0012ACB3},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對15': {
        'address': {'normal_offset': 0x0012ACB4},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對16': {
        'address': {'normal_offset': 0x0012ACB5},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對17': {
        'address': {'normal_offset': 0x0012ACB6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對18': {
        'address': {'normal_offset': 0x0012ACB7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對19': {
        'address': {'normal_offset': 0x0012ACB8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對20': {
        'address': {'normal_offset': 0x0012ACB9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},
    '劇本勢力_敵對21': {
        'address': {'normal_offset': 0x0012ACBA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x15},
        'record': 0x1A},

    '圖片_頭像圖片': {
        'address': {'normal_offset': 0x00A479E8},
        'size': (56, 64),
        'quantity': {'normal_quantity': 0x35D},
        'record': 0xE04,
        'palette': {'normal_offset': 0x009DB274}},
    '圖片_道具圖片': {
        'address': {'normal_offset': 0x019D3842},
        'size': (64, 64),
        'quantity': {'normal_quantity': 0x43},
        'record': 0x1208},
    '圖片_LOGO': {
        'address': {'normal_offset': 0x007AA364},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_主背景': {
        'address': {'normal_offset': 0x007C2F78},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_主操作按鈕': {
        'address': {'normal_offset': 0x007D9048},
        'size': (256, 208),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_遊戲人數按鈕': {
        'address': {'normal_offset': 0x008676A8},
        'size': (232, 232),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_君主能力背景': {
        'address': {'normal_offset': 0x008812FC},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_勢力選擇紋章': {
        'address': {'normal_offset': 0x0088D504},
        'size': (232, 40),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_劇本確認背景': {
        'address': {'normal_offset': 0x008A26EC},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_劇本設置素材': {
        'address': {'normal_offset': 0x008AE8F4},
        'size': (256, 176),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_地圖移動素材': {
        'address': {'normal_offset': 0x00917144},
        'size': (256, 56),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_都市信息背景': {
        'address': {'normal_offset': 0x0099C244},
        'size': (256, 216),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_經典能力背景': {
        'address': {'normal_offset': 0x009AA250},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_放浪勢力背景': {
        'address': {'normal_offset': 0x009C2660},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_戰爭信息背景': {
        'address': {'normal_offset': 0x009CE868},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_對話框素材': {
        'address': {'normal_offset': 0x00D45F64},
        'size': (256, 80),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_出戰信息背景': {
        'address': {'normal_offset': 0x00F43D88},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_外交界面背景': {
        'address': {'normal_offset': 0x00F8EBD8},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_進度報告背景': {
        'address': {'normal_offset': 0x00FA6DE8},
        'size': (256, 160),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_終止按鈕': {
        'address': {'normal_offset': 0x00FAE7F0},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_勢力一覽背景': {
        'address': {'normal_offset': 0x00FB01F8},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_勢力一覽紋章': {
        'address': {'normal_offset': 0x00FBC400},
        'size': (256, 80),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_戰鬥信息背景': {
        'address': {'normal_offset': 0x0179C662},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_DS版能力背景': {
        'address': {'normal_offset': 0x017A886A},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_收集模式素材': {
        'address': {'normal_offset': 0x019A801A},
        'size': (256, 224),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_武將一覽背景': {
        'address': {'normal_offset': 0x019C763A},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_對戰模式背景': {
        'address': {'normal_offset': 0x01A27F26},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_对战模式素材': {
        'address': {'normal_offset': 0x01A44336},
        'size': (256, 64),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_登陸武將背景': {
        'address': {'normal_offset': 0x01A5FA7A},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_選擇字符素材': {
        'address': {'normal_offset': 0x01A7C496},
        'size': (256, 144),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_選擇性別素材': {
        'address': {'normal_offset': 0x01A89EA2},
        'size': (256, 72),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_能力分配素材': {
        'address': {'normal_offset': 0x01A8E8AA},
        'size': (256, 80),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_能力變更按鈕': {
        'address': {'normal_offset': 0x01A992B6},
        'size': (256, 48),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_文字輸入素材': {
        'address': {'normal_offset': 0x01A6BC82},
        'size': (256, 256),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0},
    '圖片_大地圖背景': {
        'address': {'normal_offset': 0x008CBB08},
        'size': (320, 320),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x008E4B0C}},
    '圖片_主選項': {
        'address': {'normal_offset': 0x007CF180},
        'size': (232, 120),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_列傳選項': {
        'address': {'normal_offset': 0x007E6250},
        'size': (232, 72),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_遊戲模式選項': {
        'address': {'normal_offset': 0x01CF7031},
        'size': (232, 56),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_經典劇本選項': {
        'address': {'normal_offset': 0x008609E4},
        'size': (232, 120),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_挑戰劇本選項': {
        'address': {'normal_offset': 0x01CFF035},
        'size': (232, 120),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_通信對戰選項': {
        'address': {'normal_offset': 0x01A21262},
        'size': (232, 120),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_登陸新武將選項': {
        'address': {'normal_offset': 0x01A5A276},
        'size': (232, 96),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_登陸確認選項': {
        'address': {'normal_offset': 0x01A93AB2},
        'size': (232, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_登陸編輯選項': {
        'address': {'normal_offset': 0x01A9C6C2},
        'size': (232, 56),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x007D5E44}},
    '圖片_地圖紋章素材': {
        'address': {'normal_offset': 0x0090D538},
        'size': (256, 152),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x916D3C}},
    '圖片_勢力菜單': {
        'address': {'normal_offset': 0x009351DC},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x916D3C}},
    '圖片_放浪菜單': {
        'address': {'normal_offset': 0x00F9EDE4},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x916D3C}},
    '圖片_返回按鈕': {
        'address': {'normal_offset': 0x0093D1E0},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_軍事按鈕': {
        'address': {'normal_offset': 0x0093E9E4},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_人事按鈕': {
        'address': {'normal_offset': 0x009469E8},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_外交按鈕': {
        'address': {'normal_offset': 0x0094E9EC},
        'size': (256, 112),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_情報按鈕': {
        'address': {'normal_offset': 0x009559F0},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_開發按鈕': {
        'address': {'normal_offset': 0x0095D9F4},
        'size': (256, 64),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_計略按鈕': {
        'address': {'normal_offset': 0x009619F8},
        'size': (256, 112),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_商人按鈕': {
        'address': {'normal_offset': 0x009689FC},
        'size': (256, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_特別按鈕': {
        'address': {'normal_offset': 0x0096E200},
        'size': (256, 64),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_委任按鈕': {
        'address': {'normal_offset': 0x00972204},
        'size': (256, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_官職按鈕': {
        'address': {'normal_offset': 0x00977A08},
        'size': (256, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_資源按鈕': {
        'address': {'normal_offset': 0x0097D20C},
        'size': (256, 128),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_機能按鈕': {
        'address': {'normal_offset': 0x00985210},
        'size': (256, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_艦船按鈕': {
        'address': {'normal_offset': 0x0098AA14},
        'size': (256, 52),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_確定按鈕': {
        'address': {'normal_offset': 0x0098DE58},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_兵種按鈕': {
        'address': {'normal_offset': 0x0099421C},
        'size': (256, 64),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_說得按鈕': {
        'address': {'normal_offset': 0x00998220},
        'size': (144, 48),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_捕縛按鈕': {
        'address': {'normal_offset': 0x00F9ADE0},
        'size': (256, 64),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x99BA34}},
    '圖片_操作素材1': {
        'address': {'normal_offset': 0x00F1C170},
        'size': (256, 208),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0xF3797C}},
    '圖片_操作素材2': {
        'address': {'normal_offset': 0x00F2A978},
        'size': (256, 208),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0xF3797C}},
    '圖片_數字盤素材': {
        'address': {'normal_offset': 0x00F58F9C},
        'size': (256, 88),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0xF5E7A0}},
    '圖片_外交界面按鈕': {
        'address': {'normal_offset': 0x00F835C8},
        'size': (256, 176),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0xF8E5CC}},
    '圖片_戰鬥指令1': {
        'address': {'normal_offset': 0x017EDB06},
        'size': (256, 40),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令2': {
        'address': {'normal_offset': 0x017F030A},
        'size': (256, 40),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令3': {
        'address': {'normal_offset': 0x017F2B0E},
        'size': (256, 72),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令4': {
        'address': {'normal_offset': 0x017F7312},
        'size': (256, 40),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令5': {
        'address': {'normal_offset': 0x017F9B16},
        'size': (256, 72),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令6': {
        'address': {'normal_offset': 0x017FE31A},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令7': {
        'address': {'normal_offset': 0x017FFB1E},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令8': {
        'address': {'normal_offset': 0x01801322},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令9': {
        'address': {'normal_offset': 0x01802B26},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥指令10': {
        'address': {'normal_offset': 0x0180432A},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_戰鬥按鈕': {
        'address': {'normal_offset': 0x01805B72},
        'size': (256, 24),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x17ED902}},
    '圖片_單挑素材': {
        'address': {'normal_offset': 0x01A3412E},
        'size': (256, 224),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x1A44132}},
    '圖片_通關圖片1': {
        'address': {'normal_offset': 0x01A9FEC6},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x1AAFECE}},
    '圖片_通關圖片2': {
        'address': {'normal_offset': 0x01AB08D6},
        'size': (256, 192),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x1AAFECE}},
}

PALETTE_PARAMETER = {
    '色板_春夏秋冬': (0x8E4B0C, 0x8E4D10, 0x8E4F14, 0x8E5118),
    '色板_選項': (0x7D5E44, 0x893B50),
    '色板_地圖紋章': (0x916D3C, 0x916F40),
    '色板_菜單': (0x99B224, 0x99B428, 0x99B62C, 0x99B830),
    '色板_按鈕': (0x99BA34, 0x99BC38, 0x99BE3C, 0x99C040),
    '色板_數字盤': (0xF5E7A0, 0xF5E9A4, 0xF5EBA8, 0xF5EDAC),
    '色板_外交界面': (0xF8E5CC, 0xF8E7D0, 0xF8E9D4),

}


if __name__ == '__main__':
    print([i for i in DATA_PARAMETER])
