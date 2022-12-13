def perform_task():
    with open("input") as f:
        lines = f.readlines()

    accumulator = 0
    for groupIndex in range(0, len(lines), 3):
        sets = [None] * 3
        for offset in range(0, 3):
            if offset == 0:
                subset_of = None
            else:
                subset_of = sets[offset - 1]
            sets[offset] = build_set(lines[groupIndex + offset].strip(), subset_of)
        accumulator += calc_priority(list(sets[2])[0])

    print(accumulator)


def calc_priority(character):
    priority = ord(character)
    if 96 < priority < 123:
        priority -= 96
    else:
        priority -= 38
    return priority


def build_set(line, subset_of = None):
    result = set()
    for character in line:
        if character not in result and (subset_of is None or character in subset_of):
            result.add(character)
    return result


perform_task()