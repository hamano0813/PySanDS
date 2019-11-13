#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into
from attributes import Address, Length, Quantity


class Numerical:
    offset = start = 0
    length_format = {0x1: 'B', 0x2: 'H', 0x4: 'I'}

    def __init__(self, parent, address: dict, length: dict, quantity: dict, record: int, bit=None):
        self.buffer = parent.buffer
        self.address = Address(**address)
        self.length = Length(**length)
        self.quantity = Quantity(**quantity)
        self.record = record
        self.bit = bit

    def set_offset(self, offset: int):
        self.offset = offset

    def set_start(self, index: int):
        self.start = index

    @property
    def real_quantity(self):
        return self.quantity(self.buffer, self.offset) - self.start

    def get_data(self, data_index: int):
        if not data_index < self.real_quantity:
            return None
        address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
        length = self.length(self.buffer, self.record * (data_index + self.start) + self.offset)
        fmt = self.length_format[length]
        data = unpack_from(fmt, self.buffer, address)[0]
        if self.bit:
            return self._load_bin(data)
        else:
            return data

    def set_data(self, data_index: int, value: int):
        if data_index < self.real_quantity:
            address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
            length = self.length(self.buffer, self.record * (data_index + self.start) + self.offset)
            fmt = self.length_format[length]
            if self.bit:
                data = self._save_bin(unpack_from(fmt, self.buffer, address)[0], value)
            else:
                data = value
            pack_into(fmt, self.buffer, address, data)

    def _load_bin(self, number: int) -> int:
        if isinstance(self.bit, int):
            return (number & ((1 << (self.bit + 1)) - 1)) >> self.bit
        else:
            return (number & ((1 << self.bit[1]) - 1)) >> self.bit[0]

    def _save_bin(self, number: int, data: int) -> int:
        if isinstance(self.bit, int):
            return number | (data << self.bit)
        elif self.bit[0] == 0:
            return (number >> self.bit[1] << self.bit[1]) | data
        else:
            return number & (((1 << self.bit[0]) - 1 << self.bit[1]) | (1 << self.bit[0]) - 1) | (data << self.bit[0])
