# count the number of times a depth measurement increases


with open(file="/advent_2021/day1/input/input1",
          mode='r') as input1:
    input_one = input1.read().split()

print(input_one[:5])

test = ['176', '184', '196', '199', '204']
test2 = ['1', '2', '1', '3', '4']

input_one_int = [int(x) for x in input_one]

loop_input = input_one_int


def part1(x):
    increase_count = 0

    for index in range(1, len(loop_input)):
        equal_test = (loop_input[index - 1] < loop_input[index])
        if equal_test:
            increase_count += 1

        print(loop_input[index - 1], loop_input[index], equal_test, print(type(loop_input[index])))

    print(increase_count)


def part2(x):
    window_count = 0

    for index in range(1, len(loop_input)):
        first_var = sum(loop_input[index - 1:index + 2]) / 3
        second_var = sum(loop_input[index:index + 3]) / 3
        equal_test = (first_var < second_var)
        if equal_test:
            window_count += 1

        print(first_var, second_var, equal_test, print(type(first_var)))

    print(window_count)


part2(input_one)
