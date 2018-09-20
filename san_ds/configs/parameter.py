#!/usr/bin/env python
# -*- coding: utf-8 -*-


DATA_PARAMETER = {
    '武将データ_名前': {
        'address': {'normal_offset': 0x001108B3},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_読み': {
        'address': {'normal_offset': 0x001108BC},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_野望': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武将データ_幸運': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武将データ_冷静': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武将データ_勇猛': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武将データ_寿命': {
        'address': {'normal_offset': 0x001108A8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 7)},
    '武将データ_陸指': {
        'address': {'normal_offset': 0x001108A9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_水指': {
        'address': {'normal_offset': 0x001108AA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_武力': {
        'address': {'normal_offset': 0x001108AB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_知力': {
        'address': {'normal_offset': 0x001108AC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_政治': {
        'address': {'normal_offset': 0x001108AD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_魅力': {
        'address': {'normal_offset': 0x001108AE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_相性': {
        'address': {'normal_offset': 0x001108AF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_義理': {
        'address': {'normal_offset': 0x001108B0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_家族': {
        'address': {'normal_offset': 0x001108B1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将データ_生年': {
        'address': {'normal_offset': 0x001108B2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},

    'NPCデータ_名前': {
        'address': {'normal_offset': 0x0011A530, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0xA},
        'record': 0x4},

    '武将登場_登場年': {
        'address': {'normal_offset': 0x001291F8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_血縁': {
        'address': {'normal_offset': 0x001291FA},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_兵数': {
        'address': {'normal_offset': 0x0010F09C},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_身份': {
        'address': {'normal_offset': 0x0010F09D},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_忠誠': {
        'address': {'normal_offset': 0x0010F09E},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_所在都市': {
        'address': {'normal_offset': 0x0010F09F},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登場_登場都市': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},
    '武将登場_未登場武将': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFBFFE},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},

    '都市データ_都市名': {
        'address': {'normal_offset': 0x0011B15A},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},
    '都市データ_読み': {
        'address': {'normal_offset': 0x0011B163},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},

    '戦場データ_戦場名': {
        'address': {'normal_offset': 0x00126F61},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},
    '戦場データ_読み': {
        'address': {'normal_offset': 0x00126F69},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},

    'シナリオデータ_シナリオ名': {
        'address': {'normal_offset': 0x0012B0E8, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x20},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x4},

    '文本_キャラ伝記': {
        'address': {'normal_offset': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'length': {'normal_length': 148, 'main_pointer': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'quantity': {'normal_quantity': 0x30C},
        'record': 0x4},
    '図_キャラアバター': {
        'address': {'normal_offset': 0x00A479E8},
        'size': (56, 64),
        'quantity': {'normal_quantity': 0x35D},
        'record': 0xE04,
        'palette': {'normal_offset': 0x009DB274}},

    'アイテムデータ_アイテム': {
        'address': {'normal_offset': 0x0011AC99},
        'length': {'normal_length': 0xC},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    'アイテムデータ_忠誠上昇': {
        'address': {'normal_offset': 0x0011AC96},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    'アイテムデータ_効果１': {
        'address': {'normal_offset': 0x0011AC97},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    'アイテムデータ_効果２': {
        'address': {'normal_offset': 0x0011AC98},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '基本アイテム_シナリオ１': {
        'address': {'normal_offset': 0x0011E060},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ２': {
        'address': {'normal_offset': 0x0011E062},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ３': {
        'address': {'normal_offset': 0x0011E064},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ４': {
        'address': {'normal_offset': 0x0011E066},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ５': {
        'address': {'normal_offset': 0x0011E068},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ６': {
        'address': {'normal_offset': 0x0011E06A},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '基本アイテム_シナリオ７': {
        'address': {'normal_offset': 0x0011E06C},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '特産アイテム_効果文本': {
        'address': {'normal_offset': 0x0002F6EC, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0002F6EC, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x4},
    '特産アイテム_種類': {
        'address': {'normal_offset': 0x0011A5C0, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': None, 'main_pointer': 0x0011A5C0, 'pointer_offset': -0x1FFC000},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x4},
    '特産アイテム_武力': {
        'address': {'normal_offset': 0x000E88A8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_知力': {
        'address': {'normal_offset': 0x000E88A4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_政治': {
        'address': {'normal_offset': 0x000E88B0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_魅力': {
        'address': {'normal_offset': 0x000E88AC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_陸指': {
        'address': {'normal_offset': 0x000E88C4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_水指': {
        'address': {'normal_offset': 0x000E88C8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_寿命': {
        'address': {'normal_offset': 0x000E88F0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_義理': {
        'address': {'normal_offset': 0x000E88CC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_野望': {
        'address': {'normal_offset': 0x000E88D4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_幸運': {
        'address': {'normal_offset': 0x000E88D0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_冷静': {
        'address': {'normal_offset': 0x000E88D8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_勇猛': {
        'address': {'normal_offset': 0x000E88DC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_機動力': {
        'address': {'normal_offset': 0x000E88EC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特産アイテム_退却確実': {
        'address': {'normal_offset': 0x000E88F4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
}
