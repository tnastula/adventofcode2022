with open("input") as f:
    lines = f.readlines()

accumulator = 0
for line in lines:
    line = line.strip()
    first = set()
    for character in line[:len(line)//2]:
        if character not in first:
            first.add(character)
    for character in line[len(line)//2:]:
        if character in first:
            priority = ord(character)
            if 96 < priority < 123:
                priority -= 96
            else:
                priority -= 38
            accumulator += priority
            break

print(accumulator)