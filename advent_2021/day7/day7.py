with open(file="/home/urthor/projects/advent_of_code/advent_2021/day7/input7",
          mode='r') as input7:
    input_file = input7.read()

data = input_file.split(',')
data = [int(x) for x in data]

print(data[:5])

print(max(data))

min_distance = 2 ** 32 - 1

for value in range(max(data)):

    distances = [sum([x for x in range(1, abs(value - x) + 1)]) for x in data]
    print(distances)

    mean_dist = (sum(distances))
    min_distance = min(mean_dist, min_distance)

print(min_distance)

