#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from


class Quantity:
    """
    用以解析数据的序列数量的类
    分成两种情况：
    1.当仅有normal_quantity有值时
      则normal_quantity作为固定数量返回
    2.当main_pointer有值时
      则以main_pointer作为数据开始处的指针获取数据开始的偏移地址
      再根据sub_pointer是否有值来判断是否采用sub_pointer的指向作为数据结束的偏移地址
      通过将结束的偏移地址减去开始的偏移地址得到由指针控制的总数据区块长度
      以总数据区块长度除以区块内每条数据记录的长度record_length获得由指针控制的可变量据数量
    """

    def __init__(self, normal_quantity: int, main_pointer: int = None, record_length: int = 1, sub_pointer: int = None):
        self.normal_quantity = normal_quantity
        self.main_pointer = main_pointer
        self.record_length = record_length
        self.sub_pointer = sub_pointer

    def set_normal_quantity(self, quantity: int):
        self.normal_quantity = quantity

    def set_main_pointer(self, pointer: int):
        self.main_pointer = pointer

    def set_record_length(self, length: int):
        self.record_length = length

    def set_sub_pointer(self, pointer: int):
        self.sub_pointer = pointer

    def _get_quantity(self, buffer: bytearray, global_offset: int) -> int:
        if self.main_pointer is None and self.sub_pointer is None:
            return self.normal_quantity
        elif self.main_pointer is not None and self.sub_pointer is None:
            start_offset = unpack_from('I', buffer, self.main_pointer + global_offset)[0]
            end_offset = unpack_from('I', buffer, self.main_pointer + 0x4 + global_offset)[0]
        else:
            start_offset = unpack_from('I', buffer, self.main_pointer + global_offset)[0]
            end_offset = unpack_from('I', buffer, self.sub_pointer + global_offset)[0]
        return (end_offset - start_offset) // self.record_length

    def __call__(self, buffer: bytearray, global_offset: int):
        return self._get_quantity(buffer, global_offset)
