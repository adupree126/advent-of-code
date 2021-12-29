in_file = open('input.txt')
readings = [int(s) for s in in_file.readlines()]
# readings = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

# find the windows
windows = [readings[i:i+3] for i in range(len(readings) - 2)]
window_sums = [sum(window) for window in windows]
# count the increasing ones
cnt = 0
for i in range(len(windows) - 1):
    if sum(windows[i+1]) > sum(windows[i]):
        cnt += 1
print("sonar window increases: {} out of {}".format(cnt, len(windows)))
