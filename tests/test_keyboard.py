#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_keyboard.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)
import unittest

from sg41.keyboard import Keyboard


class TestKeyboard(unittest.TestCase):
    def test__encode(self):
        self.assertEqual(
            "SCHLUSSELGERATJFORTYONE",
            "".join(Keyboard.encode("Schlusselgerat Forty-One")),
        )

        self.assertEqual(
            "IOLLYJIACKJANDJIOYFULJIILLJIUMPINGJDOWNJTHEJIAGGEDJHILL",
            "".join(
                Keyboard.encode(
                    "Jolly Jack and joyful Jill, jumping down the jagged hill."
                )
            ),
        )

    def test__decode(self):
        pass
