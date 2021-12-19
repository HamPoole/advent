import copy
import heapq
from collections import defaultdict

"""
Destination value is the edge weight

"""

lines = open("/home/urthor/projects/advent_of_code/advent_2021/day15/input15").read().split('\n')

matrix = [list(map(int, row)) for row in lines]


def print_matrix(matrix):
    for x in range(len(matrix)):
        print(matrix[x])


def get_neighbours(matrix, x, y):
    # ty maxkvant
    moves = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    length_y = len(matrix)
    length_x = len(matrix[0])
    for dx, dy in moves:
        neighbour_x = x + dx
        neighbour_y = y + dy
        if 0 <= neighbour_x < length_x and 0 <= neighbour_y < length_y:
            yield neighbour_x, neighbour_y


visited = copy.deepcopy(matrix)
visited = [[-1 for x in row] for row in visited]
weights = copy.deepcopy(matrix)

moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def dijkstra(matrix):
    height = len(matrix)
    width = len(matrix[0])
    source = (0, 0)
    destination = matrix[-1][-1]

    def node_with_source_dist(*, dist_from_source, node: tuple):
        return {node: dist_from_source}

    queue_to_visit = [(dist_from_source=0, node=(0, 0))]
    min_distance = defaultdict(lambda: (float('inf'), node_with_source_dist(dist_from_source=0, node=source)))

    visited = set()

    while queue_to_visit:
        current_distance, node = heapq.heappop(queue_to_visit)

        if node == destination:
            return current_distance

        if node in visited:
            continue

        visited.add(node)

        row, col = node  # row and col are better than x and y because the y is first in a row wise array

        for neighbour in get_neighbours(matrix, row, col):

            if neighbour in visited:
                continue

            neighbour_row, neighbour_col = neighbour

            new_distance = current_distance + matrix[neighbour_row][neighbour_col]
            # Calculate total distance from source by getting the current total of weights and the weight of neighbour

            if new_distance < min_distance[neighbour]:
                min_distance[neighbour] = new_distance
                heapq.heappush(queue_to_visit, node_with_source_dist(dist_from_source=new_distance, node=neighbour))

    return "No path"


min_dist = dijkstra(matrix)

print("pt1", min_dist)
