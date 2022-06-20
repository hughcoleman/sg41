<h3 align="center">sg41</h3>

<p align="center">
  <b>A historically accurate simulator of the Schlüsselgerät 41 Cipher Machine</b>
</p>

The Schlüsselgerät 41 was a mechanical cipher machine developed by Wanderer in modern-day Chemnitz, Germany. It was primarily used by the [German Intelligence Service](https://en.wikipedia.org/wiki/Abwehr) for securing top-secret communications.

#### Usage

```python
import sg41

machine = sg41.SG41(
    sg41.Wheel.from_pattern_str("0001101011000100010001101"),
    sg41.Wheel.from_pattern_str("0110100100001011100101100"),
    sg41.Wheel.from_pattern_str("11001001000100100100010"),
    sg41.Wheel.from_pattern_str("01001000111010001110010"),
    sg41.Wheel.from_pattern_str("001001001010000101011010"),
    sg41.Wheel.from_pattern_str("011001100110001011010100")
)

print(
    machine.crypt("SCHLUESSELGERAETVIEREINSWANDERER", key=[0, 1, 2, 3, 0, 0])
) # IHEPLRETQSDSNDCWHPIVVGLYMHOWSJQS
```

This example has been designed to match the example provided in the *Simulation* section of Kopacz & Reuvers' paper.

#### References

* Kopacz, K., & Reuvers, P. (2021). *Schlüsselgerät 41: Full technical details of the German wartime SG-41 cipher machine.* Crypto Museum, Eindhoven (Netherlands). [https://www.cryptomuseum.com/pub/files/CM_SG41.pdf](https://www.cryptomuseum.com/pub/files/CM_SG41.pdf)

#### License

[MIT](https://choosealicense.com/licenses/mit/)
