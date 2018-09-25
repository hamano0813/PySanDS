#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into
from PyQt5.QtCore import QRegExp
from attributes import Address, Length, Quantity
from configs import CODE_ALIASES, DECODE_MAPPING, ENCODE_MAPPING, EXPAND_CHARACTER


class Character:
    def __init__(self, parent, address: dict, length: dict, quantity: dict, record: int):
        self.offset = self.start = 0
        self.buffer = parent.buffer
        self.address = Address(**address)
        self.length = Length(**length)
        self.quantity = Quantity(**quantity)
        self.record = record
        char_file = open('./configs/character.txt', 'r', encoding='UTF-8')
        regex_char = char_file.read() + EXPAND_CHARACTER
        char_file.close()
        self.reg_exp = QRegExp(f'[{regex_char}\\n\\r]+')

    def set_offset(self, offset: int):
        self.offset = offset

    def set_start(self, index: int):
        self.start = index

    @property
    def real_quantity(self):
        return self.quantity.normal_quantity - self.start

    def get_data(self, data_index: int):
        if not data_index < self.real_quantity:
            return None
        address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
        length = self.length(self.buffer, self.record * (data_index + self.start) + self.offset)
        fmt = f'{length}s'
        data = unpack_from(fmt, self.buffer, address)[0]
        return self.decode_text(data)

    def set_data(self, data_index: int, text: str):
        if data_index < self.real_quantity:
            temp = ''.join([i if not self.reg_exp.indexIn(i) else '' for i in text])
            data = self.encode_text(temp)
            self.length(self.buffer, self.record * (data_index + self.start) + self.offset, len(data))
            address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
            length = self.length(self.buffer, self.record * (data_index + self.start) + self.offset)
            fmt = f'{length}s'
            pack_into(fmt, self.buffer, address, data[:length])

    @staticmethod
    def decode_text(data: bytes) -> str:
        try:
            return ''.join([DECODE_MAPPING[char] if char in DECODE_MAPPING else char
                            for char in data.replace(b'\r', b'\n').decode(CODE_ALIASES)])
        except UnicodeDecodeError:
            return ''

    @staticmethod
    def encode_text(text: str) -> bytes:
        return ''.join([ENCODE_MAPPING[char] if char in ENCODE_MAPPING else char
                        for char in text]).encode(CODE_ALIASES).replace(b'\n', b'\r')

    def sequence(self) -> list:
        return [f'{i+1:0{len(str(self.real_quantity+1))}d}. {self.get_data(i)}' for i in range(self.real_quantity)]

    def mapping(self) -> dict:
        return {i: f'{i+1:0{len(str(self.real_quantity+1))}d}.{self.get_data(i)}' for i in range(self.real_quantity)}
