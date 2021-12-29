in_file = open('input.txt')
sonar_readings = [int(s) for s in in_file.readlines()]
cnt = 0
for i in range(len(sonar_readings)-1):
    if sonar_readings[i+1] > sonar_readings[i]:
        cnt += 1

print("sonar increases: {} out of {}".format(cnt, len(sonar_readings)))
