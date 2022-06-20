""" sg41 | Copyright (c) 2021-2022 Hugh Coleman """

import typing

__author__ = "Hugh Coleman"
__copyright__ = "Copyright (c) 2021-2022 Hugh Coleman"
__version__ = "1.0.0"

class Wheel:
    """ class Wheel """

    cams: typing.List[bool]
    position: int

    def __init__(self, cams: typing.List[bool], position: int = 0):
        self.cams = cams
        self.position = position

    @classmethod
    def from_pattern_str(cls, pattern: str):
        def _bool(x):
            return { "0": False, "1": True }[x]

        return cls([ _bool(c) for c in pattern ], position = 0)

    def peek(self, offset: int = 0):
        return self.cams[(self.position + offset) % len(self.cams)]

    def step(self):
        self.position = (self.position + 1) % len(self.cams)

INNER_PRINTER_RING = "FHRKAPEUYLCOSGVJWBTMXNQZDI"
OUTER_PRINTER_RING = "PAKRHFIDZQNXMTBWJVGSOCLYUE"

class SG41:
    """ class SG41 """

    wheels: typing.Dict[int, Wheel]

    def __init__(self, *wheels: typing.List[Wheel]):
        self.wheels = {
            i: wheel
                for i, wheel in enumerate(wheels, 1)
        }

    def __keystream(self):
        while True:
            # Phase I/II
            if self.wheels[6].peek(-5):
                for wheel in (6, 5, 4, 3, 2, 1):
                    if wheel != 1 and self.wheels[wheel - 1].peek(-5):
                        self.wheels[wheel].step()
                    self.wheels[wheel].step()

            # Compute pseudo-random number!
            invert = self.wheels[6].peek(8)
            yield (
                (invert ^ self.wheels[1].peek(8)) * 1 +
                (invert ^ self.wheels[2].peek(8)) * 2 +
                (invert ^ self.wheels[3].peek(8)) * 4 +
                (invert ^ self.wheels[4].peek(8)) * 8 +
                (invert ^ self.wheels[5].peek(8)) * 10
            )

            # Phase III/IV
            for wheel in (6, 5, 4, 3, 2, 1):
                if wheel != 1 and self.wheels[wheel - 1].peek(-5):
                    self.wheels[wheel].step()
                self.wheels[wheel].step()

    def crypt(self, message: str, key: typing.List[int] = [0, 0, 0, 0, 0, 0]):
        # Reposition wheels according to external key.
        for i, k in enumerate(key, 1):
            self.wheels[i].position = k

        return "".join(
            INNER_PRINTER_RING[(OUTER_PRINTER_RING.index(c) + prn) % 26]
                for c, prn in zip(message, self.__keystream())
        )
