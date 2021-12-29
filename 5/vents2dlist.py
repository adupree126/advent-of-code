def pointsOnSegment(p1, p2):
    dx = 0
    dy = 0
    if p1[0] == p2[0]:
        dx = 0
    elif p1[0] < p2[0]:
        dx = 1
    else:
        dx = -1
    # now do the y's
    if p1[1] == p2[1]:
        dy = 0
    elif p1[1] < p2[1]:
        dy = 1
    else:
        dy = -1
    # for part 1:
    # if dy != 0 and dx != 0:
    #    return []
    curP = p1
    points = [p2]  # the while loop misses p2, so add it here
    while curP != p2:
        points.append(curP)
        curP = (curP[0] + dx, curP[1] + dy)
    return points


grid = [[0 for i in range(1000)] for j in range(1000)]

file = open('input')
segmentStrings = [line[:-1].split(' -> ') for line in file.readlines()]
for segment in segmentStrings:
    p1 = (int(segment[0].split(',')[0]), int(segment[0].split(',')[1]))
    p2 = (int(segment[1].split(',')[0]), int(segment[1].split(',')[1]))
    print('{} -> {}'.format(p1, p2))
    points = pointsOnSegment(p1, p2)
    for point in points:
        grid[point[0]][point[1]] += 1

count = sum([sum(list(map(lambda x: 0 if x < 2 else 1, row))) for row in grid])
print('overlapping squares: {}'.format(count))
