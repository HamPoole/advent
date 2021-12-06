import numpy as np
import pandas

with open(file="/home/urthor/projects/advent_of_code/advent_2021/day5/input/input5",
          mode='r') as input1:
    input_file = input1.readlines()

input_file = input_file

cleaned_d5 = [x[:-1] for x in input_file]

grid_size = range(1000)

grid = [[0 for y in grid_size] for x in grid_size]
numpy_grid = np.array(grid)
numpy_grid2 = np.array(grid)


class coords:
    x: int
    y: int

    def __init__(self, x, y):
        self.x: int = y
        self.y: int = x


class line:
    start: coords
    end: coords

    def __init__(self, start: coords, end: coords):
        self.start = start
        self.end = end


lines = []

for val in cleaned_d5:
    # Example val '409,872 -> 409,963'
    arrow_split = val.split('->')
    split_val = [x.split(',') for x in arrow_split]

    first_x = int(split_val[0][0])
    first_y = int(split_val[0][1].strip())
    last_x = int(split_val[1][0])
    last_y = int(split_val[1][1].strip())

    line_start: coords = coords(first_x, first_y)

    line_end: coords = coords(last_x, last_y)

    lines.append(line(line_start, line_end))


def apply_nonzero_gradient(line, grid1, grid2):
    gradient = (line.end.y - line.start.y) / (line.end.x - line.start.x)
    values = (line.start.x, line.start.y, line.end.x, line.end.y)

    if gradient > 0:
        sorted_x = sorted((line.end.x, line.start.x))
        y_val = min((line.end.y, line.start.y))

        for x_val in range(sorted_x[0], sorted_x[1] + 1 ):
            grid1[x_val][y_val] += 1
            grid2[x_val][y_val] += 1
            print(values)
            y_val += 1 # if y_val < line.end.y else y_val

    if gradient < 0:

        sorted_x = sorted((line.end.x, line.start.x))
        y_val = max((line.end.y, line.start.y))

        for x_val in range(sorted_x[0], sorted_x[1] + 1):
            grid1[x_val][y_val] += 1
            grid2[x_val][y_val] += 1
            y_val -= 1


def apply_line_to_grid(line, grid1, grid2):
    values = (line.start.x, line.start.y, line.end.x, line.end.y)
    # print(values)

    if line.end.x == line.start.x:

        sorted_y = sorted((line.end.y, line.start.y))

        # 913 445 913 958
        # QD. AJW
        # 432 125 432 795

        for y in range(sorted_y[0], sorted_y[1] + 1):
            grid1[line.end.x][y] += 1
            grid2[line.end.x][y] += 1

    elif line.end.y == line.start.y:

        sorted_x = sorted((line.end.x, line.start.x))

        for x in range(sorted_x[0], sorted_x[1] + 1):
            grid1[x][line.end.y] += 1
            grid2[x][line.end.y] += 1
    else:

        apply_nonzero_gradient(line, grid1, grid2)


column_labels = [x for x in grid_size]
row_labels = [y for y in grid_size]

my_df = pandas.DataFrame(numpy_grid, column_labels, row_labels)

print(len(lines))
for line in lines:
    apply_line_to_grid(line, grid1=grid, grid2=numpy_grid2)
print(len(lines))
print("look here 3")
mag2_count = 0

print(type(numpy_grid2))

for x in grid_size:
    for y in grid_size:
        val = numpy_grid2[x][y]
        if val > 1:
            mag2_count += 1

print(mag2_count)

my_df2 = pandas.DataFrame(numpy_grid2, column_labels, row_labels)

print(my_df2)

my_df2.to_csv(path_or_buf="/home/urthor/projects/advent_of_code/advent_2021/day5/input/csv1")
