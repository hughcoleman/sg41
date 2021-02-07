#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_machines.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)
import unittest

from sg41.machines import SG41
from sg41.machines import SG41Z

import random


class TestSG41(unittest.TestCase):
    def test__encrypt(self):
        pins = [
            [random.randint(0, 1) for pin in range(size)]
            for size in SG41.WHEEL_SIZES
        ]
        positions = [random.randint(0, size - 1) for size in SG41.WHEEL_SIZES]

        machine = SG41(pins, positions)

        print("\n\n" + "=" * 80)
        print('Encrypting "WETTERREPORT" using the following settings.\n')
        print("pins      =", pins)
        print("positions = ", positions, "\n")
        print(
            "Computed ciphertext",
            machine.encrypt("WETTERREPORT") + ".",
            "Is this correct?",
        )
        print("=" * 80 + "\n\n")

    def test__decrypt(self):
        pass


class TestSG41Z(unittest.TestCase):
    def test__encrypt(self):
        pass

    def test__decrypt(self):
        pass
