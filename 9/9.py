file = open('input')
field = [line[:-1] for line in file.readlines()]
file.close()

lowPoints = []
risk = 0
for i in range(len(field)):
    for j in range(len(field[0])):
        val = field[i][j]
        if i > 0 and val >= field[i - 1][j]:
            pass
        elif i < len(field) - 1 and val >= field[i + 1][j]:
            pass
        elif j > 0 and val >= field[i][j - 1]:
            pass
        elif j < len(field[0]) - 1 and val >= field[i][j + 1]:
            pass
        else:
            print("new low point @{}: {}".format((i, j), field[i][j]))
            lowPoints.append((i, j))
            risk += 1 + int(val)


print("risk: {}".format(risk))

checked = []


def basinSum(x, y):
    if field[x][y] == '9' or checked.count((x, y)) == 1:
        return 0
    else:
        neighbors = []
        if x > 0 and checked.count((x - 1, y)) == 0:
            neighbors.append((x - 1, y))
        if x < len(field) - 1 and checked.count((x + 1, y)) == 0:
            neighbors.append((x + 1, y))
        if y > 0 and checked.count((x, y - 1)) == 0:
            neighbors.append((x, y - 1))
        if y < len(field[0]) - 1 and checked.count((x, y + 1)) == 0:
            neighbors.append((x, y + 1))
        checked.append((x, y))
        return 1 + sum([basinSum(n[0], n[1]) for n in neighbors])


basins = []
for point in lowPoints:
    print("basin @ point {}...".format(point))
    basins.append(basinSum(point[0], point[1]))
basins.sort(reverse=True)
print(int(basins[0]) * int(basins[1]) * int(basins[2]))
