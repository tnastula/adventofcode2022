def perform_task():
    with open("input") as f:
        lines = f.readlines()

    visited = {0: {0}}  # x to y
    head_pos = (0, 0)
    rope = [(0, 0) for _ in range(9)]
    tail_index = len(rope) - 1

    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        delta_x = 0
        delta_y = 0

        if parts[0] == "U":
            delta_y += 1
        elif parts[0] == "D":
            delta_y -= 1
        elif parts[0] == "L":
            delta_x -= 1
        else:
            delta_x += 1

        for _ in range(int(parts[1])):
            head_pos = (head_pos[0] + delta_x, head_pos[1] + delta_y)
            for knot_index in range(len(rope)):
                if knot_index == 0:
                    prev = head_pos
                else:
                    prev = rope[knot_index - 1]
                rope[knot_index] = catch_up(prev, rope[knot_index])

            if rope[tail_index][0] not in visited:
                visited[rope[tail_index][0]] = set()
            visited[rope[tail_index][0]].add(rope[tail_index][1])
            # print("visited " + str(rope[tail_index][0]) + ", " + str(rope[tail_index][1]))

    pos_count = 0
    for key in visited:
        pos_count += len(visited[key])

    print(pos_count)


def catch_up(head_pos, tail_pos):
    delta_x = head_pos[0] - tail_pos[0]
    delta_y = head_pos[1] - tail_pos[1]

    if abs(delta_x) >= 2 and delta_y == 0:
        tail_pos = (tail_pos[0] + clamp(delta_x), tail_pos[1])
    elif abs(delta_y) >= 2 and delta_x == 0:
        tail_pos = (tail_pos[0], tail_pos[1] + clamp(delta_y))
    elif abs(delta_x) + abs(delta_y) >= 3:
        tail_pos = (tail_pos[0] + clamp(delta_x), tail_pos[1] + clamp(delta_y))

    return tail_pos


def clamp(number):
    if number < 0:
        return -1
    else:
        return 1


perform_task()
