#!/usr/bin/env python
# -*- coding: utf-8 -*-

from attributes import Address, Length, Quantity

buffer = bytearray(open(r'D:\Python\PySanDS\resource\4032.nds', 'rb').read())

address = Address(0x0012B0E8, -0x1FFC000)
address_value = address(buffer, 0)
print(hex(address_value))

length = Length(148, 0x01CB7E1D, 0x00430C00)
length_value = length(buffer, 0)
print(length_value)
