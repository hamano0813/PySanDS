#!/usr/bin/env python
# -*- coding: utf-8 -*-

from struct import unpack_from, pack_into
from PIL import Image
from attributes import Address, Quantity


class Picture:
    offset = start = 0

    def __init__(self, parent, address: dict, size: tuple, quantity: dict, record: int, palette: dict = None):
        self.buffer = parent.buffer
        self.address = Address(**address)
        self.width, self.height = size
        self.quantity = Quantity(**quantity)
        self.record = record
        self.palette = Address(**palette) if palette else None

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
        fmt = 'B' * self.width * self.height
        pixel_data = unpack_from(fmt, self.buffer, address)
        image = Image.new('P', (self.width, self.height))
        for box_col in range(self.height // 8):
            for box_row in range(self.width // 8):
                for row in range(8):
                    for col in range(8):
                        pixel_x = box_row * 8 + row
                        pixel_y = box_col * 8 + col
                        box = box_col * self.width // 8 + box_row
                        off = box * 64 + col * 8 + row
                        image.putpixel((pixel_x, pixel_y), pixel_data[off])
        image.putpalette(self._get_palette(data_index))
        return image

    def set_data(self, data_index: int, picture: Image.Image):
        self._set_palette(data_index, [color // 8 * 8 for color in picture.getpalette()])
        image = picture.convert('P')
        address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
        for box_col in range(self.height // 8):
            for box_row in range(self.width // 8):
                for row in range(8):
                    for col in range(8):
                        pixel_x = box_row * 8 + row
                        pixel_y = box_col * 8 + col
                        box = box_col * self.width // 8 + box_row
                        off = box * 64 + col * 8 + row
                        pixel = image.getpixel((pixel_x, pixel_y))
                        pack_into('B', self.buffer, address + off, pixel)

    def _get_palette(self, data_index: int):
        if self.palette is not None:
            address = self.palette(self.buffer, 0x204 * (data_index + self.start))
        else:
            image_address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
            address = image_address + self.width * self.height + 4
        fmt = 'H' * 256
        palette_data = unpack_from(fmt, self.buffer, address)
        palette = []
        [palette.extend([(p & 0b0000000000011111) << 3, (p & 0b0000001111100000) >> 2, (p & 0b0111110000000000) >> 7])
         for p in palette_data]
        return palette

    def _set_palette(self, data_index: int, palette: list):
        if self.palette is not None:
            address = self.palette(self.buffer, 0x204 * (data_index + self.start))
        else:
            image_address = self.address(self.buffer, self.record * (data_index + self.start) + self.offset)
            address = image_address + self.width * self.height + 4
        for i in range(256):
            b, g, r = palette[(0 + 3 * i): (3 + 3 * i)]
            pal = (r << 7) | (g << 2) | (b >> 3)
            pack_into('H', self.buffer, address + i * 2, pal)

    def mapping(self) -> dict:
        return {i: self.get_data(i) for i in range(self.real_quantity)}
