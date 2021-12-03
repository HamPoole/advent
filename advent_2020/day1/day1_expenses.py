with open(file="/home/urthor/projects/advent_of_code/advent_2020/day1/input/input",
          mode='r') as input1:
    problem_input = input1.read().split()

print(problem_input[:5])
problem_input = [int(x) for x in problem_input]

target = 2020

target = 2020

numbers = set(tuple(problem_input))

for number in problem_input:

    if target - number in numbers:
        print(number, target - number, number * (target - number))

sorted_input = list(problem_input)

sorted_input.sort()

for i in sorted_input:
    for j in sorted_input:

        if target - i - j in numbers:
            print((target - i - j) * i * j)
