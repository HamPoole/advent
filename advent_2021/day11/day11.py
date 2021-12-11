import copy

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day11/input11") as myinput:
    input_file = myinput.readlines()

cleaned_matrix = [x[:-1] for x in input_file]

for index in range(len(cleaned_matrix)):
    cleaned_matrix[index] = list((map(int, cleaned_matrix[index])))

clean_flashed = copy.deepcopy(cleaned_matrix)
clean_flashed = [[0 for x in y] for y in clean_flashed]

print(cleaned_matrix)
print(clean_flashed)
print([len(y) for y in clean_flashed])
print([len(y) for y in cleaned_matrix])

moves = [(0, -1), (0, 1), (1, 0), (-1, 0), (-1, -1), (1, 1), (1, -1), (-1, 1)]

flash_count = 0


def get_neighbours(matrix, x, y):
    # ty maxkvant
    length_y = len(matrix)
    length_x = len(matrix[0])
    for dx, dy in moves:
        neighbour_x = x + dx
        neighbour_y = y + dy
        if 0 <= neighbour_x < length_x and 0 <= neighbour_y < length_y:
            yield neighbour_x, neighbour_y


class my_matrices:
    cavern: list
    flashed: list
    flash_count: int
    first_step: int

    def __init__(self, octo_matrix, octo_flash):
        self.cavern = octo_matrix
        self.flashed = octo_flash
        self.flash_count = 0
        self.first_step = 0


def flash(matrices, x, y):
    matrices.flash_count += 1
    matrices.flashed[y][x] = 1
    for neighbour_x, neighbour_y in get_neighbours(matrices.cavern, x, y):
        update_octopus(matrices, neighbour_x, neighbour_y)


def update_octopus(matrices, x, y):
    if matrices.flashed[y][x] <= 0:
        matrices.cavern[y][x] += 1
    if matrices.cavern[y][x] > 9 and matrices.flashed[y][x] <= 0:
        matrices.cavern[y][x] = 0
        flash(matrices, x, y)


def print_matrix(matrix):
    for x in range(len(matrix)):
        print(matrix[x])


def loop_through_matrix(matrix):
    for y in range(len(matrix.cavern)):
        for x in range(len(matrix.cavern)):
            update_octopus(matrices_struct, x, y)
            # if step == 2 and x == 0 and y == 0:
            #     return


steps = 1000

matrices_struct = my_matrices(cleaned_matrix, copy.deepcopy(clean_flashed))

for step in range(steps):
    loop_through_matrix(matrices_struct)

    matrices_struct.flashed = copy.deepcopy(clean_flashed)

    if matrices_struct.cavern == copy.deepcopy(clean_flashed) and matrices_struct.first_step == 0:
        matrices_struct.first_step = step + 1

print(matrices_struct.flash_count)
print(matrices_struct.first_step)
