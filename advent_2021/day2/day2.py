with open(file="/home/urthor/projects/advent_of_code/advent_2021/day2/input/input_day2",
          mode='r') as input1:
    input_day2 = input1.readlines()

print(input_day2[:5])

# x and y start at 0, 0, depth is y horizontal is x


cleaned_d2 = [x[:-1] for x in input_day2]

print(cleaned_d2[-4:])

horizontal = 0
depth = 0

aim = 0

test1 = ['forward 5',
         'down 5',
         'forward 8',
         'up 3',
         'down 8',
         'forward 2']

for command in cleaned_d2:

    if 'forward' in command:

        horizontal += int(command[-1])

        depth += aim * int(command[-1])

    elif 'down' in command:

        # depth += int(command[-1])
        aim += int(command[-1])

    elif 'up' in command:

        # depth -= int(command[-1])
        aim -= int(command[-1])

    else:

        print(command)

print(horizontal, depth, horizontal * depth, aim)
