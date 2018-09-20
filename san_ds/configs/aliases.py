#!/usr/bin/env python
# -*- coding: utf-8 -*-

CODE_ALIASES = 'shiftjisx0213'

DECODE_MAPPING = {
    'Д': '浚',
    '①': '璿',
    '𠂉': '瓚',
    '丒': '郃',
    '丩': '蒯',
    '丮': '傕',
    '乀': '邕',
    '么': '詡',
    '乑': '兗',
    '㐆': '龐',
    '𠂤': '繇',
    '乚': '邈',
    '乩': '騭',
    '㐬': '闞',
    '㐮': '玠',
    '亻': '邢',
    '𠆢': '歆',
    '亼': '闓',
    '仈': '譙',
    '仐': '琬',
    '仫': '郝',
    '仱': '伷',
    '仵': '褚',
    '佤': '邳',
    '𠈓': '璝',
    '佸': '彤',
    '侂': '涪',
    '侚': '鄴',
    '侾': '鄱',
    '俅': '莒',
    '俋': '綝',
    '倀': '笮',
    '倐': '祜',
    '倓': '蕤',
    '倜': '璜',
    '㑨': '瓘',
    '偂': '靚',
    '偆': '琰',
    '偎': '頎',
    '偣': '龔',
    '偦': '眭',
    '傈': '嘏',
    '𠌫': '宓',
    '傱': '珝',
    '傺': '禕',
    '僳': '寗',
    '𠎁': '蹋',
    '踖': '昱',
    '鄷': '彧',
    '酴': '惲',
    '釬': '昕',
    '鉂': '晙',
    '鋐': '汜',
    '鐗': '琦',
    '鏻': '琪',
    '鐴': '琮',
    '鑭': '畯',
    '韑': '諶',
    '頳': '鄧',
    '颫': '釭',
    '𩣆': '顗',
    '\x00': '',
    # 'ｶﾞ': 'ガ',
    # 'ｷﾞ': 'ギ',
    # 'ｸﾞ': 'グ',
    # 'ｹﾞ': 'ゲ',
    # 'ｺﾞ': 'ゴ',
    # 'ｻﾞ': 'ザ',
    # 'ｼﾞ': 'ジ',
    # 'ｽﾞ': 'ズ',
    # 'ｾﾞ': 'ゼ',
    # 'ｿﾞ': 'ゾ',
    # 'ﾀﾞ': 'ダ',
    # 'ﾁﾞ': 'ヂ',
    # 'ﾂﾞ': 'ヅ',
    # 'ﾃﾞ': 'デ',
    # 'ﾄﾞ': 'ド',
    # 'ﾊﾞ': 'バ',
    # 'ﾊﾟ': 'パ',
    # 'ﾋﾞ': 'ビ',
    # 'ﾋﾟ': 'ピ',
    # 'ﾌﾞ': 'ブ',
    # 'ﾌﾟ': 'プ',
    # 'ﾍﾞ': 'ベ',
    # 'ﾍﾟ': 'ペ',
    # 'ﾎﾞ': 'ボ',
    # 'ﾎﾟ': 'ポ',
    # 'ｳﾞ': 'ヴ',
    # 'ｧ': 'ァ',
    # 'ｱ': 'ア',
    # 'ｨ': 'ィ',
    # 'ｲ': 'イ',
    # 'ｩ': 'ゥ',
    # 'ｳ': 'ウ',
    # 'ｪ': 'ェ',
    # 'ｴ': 'エ',
    # 'ｫ': 'ォ',
    # 'ｵ': 'オ',
    # 'ｶ': 'カ',
    # 'ｷ': 'キ',
    # 'ｸ': 'ク',
    # 'ｹ': 'ケ',
    # 'ｺ': 'コ',
    # 'ｻ': 'サ',
    # 'ｼ': 'シ',
    # 'ｽ': 'ス',
    # 'ｾ': 'セ',
    # 'ｿ': 'ソ',
    # 'ﾀ': 'タ',
    # 'ﾁ': 'チ',
    # 'ｯ': 'ッ',
    # 'ﾂ': 'ツ',
    # 'ﾃ': 'テ',
    # 'ﾄ': 'ト',
    # 'ﾅ': 'ナ',
    # 'ﾆ': 'ニ',
    # 'ﾇ': 'ヌ',
    # 'ﾈ': 'ネ',
    # 'ﾉ': 'ノ',
    # 'ﾊ': 'ハ',
    # 'ﾋ': 'ヒ',
    # 'ﾌ': 'フ',
    # 'ﾍ': 'ヘ',
    # 'ﾎ': 'ホ',
    # 'ﾏ': 'マ',
    # 'ﾐ': 'ミ',
    # 'ﾑ': 'ム',
    # 'ﾒ': 'メ',
    # 'ﾓ': 'モ',
    # 'ｬ': 'ャ',
    # 'ﾔ': 'ヤ',
    # 'ｭ': 'ュ',
    # 'ﾕ': 'ユ',
    # 'ｮ': 'ョ',
    # 'ﾖ': 'ヨ',
    # 'ﾗ': 'ラ',
    # 'ﾘ': 'リ',
    # 'ﾙ': 'ル',
    # 'ﾚ': 'レ',
    # 'ﾛ': 'ロ',
    # 'ﾜ': 'ヮ',
    # 'ｦ': 'ヲ',
    # 'ﾝ': 'ン',
}

ENCODE_MAPPING = {
    '浚': 'Д',
    '璿': '①',
    '瓚': '𠂉',
    '郃': '丒',
    '蒯': '丩',
    '傕': '丮',
    '邕': '乀',
    '詡': '么',
    '兗': '乑',
    '龐': '㐆',
    '繇': '𠂤',
    '邈': '乚',
    '騭': '乩',
    '闞': '㐬',
    '玠': '㐮',
    '邢': '亻',
    '歆': '𠆢',
    '闓': '亼',
    '譙': '仈',
    '琬': '仐',
    '郝': '仫',
    '伷': '仱',
    '褚': '仵',
    '邳': '佤',
    '璝': '𠈓',
    '彤': '佸',
    '涪': '侂',
    '鄴': '侚',
    '鄱': '侾',
    '莒': '俅',
    '綝': '俋',
    '笮': '倀',
    '祜': '倐',
    '蕤': '倓',
    '璜': '倜',
    '瓘': '㑨',
    '靚': '偂',
    '琰': '偆',
    '頎': '偎',
    '龔': '偣',
    '眭': '偦',
    '嘏': '傈',
    '宓': '𠌫',
    '珝': '傱',
    '禕': '傺',
    '寗': '僳',
    '蹋': '𠎁',
    '昱': '踖',
    '彧': '鄷',
    '惲': '酴',
    '昕': '釬',
    '晙': '鉂',
    '汜': '鋐',
    '琦': '鐗',
    '琪': '鏻',
    '琮': '鐴',
    '畯': '鑭',
    '諶': '韑',
    '鄧': '頳',
    '釭': '颫',
    '顗': '𩣆',
    # 'ガ': 'ｶﾞ',
    # 'ギ': 'ｷﾞ',
    # 'グ': 'ｸﾞ',
    # 'ゲ': 'ｹﾞ',
    # 'ゴ': 'ｺﾞ',
    # 'ザ': 'ｻﾞ',
    # 'ジ': 'ｼﾞ',
    # 'ズ': 'ｽﾞ',
    # 'ゼ': 'ｾﾞ',
    # 'ゾ': 'ｿﾞ',
    # 'ダ': 'ﾀﾞ',
    # 'ヂ': 'ﾁﾞ',
    # 'ヅ': 'ﾂﾞ',
    # 'デ': 'ﾃﾞ',
    # 'ド': 'ﾄﾞ',
    # 'バ': 'ﾊﾞ',
    # 'パ': 'ﾊﾟ',
    # 'ビ': 'ﾋﾞ',
    # 'ピ': 'ﾋﾟ',
    # 'ブ': 'ﾌﾞ',
    # 'プ': 'ﾌﾟ',
    # 'ベ': 'ﾍﾞ',
    # 'ペ': 'ﾍﾟ',
    # 'ボ': 'ﾎﾞ',
    # 'ポ': 'ﾎﾟ',
    # 'ヴ': 'ｳﾞ',
    # 'ァ': 'ｧ',
    # 'ア': 'ｱ',
    # 'ィ': 'ｨ',
    # 'イ': 'ｲ',
    # 'ゥ': 'ｩ',
    # 'ウ': 'ｳ',
    # 'ェ': 'ｪ',
    # 'エ': 'ｴ',
    # 'ォ': 'ｫ',
    # 'オ': 'ｵ',
    # 'カ': 'ｶ',
    # 'キ': 'ｷ',
    # 'ク': 'ｸ',
    # 'ケ': 'ｹ',
    # 'コ': 'ｺ',
    # 'サ': 'ｻ',
    # 'シ': 'ｼ',
    # 'ス': 'ｽ',
    # 'セ': 'ｾ',
    # 'ソ': 'ｿ',
    # 'タ': 'ﾀ',
    # 'チ': 'ﾁ',
    # 'ッ': 'ｯ',
    # 'ツ': 'ﾂ',
    # 'テ': 'ﾃ',
    # 'ト': 'ﾄ',
    # 'ナ': 'ﾅ',
    # 'ニ': 'ﾆ',
    # 'ヌ': 'ﾇ',
    # 'ネ': 'ﾈ',
    # 'ノ': 'ﾉ',
    # 'ハ': 'ﾊ',
    # 'ヒ': 'ﾋ',
    # 'フ': 'ﾌ',
    # 'ヘ': 'ﾍ',
    # 'ホ': 'ﾎ',
    # 'マ': 'ﾏ',
    # 'ミ': 'ﾐ',
    # 'ム': 'ﾑ',
    # 'メ': 'ﾒ',
    # 'モ': 'ﾓ',
    # 'ャ': 'ｬ',
    # 'ヤ': 'ﾔ',
    # 'ュ': 'ｭ',
    # 'ユ': 'ﾕ',
    # 'ョ': 'ｮ',
    # 'ヨ': 'ﾖ',
    # 'ラ': 'ﾗ',
    # 'リ': 'ﾘ',
    # 'ル': 'ﾙ',
    # 'レ': 'ﾚ',
    # 'ロ': 'ﾛ',
    # 'ヮ': 'ﾜ',
    # 'ワ': 'ﾜ',
    # 'ヰ': 'ｲ',
    # 'ヱ': 'ｴ',
    # 'ヲ': 'ｦ',
    # 'ン': 'ﾝ',
}

EXPAND_CHARACTER = ''.join(ENCODE_MAPPING)
