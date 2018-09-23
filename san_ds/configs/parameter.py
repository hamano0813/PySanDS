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

    '都市屬性_都市名': {
        'address': {'normal_offset': 0x0011B15A},
        'length': {'normal_length': 0x8},
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
        'address': {'normal_offset': 0x00126F61},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},
    '戰場屬性_讀音': {
        'address': {'normal_offset': 0x00126F69},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},

    '劇本屬性_劇本名': {
        'address': {'normal_offset': 0x0012B0E8, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x20},
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
        'address': {'normal_offset': 0x001275BB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x22},
    '劇本屬性_玩家數': {
        'address': {'normal_offset': 0x000FBCD4},
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
    '圖片_角色頭像': {
        'address': {'normal_offset': 0x00A479E8},
        'size': (56, 64),
        'quantity': {'normal_quantity': 0x35D},
        'record': 0xE04,
        'palette': {'normal_offset': 0x009DB274}},
    '圖片_紋章1': {
        'address': {'normal_offset': 0x0088D504},
        'size': (232, 40),
        'quantity': {'normal_quantity': 0x1},
        'record': 0x0,
        'palette': {'normal_offset': 0x0088F948}},

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
}
