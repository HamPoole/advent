from collections import deque

with open("/home/urthor/projects/advent_of_code/advent_2021/day10/input10") as input1:
    myinput = input1.readlines()

print(myinput)
cleaned = [x[:-1] for x in myinput]
print(cleaned)

left_bracket_types = '<([{'
# bracket_lookup = {key: val for key, val in '}])>', '<([{'}

right_bracket_lookup = {'}': '{', ']': '[', ')': '(', '>': '<'}

bad_val_score = {'}': 1197, ']': 57, ')': 3, '>': 25137}

corrupt_score = 0

cleaned_2 = list(cleaned)

for line in cleaned:

    boring_stack = []

    for char_index in line:

        if char_index not in right_bracket_lookup.keys():
            boring_stack.append(char_index)
            print(boring_stack)
        elif char_index in right_bracket_lookup:
            stack_top = boring_stack.pop()
            if right_bracket_lookup[char_index] != stack_top:
                corrupt_score += bad_val_score[char_index]
                cleaned_2.remove(line)
                break

print(corrupt_score)

left_bracket_lookup = {'}': '{', ']': '[', ')': '(', '>': '<'}

left_bracket_lookup = {value: key for key, value in left_bracket_lookup.items()}

score2_dict = {'{': 3, '[': 2, '(': 1, '<': 4}

all_scores = []

for line in cleaned_2:
    score_2 = 0

    boring_stack = []
    remainder = []

    my_deque = deque(line)
    for char_index in range(len(line)):
        if my_deque[char_index] not in right_bracket_lookup.keys():
            boring_stack.append(my_deque[char_index])
        else:
            stack_top = boring_stack.pop()
            if my_deque[char_index] != stack_top:
                remainder.append(my_deque[char_index])

    print(boring_stack)

    for char in boring_stack[::-1]:
        score_2 *= 5
        # print(score_2)
        score_2 += score2_dict[char]
        # print(score_2)

    all_scores.append(score_2)
    print(score_2)

print(all_scores)
sort_me = list(all_scores)
sort_me.sort()
print(sort_me)
print(sort_me[len(sort_me) - 1 - len(sort_me)//2])