def perform_task():
    with open("input") as f:
        lines = f.readlines()

    first_command_index = None

    for index in range(len(lines)):
        line = lines[index].strip()
        if not line:
            first_command_index = index + 1

    stacks = parse_stacks(first_command_index, lines)

    for command_index in range(first_command_index, len(lines)):
        command = lines[command_index]
        command_parts = command.split(" ")
        count = int(command_parts[1])
        source = int(command_parts[3]) - 1
        target = int(command_parts[5]) - 1
        for _ in range(count):
            cargo = stacks[source].pop()
            stacks[target].append(cargo)

    for stack in stacks:
        print(stack.pop())


def parse_stacks(first_command_index, lines):
    stacks_ids_index = first_command_index - 2
    stacks_bottom = first_command_index - 3

    stacks_count = int(lines[stacks_ids_index].strip()[-1])
    stacks = [[] for _ in range(stacks_count)]

    for index in range(stacks_bottom, -1, -1):
        line = lines[index]
        for stack_index in range(0, stacks_count, 1):
            char_index = (stack_index + 1) * 4 - 3
            if char_index >= len(line):
                break
            if line[char_index] == " ":
                continue
            stacks[stack_index].append(line[char_index])

    return stacks


perform_task()
