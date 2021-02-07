#!/usr/bin/env python
# -*- coding: utf-8 -*-
# keyboard.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)
from .machines import SG41


class Keyboard:
    @staticmethod
    def encode(message, j="i"):
        # TODO: handle numerical shifting/unshifting sequences

        return [
            "J"         if c.isspace()  else # encode spaces
            j.upper()   if c == "J"     else # encode "J"s
            c.upper()
            
            for c in message.upper()
            if (c in SG41.CHARSET or c.isspace())
        ]
