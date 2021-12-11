import resource
import sys

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day9/input9",
          mode='r') as input9:
    input_file = input9.readlines()

cleaned = [[int(y) for y in (x[:-1])] for x in input_file]


matrix = cleaned

lower_bound = -1
upper_bound_x = len(matrix[0])
upper_bound_y = len(matrix)

padded_matrix = [[10] + d + [10] for d in matrix]
padded_matrix = [[10 for c in range(len(matrix[0]) + 1)]] + padded_matrix + [[10 for c in range(len(matrix[0]) + 1)]]


low_points = []
low_points_indices = []

visited = set()


def dfs_from_index(*, y_val, x_val, prev_val):
    x = x_val
    y = y_val
    adjacent_indexes1 = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

    size_of_basin = 1

    for x in adjacent_indexes1:
        my_tuple = (x[1], x[0])
        curr_val = padded_matrix[x[1]][x[0]]

        if my_tuple not in visited and 9 > curr_val > prev_val:
            print(prev_val, curr_val)

            visited.add(my_tuple)
            val = dfs_from_index(y_val=my_tuple[0],
                                 x_val=my_tuple[1],
                                 prev_val=prev_val)
            size_of_basin += val

    return size_of_basin


for y in range(1, len(padded_matrix) - 1):
    print("row")
    for x in range(1, len(padded_matrix[1]) - 1):
        x_axis_val = x
        adjacent_indexes = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

        current = padded_matrix[y][x]
        adjacents = []
        for a in adjacent_indexes:
            val = padded_matrix[a[1]][a[0]]
            adjacents += [val]

        if current < min(adjacents):
            low_points.append(current)
            low_points_indices.append([y, x])

print(low_points)
print(low_points_indices)

result = [x + 1 for x in low_points]
print(sum(result))


# resource.setrlimit(resource.RLIMIT_STACK, (2 ** 41, -1))
# sys.setrecursionlimit(2 ** 25)

max_3_size = [-1, -1, -1]
for low_point in low_points_indices:
    print("prev val", padded_matrix[low_point[0]][low_point[1]])
    size_of_basin1 = dfs_from_index(y_val=low_point[0],
                                    x_val=low_point[1],
                                    prev_val=padded_matrix[low_point[0]][low_point[1]])

    print(size_of_basin1)
    max_3_size.sort()
    if size_of_basin1 > max_3_size[0]:
        max_3_size[0] = size_of_basin1

print(max_3_size)


print(max_3_size[0] * max_3_size[1] * max_3_size[2])

import re

import cv2
import numpy as np
from scipy.ndimage import label

import aoc_helper

RAW = aoc_helper.day(9)

CAVE_MAP = np.fromiter(map(int, re.findall(r"\d", RAW)), dtype=int).reshape(100, 100)

def part_one():
    border_map = np.pad(CAVE_MAP, 1, mode="constant", constant_value=9)

    mask = (
            (CAVE_MAP < border_map[2:   , 1: -1])
            & (CAVE_MAP < border_map[ : -2, 1: -1])
            & (CAVE_MAP < border_map[1: -1, 2:   ])
            & (CAVE_MAP < border_map[1: -1,  : -2])
    )
    return (CAVE_MAP[mask] + 1).sum()

def part_two():
    labels, nbins = label(CAVE_MAP != 9)
    labels = labels.reshape(-1)

    return np.partition(np.bincount(labels, labels != 0), nbins - 3)[-3:].prod().astype(int)