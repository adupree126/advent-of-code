file = open('input')
crabs = [int(pos) for pos in file.readline()[:-1].split(',')]
file.close()


def fuel(pos):
    fuels = [abs(pos - crab) for crab in crabs]
    return sum(fuels)


# simple gradient descent algorithm
# the fuel consumption can be expressed as sum(|X - crab[n]|)
# absolute value functions have only one critical point, so
# a sum of absolute values has only one critical point
# therefore, we can just follow the slope to the minimum
x = int(sum(crabs)/len(crabs))  # start with the mean as a guess
dir = -1 if fuel(x + 1) > fuel(x) else 1  # get descent direction
while fuel(x) > fuel(x + 1) or fuel(x) > fuel(x - 1):
    print("at point: {}".format(x))
    x += dir
print('minimum @ {}, costing {}'.format(x, fuel(x)))
