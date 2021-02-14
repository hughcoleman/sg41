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

    # the SZ-41 was only capable of handling the 26 letters of the Latin
    # alphabet
    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    WHEEL_SIZES = [25, 25, 23, 23, 24, 24]

    PRINT_INNER = "PAKRHFIDZQNXMTBWJVGSOCLYUE"
    PRINT_OUTER = "FHRKAPEUYLCOSGVJWBTMXNQZDI"

    def __process(self, stream):
        """ Feed the machine with a given input. """

        output = ""
        for character in stream:
            # Phase I:
            # If Wheel 6 is active, then for each Wheel 1 to 5, if it is
            # active, then we step the wheel immediately to its right.
            #
            # Phase II:
            # If Wheel 6 was active before Phase I, then all wheels step once.
            if self.wheels[6].peek(-5):
                for wheel in [6, 5, 4, 3, 2, 1]:
                    if wheel > 1 and self.wheels[wheel - 1].peek(-5):
                        self.wheels[wheel].step()
                    self.wheels[wheel].step()

            # Generate the pseudorandom number using the pins eight above the
            # window, and encrypt/decrypt the currently pressed character.
            inv = self.wheels[6].peek(8)
            prn = (
                (inv ^ self.wheels[1].peek(8)) * 1 +
                (inv ^ self.wheels[2].peek(8)) * 2 +
                (inv ^ self.wheels[3].peek(8)) * 4 +
                (inv ^ self.wheels[4].peek(8)) * 8 +
                (inv ^ self.wheels[5].peek(8)) * 10
            )

            output = (
                output + SG41.PRINT_OUTER[
                    (SG41.PRINT_INNER.index(character) + prn) % 26
                ]
            )

            # Phase III:
            # Re-sense the pins five below the window, and then for each Wheel
            # 1 to 5 that is active, step the wheel immediately to its right.
            # 
            # Phase IV:
            # All wheels step.
            for wheel in [6, 5, 4, 3, 2, 1]:
                if wheel > 1 and self.wheels[wheel - 1].peek(-5):
                    self.wheels[wheel].step()
                self.wheels[wheel].step()

        return output

    def encrypt(self, plaintext):
        """ Encrypt a plaintext message. """

        if any(c not in SG41.CHARSET for c in plaintext):
            raise ValueError("illegal character in plaintext stream.")

        return self.__process(plaintext)

    def decrypt(self, ciphertext):
        """ Decrypt a ciphertext message. """

        if any(c not in SG41.CHARSET for c in ciphertext):
            raise ValueError("illegal character in ciphertext stream.")

        return self.__process(ciphertext)

    def __init__(self, internal, external):
        # validate the "internal" key (cam positions)
        if type(internal) is not list or len(internal) != 6:
            raise ValueError(
                "the internal key must be a list of lists of pin positions."
            )

        for wheel in range(6):
            if (
                type(internal[wheel]) is not list
                or len(internal[wheel]) != SG41.WHEEL_SIZES[wheel]
            ):
                raise ValueError(
                    "wheel {} contains {} pins, but you specified {}.".format(
                        wheel + 1,
                        SG41.WHEEL_SIZES[wheel],
                        len(internal[wheel]),
                    )
                )

        # validate the "external" key (initial rotor positions)
        if type(external) is not list or len(external) != 6:
            raise ValueError(
                "the external key must be a list of positions to set rotors."
            )

        for wheel in range(6):
            if (
                type(external[wheel]) is not int
                or external[wheel] < 0
                or external[wheel] >= SG41.WHEEL_SIZES[wheel]
            ):
                raise ValueError(
                    "wheel {} cannot be set to position {}.".format(
                        wheel + 1, external[wheel]
                    )
                )

        self.wheels = {
            (wheel + 1): Wheel(pins=pins, position=position)
            for wheel, (pins, position) in enumerate(zip(internal, external))
        }


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
