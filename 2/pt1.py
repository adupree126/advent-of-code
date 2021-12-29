lines = open('input').readlines()
directions = [line.split(' ') for line in lines]  # e.g ['forward', 2]
depth = 0
position = 0
for direction in directions:
    if direction[0] == 'forward':
        position += int(direction[1])
    elif direction[0] == 'up':
        depth -= int(direction[1])
    elif direction[0] == 'down':
        depth += int(direction[1])
    else:
        print("bad input " + direction)
print("height: {}\nposition: {}\nproduct: {}".format(
    depth, position, depth*position))
