#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into


class Address:
    """
    用以解析数据偏移地址的类
    分成两种情况：
    1.当仅有normal_offset有值时
      则normal_offset作为固定偏移地址
      通过加上全局偏移地址global_offset的形式获取真实的偏移地址
    2.当pointer_offset也有值时
      则normal_offset作为指向真实地址的指针
      通过加上全局偏移地址global_offset的形式获取指针指向的偏移地址
      再通过加上指针偏移修正pointer_offset获取真实的偏移地址
    """

    def __init__(self, normal_offset: int, pointer_offset: int = None):
        self.normal_offset = normal_offset
        self.pointer_offset = pointer_offset

    def set_normal_offset(self, offset: int):
        self.normal_offset = offset

    def set_pointer_offset(self, offset: int):
        self.pointer_offset = offset

    def _get_address(self, buffer: bytearray, global_offset: int) -> int:
        if self.pointer_offset is not None:
            return unpack_from('I', buffer, self.normal_offset + global_offset)[0] + self.pointer_offset
        return self.normal_offset + global_offset

    def _set_address(self, buffer: bytearray, global_offset: int, address: int):
        if self.pointer_offset is not None:
            pack_into('I', buffer, self.normal_offset + global_offset, address - self.pointer_offset)

    def __call__(self, buffer: bytearray, global_offset: int, address: int = None):
        if address is None:
            return self._get_address(buffer, global_offset)
        self._set_address(buffer, global_offset, address)
