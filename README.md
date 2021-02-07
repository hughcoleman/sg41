<h3 align="center">sg41</h3>

<p align="center">
  <b>A historically accurate simulator of the Schlüsselgerät 41 Cipher Machine</b>
</p>

The Schlüsselgerät 41 was a mechanical cipher machine developed by Wanderer Werke in modern-day Chemnitz, Germany. It was primarily used by the [German Intelligence Service](https://en.wikipedia.org/wiki/Abwehr) for securing top-secret communications.

###### Usage

N/A

###### Ambiguities

This implementation is primarily based on Kopacz & Reuvers' paper, cited below. Unfortunately, there are several ambiguities in the paper&mdash;I have done my best to be as flexible around these, but will also confess them here.

**In which direction do the pin-wheels rotate?**

I am led to believe that the pin-wheels rotate towards the user (that is, the pin that was sensed by the adder moves towards the user.) This, however, is the opposite direction that the crank is turned.

**When does the adder sense/latch the pins at "+8"?**

There are several explanations as to when this happens, but all differ.

1. Table 4 (p. 16) suggests that the adder senses *and latches* the pins at "+8" at the six o'clock position, before a key is pressed.

2. Page 15 suggests that "two of the stepping phases are carried out before the encryption of a letter. The other two stepping phases are carried out after the encryption of a letter and will therefore have an effect on the next letter that is to be encrypted." In other words, Phases I and II are run, then the pseudo-random number is generated, and finally Phases III and IV are run.

3. Page 17 suggests that the "stepping of the pin-wheels [during Phases I, II, and III] take place before the pseudo-random number is generated and the print head is rotated. This means that [they have] an effect on the encryption of the current input letter. [The final] stepping phase, Phase IV], takes place after the letter has been encrypted, and ... therefore only [has] an effect on the next letter that is to be encrypted." In other words, Phases I, II, and II run first, then the pseudo-random number is generated, and finally Phase IV is run.

###### References

* Kopacz, K., & Reuvers, P. (2021). *Schlüsselgerät 41*. [https://www.cryptomuseum.com/pub/files/CM_SG41.pdf](https://www.cryptomuseum.com/pub/files/CM_SG41.pdf)

###### License

[MIT](https://choosealicense.com/licenses/mit/)
