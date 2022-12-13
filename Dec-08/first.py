def perform_task():
    with open("input") as f:
        lines = f.readlines()

    # Mark edges as visible immediately
    # NxM O(2(N-2)+2(M-2))
    row_count = len(lines)
    col_count = len(lines[0].strip())
    forest = [[None] * col_count for _ in range(row_count)]

    for row_index in range(row_count):
        line = lines[row_index].strip()
        for col_index in range(col_count):
            height = line[col_index]
            tree = Tree(height)
            if row_index == 0 or row_index == row_count - 1 or col_index == 0 or col_index == col_count - 1:
                tree.visible = True
            forest[row_index][col_index] = tree

    for row_index in range(row_count):
        forest = verify_forest_file(forest, (0, 1), (row_index, 0))
        forest = verify_forest_file(forest, (0, -1), (row_index, col_count - 1))

    for col_index in range(col_count):
        forest = verify_forest_file(forest, (1, 0), (0, col_index))
        forest = verify_forest_file(forest, (-1, 0), (row_count - 1, col_index))

    visible_count = 0
    for row in forest:
        for tree in row:
            if tree.visible:
                visible_count += 1

    print(visible_count)


def verify_forest_file(forest, delta_step, start_pos):
    tallest = 0
    current_row = int(start_pos[0])
    current_col = int(start_pos[1])
    while len(forest) > current_row >= 0 and len(forest[0]) > current_col >= 0:
        tree = forest[current_row][current_col]
        if tree.height > tallest:
            tree.visible = True
            tallest = tree.height
        current_row += delta_step[0]
        current_col += delta_step[1]
    return forest


class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False


perform_task()
