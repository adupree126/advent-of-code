file = open('input')
data = file.readlines()
file.close()
notes = [s.split(' ') for s in [line.split(' | ')[0] for line in data]]
outputs = [s.split(' ') for s in [line.split(' | ')[1][:-1] for line in data]]
numbersOut = []
digits = {
    "abcefg": '0',
    "cf": '1',
    "acdeg": '2',
    "acdfg": '3',
    "bcdf": '4',
    "abdfg": '5',
    "abdefg": '6',
    "acf": '7',
    "abcdefg": '8',
    "abcdfg": '9'
}

for i in range(len(notes)):
    curNotes = sorted(notes[i], key=len)
    curOutputs = outputs[i]
    wires = set("abcdefg")
    mappings = {}
    for wire in wires:
        mappings[wire] = wires
    # analyse the 'knowables' (1, 4, 7)
    for wire in wires:
        if curNotes[0].count(wire) == 1:    # one
            mappings[wire] = set('cf')
        elif curNotes[1].count(wire) == 1:  # seven
            mappings[wire] = set('a')
        elif curNotes[2].count(wire) == 1:  # four
            mappings[wire] = set('bd')
        else:                               # everything else
            mappings[wire] = set('eg')

    # check the length 5 group: (2, 3, 5)
    # find 3 to get d and g
    len5 = curNotes[3:6]
    for cand in len5:
        # check if it's a 3 (only 3 contains all of 1)
        if set(curNotes[0]).issubset(set(cand)):
            # if it's a 3, find the g
            for wire in mappings:
                mappings[wire] = mappings[wire] - set('g')
            unseen = str(set(cand) - set(curNotes[1]) - set(curNotes[2]))[2:3]
            mappings[unseen] = set('g')
            # now differentiate d and b
            for signal in cand:
                mappings[signal] -= set('b')
            break

    # now use 9 to differentiate b and e
    len6 = curNotes[6:9]
    print(len6)
    for cand in len6:
        # is it a 9?
        if set(curNotes[2]).issubset(set(cand)):
            print("{} maps to 9".format(cand))
            # it's a 9, so find the e
            for wire in mappings:
                mappings[wire] = mappings[wire] - set('e')
            unseen = str(wires - set(cand))[2:3]
            mappings[unseen] = set('e')
        # is it a 6?
        if not set(curNotes[0]).issubset(set(cand)):
            print("{} maps to 6".format(cand))
            # it's a 6, so find the c
            for wire in mappings:
                mappings[wire] -= set('c')
            unseen = str(wires - set(cand))[2:3]
            mappings[unseen] = set('c')
    # now only one should be ambiguous (whatever maps to b), but can be deduced
    for wire in mappings:
        if len(mappings[wire]) == 2:
            mappings[wire] = 'b'
        else:
            mappings[wire] = str(mappings[wire])[2:3]

    # now decode the outputs
    mappedOutputs = ["".join(sorted([mappings[signal]
                             for signal in digit])) for digit in curOutputs]
    numbersOut.append(int("".join([digits[o] for o in mappedOutputs])))

print(numbersOut)
print(sum(numbersOut))
