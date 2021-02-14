/**
 * cryptanalysis.cpp
 * Copyright (c) 2021 Hugh Coleman
 *
 * This file is part of hughcoleman/sg41, a historically accurate simulator of
 * the Schlüsselgerät 41 Cipher Machine. It is released under the MIT License
 * (see LICENSE.)
 */

#include <iostream>
#include <vector>

using namespace std;

const string R1_LABEL   = "ABCDEFGHIKLMNOPQRSTUVWXYZ";
const string R5_LABEL[] = {
    "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12",
    "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"
};
const string R6_LABEL[] = {
    "00", "02", "05", "07", "10", "12", "15", "17", "20", "22", "25", "27",
    "30", "32", "35", "37", "40", "42", "45", "47", "50", "52", "55", "57"
};

struct Rotor {
    // configuration
    int size = 0;
    vector<bool> cams;

    int position = 0;

    void step() {
        position = (position + 1) % size;
    }

    bool peek(int offset) {
        int i = (position - offset) % size;
        if (i < 0) i = i + size;

        return cams[i];
    }
};

void wheelset(Rotor rotors[6], vector<int> stream) {
    // Wheelsetting
    //
    // This naive algorithm attempts to recover the initial rotor positions,
    // given (1) the positions of the 144 rotor cams, and (2) a portion of the
    // pseudo-random stream.
    //
    // This is accomplished by considering all 190440000 possible rotor
    // positions, and simulating each one until it is discovered to be
    // incorrect, or we run out of samples. There are, luckily, some tricks we
    // can use the heavily reduce the search space.
    //
    // On an i5-7400, in the worst case, takes about a minute. On average,
    // though, this takes less than a second.

#if !defined(DISABLE_OPTIMIZATIONS)
    bool f1 = (
        stream[0] ==  0 || stream[0] ==  3 || stream[0] ==  4 ||
        stream[0] ==  7 || stream[0] ==  8 || stream[0] == 17 ||
        stream[0] == 18 || stream[0] == 21 || stream[0] == 22 ||
        stream[0] == 25
    );

    bool f2 = (
        stream[0] ==  1 || stream[0] ==  2 || stream[0] ==  5 ||
        stream[0] ==  6 || stream[0] ==  9 || stream[0] == 16 ||
        stream[0] == 19 || stream[0] == 20 || stream[0] == 23 ||
        stream[0] == 24
    );
#endif

    for (int r1 = 0; r1 < 25; r1++) {
    for (int r2 = 0; r2 < 25; r2++) {
#if !defined(DISABLE_OPTIMIZATIONS)
        // We can reduce the search space, by eliminating partial
        // configurations as early as possible.

        if (f1 && (
            // f1 is truthy iff the first value in the supplied stream can
            // only be created if the left- and second-to-left-most rotors
            // contribute identical values. Thus, we consider both cases for
            // the right-most rotor, and, if both lead to situations where
            // the left- and second-to-left-most rotors contribute differing
            // values, we can reject this r1/r2 starting position pair
            // entirely.

            // Case 1: Rotor 6 is inactive, leading to none of the rotors
            //         stepping in Phases I and II.
            (rotors[0].peek(-8) != rotors[1].peek(-8)) &&

            // Case 2: Rotor 6 is active, leading to the left-most rotor
            //         stepping once, and the second-to-left-most rotor
            //         stepping either once or twice, depending on the state
            //         of the cam at position +5.
            (rotors[0].peek(-7) != rotors[1].peek(-7 - rotors[0].peek(5)))
        )) {
            continue;
        } else if (f2 && (
            // f2 is truthy iff the first value in the supplied stream can
            // only be created if the left- and second-to-left-most rotors
            // contribute differing values. Thus, we consider both cases for
            // the right-most rotor, and, if both lead to situations where
            // the left- and second-to-left-most rotors contribute identical
            // values, we can reject this r1/r2 starting position pair
            // entirely.

            // Case 1: Rotor 6 is inactive, leading to none of the rotors
            //         stepping in Phases I and II.
            (rotors[0].peek(-8) == rotors[1].peek(-8)) &&

            // Case 2: Rotor 6 is active, leading to the left-most rotor
            //         stepping once, and the second-to-left-most rotor
            //         stepping either once or twice, depending on the state
            //         of the cam at position +5.
            (rotors[0].peek(-7) == rotors[1].peek(-7 - rotors[0].peek(5)))
        )) {
            continue;
        }
#endif
    for (int r3 = 0; r3 < 23; r3++) {
    for (int r4 = 0; r4 < 23; r4++) {
    for (int r5 = 0; r5 < 24; r5++) {
    for (int r6 = 0; r6 < 24; r6++) {
        rotors[0].position = r1;
        rotors[1].position = r2;
        rotors[2].position = r3;
        rotors[3].position = r4;
        rotors[4].position = r5;
        rotors[5].position = r6;

        // Now, consider the stream generated by starting
        // in the above configuration.
        for (int kprn : stream) {
            // Phase I/II
            if (rotors[5].peek(5)) {
                for (int i = 5; i >= 0; --i) {
                    if (i != 0 && rotors[i - 1].peek(5))
                        rotors[i].step();
                    rotors[i].step();
                }
            }

            // Pseudo-random Number Generation
            bool invert = rotors[5].peek(-8);
            int gprn = (
                (invert ^ rotors[0].peek(-8)) * 1  +
                (invert ^ rotors[1].peek(-8)) * 2  +
                (invert ^ rotors[2].peek(-8)) * 4  +
                (invert ^ rotors[3].peek(-8)) * 8  +
                (invert ^ rotors[4].peek(-8)) * 10
            );

            if (kprn != gprn) goto invalid;

            // Phase III/Phase IV
            for (int i = 5; i >= 0; --i) {
                if (i != 0 && rotors[i - 1].peek(5))
                    rotors[i].step();
                rotors[i].step();
            }
        }

        cout << R1_LABEL[r1] << " "
             << R1_LABEL[r2] << " "
             << R1_LABEL[r3] << " "
             << R1_LABEL[r4] << " "
             << R5_LABEL[r5] << " "
             << R6_LABEL[r6] << endl;

        invalid:
        ;
    }
    }
    }
    }
    }
    }

    return;
}

void wheelbreak(vector<int> stream) {
    // Wheelbreaking

    return;
}

int main() {
    Rotor rotors[6]{
        Rotor{
            .size = 25,
            .cams = vector<bool>{ 0, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 1 }
        },
        Rotor{
            .size = 25,
            .cams = vector<bool>{ 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 0, 0 }
        },
        Rotor{
            .size = 23,
            .cams = vector<bool>{ 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0       }
        },
        Rotor{
            .size = 23,
            .cams = vector<bool>{ 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0       }
        },
        Rotor{
            .size = 24,
            .cams = vector<bool>{ 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0    }
        },
        Rotor{
            .size = 24,
            .cams = vector<bool>{ 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 0    }
        }
    };

    vector<int> stream{
         6,  6,  2,  9, 11,  3, 13, 25, 23, 16,  6, 13, 18, 23, 11,  3, 10,
        25,  0, 11, 15,  7, 25, 15,  4,  0,  1,  9, 13, 12, 23, 9
    };

    wheelset(rotors, stream);
}
