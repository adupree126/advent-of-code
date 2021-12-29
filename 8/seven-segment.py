# before any deductions can be made, assume everything
aToG = set('a', 'b', 'c', 'd', 'e', 'f', 'g')
# wirings maps which display segment each wire might actually map to
wirings = {}
for wire in aToG:
    wirings[wire] = aToG

displays = {set('abcefg'): '0', set('cf'): '1', set('acdeg'): '2',
            set('acdfg'): '3', set('bcdf'): '4', set('abdfg'): '5',
            set('abdefg'): '6', set('acf'): '7', set('abcdefg'): '8',
            set('abcdfg'): '9'}

# returns true if a given wire string it's a 1, 4, 7, 8 or 8


def isDeducable(digit):
    return [2, 3, 4, 7].count(len(digit)) == 1 or set(digit) in displays


def makeDeductions(digit):
    if len(digit) == 2:    # it's a 1, the two digits map to either of  'cf'
        for signal in digit:
            wirings[signal] = wirings[signal] & set('cf')
        for signal in aToG - set(digit):  # deduction time
            wirings[signal] = wirings[signal] - set('cf')
    elif len(digit) == 3:  # 7, so 'acf'
        for signal in digit:
            wirings[signal] = wirings[signal] & set('acf')
        for signal in aToG - set(digit):
            wirings[signal] = wirings[signal] - set('acf')
    elif len(digit) == 4:  # 4 so 'bcdf'
        for signal in digit:
            wirings[signal] = wirings[signal] & set('bcdf')
        for signal in aToG - set(digit):
            wirings[signal] = wirings[signal] - set('bcdf')
    elif len(digit) == 5:  # it's a 2, 3, or 5
        # todo: figure out how to deal with ambiguity




file = open('input')
data = file.readlines()
file.close()
notes = [s.split(' ') for s in [line.split(' | ')[0] for line in data]]
outputs = [s.split(' ') for s in [line.split(' | ')[1][:-1] for line in data]]


unSortedOutputs = []
for l in outputs:
    for s in l:
        unSortedOutputs.append(s)
uniqueMap = (list(map(lambda x: 1 if isUnique(x) else 0, unSortedOutputs)))
nUnique = sum(uniqueMap)
print('number of 1, 4, 7, or 8: {}'.format(nUnique))
