from collections import defaultdict

input15 = open("/Users/urthor/projects/advent/advent_2021/day15/input15")

matrix = input15.read().split('\n')


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


print_matrix(matrix)


def dijkstra(matrix):
    height, width = len(matrix), len(matrix[0])
    source = (0, 0)
    destination_coords = (height -1, width - 1)

    queue = [(0, source)] # A list can be a queue if you just treat the back as the end.
    mindist = defaultdict(lambda: int(float('inf')), {source: 0})
    # Above is a dictionary with a default value for key not found.
    # If a key is not found in dictionary returns error
    visited = set()

    while queue:

        current_distance_from_source, current_node_coords = heapq.heappop(queue)

        if current_node_coords == destination_coords:
            return current_distance_from_source

        if current_node_coords in visited:
            continue
