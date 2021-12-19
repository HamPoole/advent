import copy
from collections import deque, defaultdict
from typing import Optional

input18 = open("/Users/urthor/projects/advent/advent_2021/day18/input18")

all_numbers = input18.readlines()
all_numbers = [x[:-1] for x in all_numbers]

snail_nums = [eval(x) for x in all_numbers]


def print_snail_nums(snail_nums):
    for x in snail_nums:
        print(x)


def access_matrix(matrix, indices) -> list:
    # To get a pointer to a mutable data structure in python you have to use a subscription.
    # Hence for say, matrix[1][0][1], this will return matrix[1][0]

    curr_level = matrix
    if indices:
        for val in indices:
            curr_level = curr_level[val]
    return curr_level


def fill_right_queue(curr_level, curr_level_indices, right_pointer_queue):
    for curr_index in range(len(curr_level[curr_level_indices[-1]])):
        if curr_level[curr_index].__class__() == int:
            right_pointer_queue.append(curr_level_indices + (curr_index,))
    return right_pointer_queue


def seek_right(matrix, indices):
    pass


seeking_right = False
right_val = -1

def traverse_matrix(matrix, curr_level_indices=(), left_pointer_stack=deque(), right_pointer_queue=deque()):


    curr_level = access_matrix(matrix, curr_level_indices[:-1])
    print(curr_level, "reached here")

    if len(curr_level_indices) >= 4:
        print(curr_level_indices)
        print(curr_level, "reachced here")
        print(curr_level[curr_level_indices[-1]])
        pair = curr_level[curr_level_indices[-1]]
        curr_level[curr_level_indices[-1]] = 0

        if left_pointer_stack:
            left_indices = left_pointer_stack.pop()
            first_left = access_matrix(matrix, left_indices[:-1])
            first_left[left_indices[-1]] += curr_level[curr_level_indices[-1]]
            # TODO: split

        if right_pointer_queue:
            right_indices = right_pointer_queue.popleft()
            first_right = access_matrix(matrix, right_indices[:-1])
            first_right[right_indices[-1]] = pair[1]
            # TODO split
            return pair[1], False
        else:
            # If no right pointer
            return pair[1], True

    # Fill the right stack:
    right_pointer_queue = fill_right_queue(curr_level, curr_level_indices, right_pointer_queue)
    if seeking_right and right_pointer_queue:
        right_val = 1

    for curr_index in range(len(curr_level[curr_level_indices[-1]])):
        value = curr_level[curr_level_indices[-1]][curr_index]

        print('here')
        print(value.__class__())

        if value.__class__() == int():
            left_pointer_stack.append(curr_level_indices + (curr_index,))
            right_pointer_queue.popleft()
        if value.__class__() == list():
            print('e')
            curr_indices = curr_level_indices + (curr_index,)
            right_val, seeking_right = traverse_matrix(matrix,
                                                       curr_indices,
                                                       copy.deepcopy(left_pointer_stack),
                                                       copy.deepcopy(right_pointer_queue))

            if seeking_right:
                return right_val, seeking_right

        elif isinstance(value, list) and len(value) < 2:
            print("fuckup")


start = (snail_nums[-1])


for x in range(len(start)):
    traverse_matrix(start, ())
result = traverse_matrix(start)
print(result)
[print(x) for x in snail_nums[-1]]
