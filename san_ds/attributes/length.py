#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into


class Length:
    """
    用以解析数据位长度的类
    分成三种情况：
    1.当仅有normal_length有值时
      则normal_length作为固定长度直接体现指定数据的位长度
      本情况主要用于定长文本或数值
    2.当normal_length和main_pointer有值时
      以main_pointer作为数据开始处的指针获取数据开始的偏移地址
      再根据sub_pointer是否有值来判断是否采用sub_pointer的指向作为数据结束的偏移地址
      通过将结束的偏移地址减去开始的偏移地址得到由指针控制的指定数据的位长度
      而normal_length则充当最大数据位长度的限制
      在设置由指针控制的数据位长度时不允许大于normal_length的值
      本情况主要用于由指针控制起始的文本
    3.当normal_length无值且main_pointer有值时
      以main_pointer作为数据开始处的指针获取数据开始的偏移地址
      再以寻找断点标识的方法从开始的偏移地址往后寻找数据断点
      以开始的偏移地址到断点后首个不等于断点内容的有数据的偏移地址长度作为数据的位长度
      如未找到断点则将位长度返回为2
      本情况主要用于由断点标识控制的不定长文本
      且本情况的不定长文本不支持修改文本长度
      原则上新文本所占的位长度不得大于原文本
    """

    def __init__(self, normal_length: int, main_pointer: int = None, pointer_offset: int = 0, sub_pointer: int = None):
        self.normal_length = normal_length
        self.main_pointer = main_pointer
        self.pointer_offset = pointer_offset
        self.sub_pointer = sub_pointer

    def set_normal_length(self, length: int):
        self.normal_length = length

    def set_main_pointer(self, pointer: int):
        self.main_pointer = pointer

    def set_pointer_offset(self, offset: int):
        self.pointer_offset = offset

    def set_sub_pointer(self, pointer: int):
        self.sub_pointer = pointer

    def _get_pointer_length(self, buffer: bytearray, global_offset: int) -> int:
        if self.sub_pointer is not None:
            start_offset = unpack_from('I', buffer, self.main_pointer + global_offset)[0]
            end_offset = unpack_from('I', buffer, self.sub_pointer + global_offset)[0]
        else:
            start_offset = unpack_from('I', buffer, self.main_pointer + global_offset)[0]
            end_offset = unpack_from('I', buffer, self.main_pointer + 0x4 + global_offset)[0]
        return end_offset - start_offset

    def _set_pointer_length(self, buffer: bytearray, global_offset: int, length: int):
        start_offset = unpack_from('I', buffer, self.main_pointer + global_offset)[0]
        end_offset = start_offset + min(self.normal_length, length)
        if self.sub_pointer is not None:
            pack_into('I', buffer, self.sub_pointer + global_offset, end_offset)
        else:
            pack_into('I', buffer, self.main_pointer + 0x4 + global_offset, end_offset)

    def _get_unfixed_length(self, buffer, global_offset) -> int:
        data_address = unpack_from('I', buffer, self.main_pointer + global_offset)[0] + self.pointer_offset
        data_bytes = unpack_from('512s', buffer, data_address)[0]
        for idx, character in enumerate(data_bytes[data_bytes.index(b'\00'):]):
            if character != b'\00':
                return data_bytes.index(b'\00') + idx
        return 2

    def _get_length(self, buffer: bytearray, global_offset: int) -> int:
        if self.main_pointer is None:
            return self.normal_length
        elif self.normal_length is None:
            return self._get_unfixed_length(buffer, global_offset)
        else:
            return self._get_pointer_length(buffer, global_offset)

    def _set_length(self, buffer: bytearray, global_offset: int, length: int):
        if self.normal_length is not None and self.main_pointer is not None:
            self._set_pointer_length(buffer, global_offset, length)

    def __call__(self, buffer: bytearray, global_offset: int, length: int = None):
        if length is None:
            return self._get_length(buffer, global_offset)
        self._set_length(buffer, global_offset, length)
