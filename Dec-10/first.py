def perform_task():
    with open("input") as f:
        lines = f.readlines()

    register_at_cycle = {1: 1}
    current_cycle = 1

    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        current_value = register_at_cycle[current_cycle]
        if parts[0] == "noop":
            register_at_cycle[current_cycle + 1] = current_value
            current_cycle += 1
        elif parts[0] == "addx":
            register_at_cycle[current_cycle] = current_value
            register_at_cycle[current_cycle + 1] = current_value
            register_at_cycle[current_cycle + 2] = current_value + int(parts[1])
            current_cycle += 2

    accumulator = 0
    for cycle in range(20, 221, 40):
        accumulator += register_at_cycle[cycle] * cycle

    print(accumulator)


perform_task()
