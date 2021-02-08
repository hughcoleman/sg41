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

# Grundstellung

PINS = [
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
]

POSITIONS = [0, 1, 2, 3, 0, 0]


class TestSG41(unittest.TestCase):
    def test__encrypt(self):
        machine = SG41(PINS, POSITIONS)

        # test the .encrypt() method using the sample plaintext/ciphertext pair
        # provided in Kopacz and Reuvers' paper
        self.assertEqual(
            "IHEPLRETQSDSNDCWHPIVVGLYMHOWSJQS",
            machine.encrypt("SCHLUESSELGERAETVIEREINSWANDERER"),
        )

    def test__decrypt(self):
        machine = SG41(PINS, POSITIONS)

        # test the .decrypt() method using the sample plaintext/ciphertext pair
        # provided in Kopacz and Reuvers' paper
        self.assertEqual(
            "SCHLUESSELGERAETVIEREINSWANDERER",
            machine.decrypt("IHEPLRETQSDSNDCWHPIVVGLYMHOWSJQS"),
        )


class TestSG41Z(unittest.TestCase):
    def test__encrypt(self):
        pass

    def test__decrypt(self):
        pass
