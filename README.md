<h3 align="center">sg41</h3>

<p align="center">
  <b>A historically accurate simulator of the Schlüsselgerät 41 Cipher Machine</b>
</p>

The Schlüsselgerät 41 was a mechanical cipher machine developed by Wanderer Werke in modern-day Chemnitz, Germany. It was primarily used by the [German Intelligence Service](https://en.wikipedia.org/wiki/Abwehr) for securing top-secret communications.

###### Usage

Import the `SG41` class from the `sg41.machines` module, and pass the positions of the 144 cams and six rotors to its constructor.

To perform an encryption or decryption operation, pass the relevant plaintext or ciphertext to the `.encrypt()` or `.decrypt()` methods, respectively. When encrypting, consider using `sg41.keyboard.Keyboard` to encode the plaintext into a compatible format.

```python
from sg41.machines import SG41

PINS = [
    [0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1],
    [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0],
    [1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0]
]

POSITIONS = [0, 1, 2, 3, 0, 0]

machine = SG41(PINS, POSITIONS)

print(
    machine.encrypt("SCHLUESSELGERAETVIEREINSWANDERER")
)

# IHEPLQEDMYPWMQDXWDKCVGLYMHOWSJQS
```

This example has been designed to match the example provided in the *Simulation* section of Kopacz & Reuvers' paper.

###### Cryptanalysis

A naive wheel-setting algorithm is implemented in [`cryptanalysis.cpp`](https://github.com/hughcoleman/sg41/blob/main/cryptanalysis.cpp).

It employs the use of some questionable search-space reduction algorithms, so, if it produces unexpected results, please do let me know! Define the preprocessor macro `DISABLE_OPTIMIZED` at compile-time to disable the optimizations.

###### References

* Kopacz, K., & Reuvers, P. (2021). *Schlüsselgerät 41: Full technical details of the German wartime SG-41 cipher machine.* Crypto Museum, Eindhoven (Netherlands). [https://www.cryptomuseum.com/pub/files/CM_SG41.pdf](https://www.cryptomuseum.com/pub/files/CM_SG41.pdf)

###### License

[MIT](https://choosealicense.com/licenses/mit/)
