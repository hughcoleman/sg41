#!/usr/bin/env python
# -*- coding: utf-8 -*-
# test_wheel.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)
import unittest

from sg41.wheel import Wheel

import random


class TestWheel(unittest.TestCase):
    def test__constructor(self):
        w1 = Wheel(size=25)

        self.assertEqual(25, len(w1.pins))
        self.assertTrue(all(pin == 0 for pin in w1.pins))
        self.assertEqual(25, w1.size)
        self.assertEqual(0, w1.position)

        w2 = Wheel(pins=[0, 1, 0, 0, 1, 1, 0, 1], position=4)

        self.assertEqual(8, len(w2.pins))
        self.assertEqual(8, w2.size)
        self.assertEqual(4, w2.position)

        # try illegal parameters
        self.assertRaises(ValueError, Wheel, size=24, position=-1)
        self.assertRaises(ValueError, Wheel, size=24, position=24)
        self.assertRaises(ValueError, Wheel, size=24, position=100)

        self.assertRaises(ValueError, Wheel, pins=[0, 0, 1, 8, 1])
        self.assertRaises(ValueError, Wheel, pins=[1, "a", 0])
        self.assertRaises(ValueError, Wheel, pins=13)
        self.assertRaises(ValueError, Wheel, pins="z")

    def test__step(self):
        # randomly generate the positions of the pins
        pins = [random.randint(0, 1) for _ in range(25)]

        # create the Wheel object and step it 25 times, .peek(0)ing to verify
        # its progress
        wheel = Wheel(pins=pins)
        self.assertEqual(0, wheel.position)
        for i in range(25):
            self.assertEqual(pins[i], wheel.peek(0))
            wheel.step()
        self.assertEqual(0, wheel.position)

    def test__peek(self):
        # randomly generate the positions of the pins
        pins = [random.randint(0, 1) for _ in range(25)]

        # create the Wheel object and step it 25 times, .peek()ing to verify
        # its progress
        wheel = Wheel(pins=pins)
        self.assertEqual(0, wheel.position)
        for i in range(25):
            self.assertEqual(pins[(i + 8) % 25], wheel.peek(8))
            self.assertEqual(pins[(i - 5) % 25], wheel.peek(-5))
            wheel.step()
        self.assertEqual(0, wheel.position)
