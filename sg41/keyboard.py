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

    DIGITS = {
        "1": "Q",
        "2": "W",
        "3": "E",
        "4": "R",
        "5": "T",
        "6": "Z",
        "7": "U",
        "8": "I",
        "9": "O",
        "0": "P",
    }

    @staticmethod
    def encode(message, sequence=["J", "J"]):
        shifted = False

        encoded = []
        for c in message.upper():
            if c == "J":
                c = "I"

            if c == " ":
                c = "J"

            if c.isalpha():
                if shifted:
                    encoded.extend(sequence)
                    shifted = False
                encoded.append(c)

            elif c.isdigit():
                if not shifted:
                    encoded.extend(sequence)
                    shifted = True
                encoded.append(Keyboard.DIGITS[c])

        return encoded

    @staticmethod
    def decode(message, sequence=["J", "J"]):
        shifted = False

        decoded = []
        i = 0
        while i < len(message):
            c = message[i]

            # Check for this shift/unshift sequence.
            if (i < len(message) - 1) and (
                list(message[i : i + len(sequence)]) == sequence
            ):
                shifted = not shifted
                i = i + 2
                continue

            elif c == "J":
                c = " "

            elif shifted:
                if c not in "PQWERTZUIO":
                    c = "?"
                else:
                    c = str("PQWERTZUIO".index(c))

            decoded.append(c)
            i = i + 1

        return "".join(decoded)
