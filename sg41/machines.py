#!/usr/bin/env python
# -*- coding: utf-8 -*-
# machines.py
# Copyright (c) 2021 Hugh Coleman
#
# This file is part of hughcoleman/sg41, a historically accurate simulator of
# the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
# (see LICENSE.)


class SG41:
    """A historically accurate implementation of the Schlüsselgerät 41 Cipher
    Machine.
    """

    CHARSET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def encrypt(self, plaintext):
        raise NotImplementedError("SG41.encrypt not implemented.")

    def decrypt(self, ciphertext):
        raise NotImplementedError("SG41.decrypt not implemented.")

    def __init__(self):
        pass


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
