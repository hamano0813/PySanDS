#!/usr/bin/env python
# -*- coding: utf-8 -*-


DATA_PARAMETER = {
    '武将属性_姓名': {
        'address': {'normal_offset': 0x001108B3},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_读音': {
        'address': {'normal_offset': 0x001108BC},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_野望': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武将属性_幸运': {
        'address': {'normal_offset': 0x001108A6},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武将属性_冷静': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 8)},
    '武将属性_勇猛': {
        'address': {'normal_offset': 0x001108A7},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (0, 4)},
    '武将属性_寿命': {
        'address': {'normal_offset': 0x001108A8},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28,
        'bit': (4, 7)},
    '武将属性_陆指': {
        'address': {'normal_offset': 0x001108A9},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_水指': {
        'address': {'normal_offset': 0x001108AA},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_武力': {
        'address': {'normal_offset': 0x001108AB},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_智力': {
        'address': {'normal_offset': 0x001108AC},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_政治': {
        'address': {'normal_offset': 0x001108AD},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_魅力': {
        'address': {'normal_offset': 0x001108AE},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_相性': {
        'address': {'normal_offset': 0x001108AF},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_义理': {
        'address': {'normal_offset': 0x001108B0},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_家族': {
        'address': {'normal_offset': 0x001108B1},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},
    '武将属性_生年': {
        'address': {'normal_offset': 0x001108B2},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x302},
        'record': 0x28},

    'NPC属性_姓名': {
        'address': {'normal_offset': 0x0011A530, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0xA},
        'record': 0x4},

    '武将登场_登场年': {
        'address': {'normal_offset': 0x001291F8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_血缘': {
        'address': {'normal_offset': 0x001291FA},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_士兵数': {
        'address': {'normal_offset': 0x0010F09C},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_身份': {
        'address': {'normal_offset': 0x0010F09D},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_忠诚': {
        'address': {'normal_offset': 0x0010F09E},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_都市': {
        'address': {'normal_offset': 0x0010F09F},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x301},
        'record': 0x4},
    '武将登场_登场都市': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},
    '武将登场_未登场武将': {
        'address': {'normal_offset': 0x000FBC50, 'pointer_offset': -0x1FFBFFE},
        'length': {'normal_length': 0x2},
        'quantity': {'main_pointer': 0x000FBC50, 'record_length': 0x4, 'sub_pointer': 0x0017B3C4},
        'record': 0x4},
    '都市属性_名称': {
        'address': {'normal_offset': 0x0011B15A},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},
    '都市属性_读音': {
        'address': {'normal_offset': 0x0011B163},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x2E},
        'record': 0x26},

    '战场属性_名称': {
        'address': {'normal_offset': 0x00126F61},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},
    '战场属性_读音': {
        'address': {'normal_offset': 0x00126F69},
        'length': {'normal_length': 0x8},
        'quantity': {'normal_quantity': 0x16},
        'record': 0x20},

    '剧本属性_剧本名': {
        'address': {'normal_offset': 0x0012B0E8, 'pointer_offset': -0x1FFC000},
        'length': {'normal_length': 0x20},
        'quantity': {'normal_quantity': 0x7},
        'record': 0x4},

    '文本_角色列传': {
        'address': {'normal_offset': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'length': {'normal_length': 148, 'main_pointer': 0x01CB7E1D, 'pointer_offset': 0x00430C00},
        'quantity': {'normal_quantity': 0x30C},
        'record': 0x4},
    '图片_武将头像': {
        'address': {'normal_offset': 0x00A479E8},
        'size': (56, 64),
        'quantity': {'normal_quantity': 0x35D},
        'record': 0xE04,
        'palette': {'normal_offset': 0x009DB274}},

    '物品属性_名称': {
        'address': {'normal_offset': 0x0011AC99},
        'length': {'normal_length': 0xC},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '物品属性_忠诚': {
        'address': {'normal_offset': 0x0011AC96},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0x43},
        'record': 0x12},
    '道具属性_效果1': {
        'address': {'normal_offset': 0x0011AC97},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0xD},
        'record': 0x12},
    '道具属性_效果2': {
        'address': {'normal_offset': 0x0011AC98},
        'length': {'normal_length': 0x1},
        'quantity': {'normal_quantity': 0xD},
        'record': 0x12},
    '道具归属_剧本1': {
        'address': {'normal_offset': 0x0011E060},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本2': {
        'address': {'normal_offset': 0x0011E062},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本3': {
        'address': {'normal_offset': 0x0011E064},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本4': {
        'address': {'normal_offset': 0x0011E066},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本5': {
        'address': {'normal_offset': 0x0011E068},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本6': {
        'address': {'normal_offset': 0x0011E06A},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '道具归属_剧本7': {
        'address': {'normal_offset': 0x0011E06C},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0xD},
        'record': 0xE},
    '特产效果_武力': {
        'address': {'normal_offset': 0x000E88A8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_智力': {
        'address': {'normal_offset': 0x000E88A4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_政治': {
        'address': {'normal_offset': 0x000E88B0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_魅力': {
        'address': {'normal_offset': 0x000E88AC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_陆指': {
        'address': {'normal_offset': 0x000E88C4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_水指': {
        'address': {'normal_offset': 0x000E88C8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_寿命': {
        'address': {'normal_offset': 0x000E88F0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_义理': {
        'address': {'normal_offset': 0x000E88CC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_野望': {
        'address': {'normal_offset': 0x000E88D4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_幸运': {
        'address': {'normal_offset': 0x000E88D0},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_冷静': {
        'address': {'normal_offset': 0x000E88D8},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_勇猛': {
        'address': {'normal_offset': 0x000E88DC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_机动力': {
        'address': {'normal_offset': 0x000E88EC},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
    '特产效果_强制退却': {
        'address': {'normal_offset': 0x000E88F4},
        'length': {'normal_length': 0x2},
        'quantity': {'normal_quantity': 0x36},
        'record': 0x54},
}
