# -*- coding: utf-8 -*-

from __future__ import absolute_import

from .base import Type


class Doc(Type):
    """
    Implements the Microsoft Office pre 2007 type matcher. 
    Including doc, ppt, xls extensions.
    """
    MIME = 'application/msword'
    EXTENSION = 'doc'

    def __init__(self):
        super(Doc, self).__init__(
            mime=Doc.MIME,
            extension=Doc.EXTENSION
        )

    def match(self, buf):
        return (len(buf) > 7 and
                buf[0] == 0xD0 and
                buf[1] == 0xCF and
                buf[2] == 0x11 and
                buf[3] == 0xE0 and
                buf[4] == 0xA1 and
                buf[5] == 0xB1 and
                buf[6] == 0x1A and
                buf[7] == 0xE1)