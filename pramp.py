def num_of_paths_to_dest(n):
    grid = [[x for x in range(n)] for x in range(n)]

    print(grid)

    class Tree:
        def __init__(self):
            self.val = None
            self.left = None
            self.right = None

    mytree = Tree


num_of_paths_to_dest(5)
