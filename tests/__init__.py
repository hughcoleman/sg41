""" sg41 | Copyright (c) 2021-2022 Hugh Coleman """

import unittest

class TestSG41(unittest.TestCase):
    def test(self):
        import sg41

        machine = sg41.SG41(
            sg41.Wheel.from_pattern_str("0001101011000100010001101"),
            sg41.Wheel.from_pattern_str("0110100100001011100101100"),
            sg41.Wheel.from_pattern_str("11001001000100100100010"),
            sg41.Wheel.from_pattern_str("01001000111010001110010"),
            sg41.Wheel.from_pattern_str("001001001010000101011010"),
            sg41.Wheel.from_pattern_str("011001100110001011010100")
        )

        # Sample plaintext/ciphertext pair provided on p. 22 of Kopacz and
        # Reuvers.
        self.assertEqual(
            "IHEPLRETQSDSNDCWHPIVVGLYMHOWSJQS",
            machine.crypt("SCHLUESSELGERAETVIEREINSWANDERER", key=[0, 1, 2, 3, 0, 0])
        )
        self.assertEqual(
            "SCHLUESSELGERAETVIEREINSWANDERER",
            machine.crypt("IHEPLRETQSDSNDCWHPIVVGLYMHOWSJQS", key=[0, 1, 2, 3, 0, 0])
        )
