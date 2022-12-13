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

    max_score = 0
    for row_index in range(len(forest)):
        for col_index in range(len(forest[row_index])):
            score = scenic_score(forest, (row_index, col_index))
            if score > max_score:
                max_score = score

    print(max_score)


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


def scenic_score(forest, tree_pos):
    height = forest[tree_pos[0]][tree_pos[1]].height
    scenic_score = 1

    visible = 0
    for col_index in range(tree_pos[1] + 1, len(forest[0])):
        tree = forest[tree_pos[0]][col_index]
        visible += 1
        if height <= tree.height:
            break
    scenic_score *= visible

    visible = 0
    for col_index in range(tree_pos[1] - 1, -1, -1):
        tree = forest[tree_pos[0]][col_index]
        visible += 1
        if height <= tree.height:
            break
    scenic_score *= visible

    visible = 0
    for row_index in range(tree_pos[0] + 1, len(forest)):
        tree = forest[row_index][tree_pos[1]]
        visible += 1
        if height <= tree.height:
            break
    scenic_score *= visible

    visible = 0
    for row_index in range(tree_pos[0] - 1, -1, -1):
        tree = forest[row_index][tree_pos[1]]
        visible += 1
        if height <= tree.height:
            break
    scenic_score *= visible

    return scenic_score


class Tree:
    def __init__(self, height):
        self.height = int(height)
        self.visible = False


perform_task()
