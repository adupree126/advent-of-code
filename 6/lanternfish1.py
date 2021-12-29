file = open('input')
fish = [int(f) for f in file.readline()[:-1].split(',')]
counts = [fish.count(n) for n in range(7)] + [0, 0]
print(counts)
daysLeft = 256   # the days to track the fish

while daysLeft > 0:
    newCounts = counts[1:] + [counts[0]]  # the new fish
    newCounts[6] += counts[0]           # reset the fish that just split
    counts = newCounts
    daysLeft -= 1
    if daysLeft % 10 == 0:
        print('{} days left: {} ({})'.format(daysLeft, sum(counts), counts))

print('final fish count: {}'.format(sum(counts)))
