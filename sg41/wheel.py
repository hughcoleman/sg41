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

        if position >= len(pins) or position < 0:
            raise ValueError(
                "cannot set position to {}, too big".format(position)
            )

        # TODO: set position based on letter/number

        self.pins = pins
        self.size = len(pins)
        self.position = position
