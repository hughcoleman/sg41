#!/usr/bin/env python
# -*- coding: utf-8 -*-
# machines.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)
from sg41.wheel import Wheel


class SG41:
    """A historically accurate implementation of the Schlüsselgerät 41 Cipher
    Machine.
    """

    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    WHEEL_SIZES = [25, 25, 23, 23, 24, 24]
    PRINT_INNER = "PAKRHFIDZQNXMTBWJVGSOCLYUE"
    PRINT_OUTER = "FHRKAPEUYLCOSGVJWBTMXNQZDI"

    def feed(self, stream):
        """ Feed the machine with a given input. """

        output = ""
        for character in stream:
            senses = [self.wheels[i].peek(-5) for i in range(6)]

            # Phase I: If w6 = 1, then each of the wheels 1 to 5 where the pin
            #          is active causes the wheel to its right to step.
            if senses[5]:
                for i in range(5):
                    if senses[i]:
                        self.wheels[i + 1].step()

            # Phase II: If w6 = 1, then all wheels step.
            if senses[5]:
                for i in range(6):
                    self.wheels[i].step()

            # Cipher: Generate the pseudorandom number, and encrypt/decrypt the
            #         stream.
            inv = self.wheels[5].peek(8)
            prn = (
                (inv ^ self.wheels[0].peek(8)) * 1
                + (inv ^ self.wheels[1].peek(8)) * 2
                + (inv ^ self.wheels[2].peek(8)) * 4
                + (inv ^ self.wheels[3].peek(8)) * 8
                + (inv ^ self.wheels[4].peek(8)) * 10
            )

            output = (
                output
                + SG41.PRINT_OUTER[
                    (SG41.PRINT_INNER.index(character) + prn) % 26
                ]
            )

            # Phase III: Re-sense at position -5, and then each wheel 1 to 5
            #            where the pin is active causes the wheel to its right
            #            to step..
            senses = [self.wheels[i].peek(-5) for i in range(6)]
            for i in range(5):
                if senses[i]:
                    self.wheels[i + 1].step()

            # Phase IV: All wheels step.
            for i in range(6):
                self.wheels[i].step()

        return output

    def encrypt(self, plaintext):
        """ Encrypt a plaintext message. """

        if any(c not in SG41.CHARSET for c in plaintext):
            raise ValueError("illegal character in plaintext stream")

        return self.feed(plaintext)

    def decrypt(self, ciphertext):
        """ Decrypt a ciphertext message. """

        if any(c not in SG41.CHARSET for c in ciphertext):
            raise ValueError("illegal character in ciphertext stream")

        return self.feed(ciphertext)

    def __init__(self, internal, external):
        # validate internal key
        if type(internal) is not list or len(internal) != 6:
            raise ValueError("internal key must be a list of pin positions")

        for i in range(6):
            if (
                type(internal[i]) is not list
                or len(internal[i]) != SG41.WHEEL_SIZES[i]
            ):
                raise ValueError(
                    "wheel #{} must have {} pins".format(
                        i + 1, SG41.WHEEL_SIZES[i]
                    )
                )

        # validate external key
        if type(external) is not list or len(external) != 6:
            raise ValueError("external key must be a list of positions")

        for i in range(6):
            if (
                type(external[i]) is not int
                or external[i] < 0
                or external[i] >= SG41.WHEEL_SIZES[i]
            ):
                raise ValueError(
                    "wheel #{} cannot be set to position {}".format(
                        i + 1, external[i]
                    )
                )

        self.wheels = [
            Wheel(pins=pins, position=position)
            for pins, position in zip(internal, external)
        ]


class SG41Z:
    """A historically accurate implementation of the Schlüsselgerät 41Z Cipher
    Machine.
    """

    # NOTE: This machine is not described in Kopacz and Reuvers' paper, thus,
    # the following implementation may not be correct.

    CHARSET = "0123456789"

    def encrypt(self, plaintext):
        raise NotImplementedError("SG41Z.encrypt not implemented.")

    def decrypt(self, ciphertext):
        raise NotImplementedError("SG41Z.decrypt not implemented.")

    def __init__(self):
        pass
