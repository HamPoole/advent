def dfs_from_index(*, y_val, x_val):
    x = x_val
    y = y_val
    adjacent_indexes = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]

    size_of_basin = 1

    result = []

    for x in adjacent_indexes:
        my_tuple = (x[1], x[0])
        if my_tuple not in visited:
            visited.add(my_tuple)
            stack = [my_tuple]
            while stack and 10 not in stack[-1]:
                size_of_basin += dfs_from_index(y_val=stack[-1][1], x_val=stack[-1][0])
                stack.pop()

    return size_of_basin
