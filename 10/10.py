file = open('input')
lines = [line[:-1] for line in file.readlines()]
file.close()


def scoreLine(line):
    syntaxValues = {')': 3, ']': 57, '}': 1197, '>': 25137}
    autocompValue = {')': 1, ']': 2, '}': 3, '>': 4}
    expected = []
    for char in line:
        if char == '(':
            expected.append(')')
        elif char == '[':
            expected.append(']')
        elif char == '{':
            expected.append('}')
        elif char == '<':
            expected.append('>')
        elif char == expected[-1]:
            expected = expected[:-1]
        else:
            print("syntax error at {}, expected {}!".format(
                char, expected[-1]))
            # return syntaxValues[char]
            return 0  # for part 2
    # the line is incomplete
    score = 0
    expected.reverse()
    for value in expected:
        score *= 5
        score += autocompValue[value]
    return score


scores = [scoreLine(line) for line in lines]
autoScores = sorted(list(filter(lambda x: x > 0, scores)))
print(autoScores[len(autoScores) // 2])
