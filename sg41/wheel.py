#!/usr/bin/env python
# -*- coding: utf-8 -*-
# wheel.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)


class Wheel:
    """ Emulate a single rotor. """

    def step(self):
        self.position = (self.position + 1) % self.size

    def peek(self, offset):
        return self.pins[(self.position + offset) % self.size]

    def __init__(self, pins=None, size=25, position=0):
        if pins is None:
            pins = [0] * size

        if (type(pins) is not list) or any(
            pin not in [0, 1, False, True] for pin in pins
        ):
            raise ValueError("pins must be a list of boolean-y values")

        if position >= len(pins) or position < 0:
            raise ValueError(
                "cannot set position to {}, too big".format(position)
            )

        # map pins to a list of integers (0/1)
        pins = [int(pin) for pin in pins]

        # TODO: set position based on letter/number

        self.pins = pins
        self.size = len(pins)
        self.position = position
