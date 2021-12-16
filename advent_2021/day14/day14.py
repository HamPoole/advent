from collections import Counter

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day14/input14") as myinput:
    input_file = myinput.readlines()

input_text = [x[:-1] for x in input_file]

first_line = input_text[0]

to_split = [x for x in input_text[2:]]

print(to_split)

split_mapping = {key[:2]: -1 for key in to_split}

for index in range(len(split_mapping.keys())):
    key = to_split[index][:2]
    split_mapping[key] = key[0] + to_split[index][-1] + key[1]

print(split_mapping)

memoizer = {}


def hash_table_pass(x):
    return_string = ""

    pair = x[0: 0 + 2]
    mapping = split_mapping[pair]
    return_string += mapping

    for index in range(1, len(x) - 1, +1):
        # for every pair starting from the first character, until the pair starting at the second to last character
        # with step size 1
        pair = x[index: index + 2]
        mapping = split_mapping[pair]
        return_string += mapping[1:]

    memoizer[x] = mapping
    return return_string

for index in range(1, len(first_line)):


def counetr_pass(a_counter):






problem_input = str(first_line)

for number in range(10):
    print(number, "up to this")
    print(len(problem_input))
    problem_input = hash_table_pass(problem_input)

a = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
b = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'

print(a == b)

counter = Counter(problem_input)
print(counter)
print(max(counter.values()) - min(counter.values()))

print(split_mapping)
print(Counter(split_mapping))

counter = Counter(split_mapping)
seg_counter = Counter(split_mapping[i:i + 2] for i in range(len(split_mapping) - 1))
print(counter)
print(seg_counter)
