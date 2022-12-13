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

    text = ""
    for cycle in range(1, current_cycle):
        screen_pos = cycle % 40
        sprite_pos = register_at_cycle[cycle]

        if sprite_pos - 1 <= screen_pos - 1 <= sprite_pos + 1:
            text += "#"
        else:
            text += "."

        if screen_pos == 0:
            print(text)
            text = ""


perform_task()
