import functools


def perform_task():
    with open("input") as f:
        lines = f.readlines()

    lines.append("[[2]]")
    lines.append("[[6]]")

    packets = []
    for line_index in range(len(lines)):
        line = lines[line_index].strip()
        if line.strip() == "":
            continue
        packets.append(extract_substatement(line, 0)[1])

    packets.sort(key=functools.cmp_to_key(compare), reverse=True)

    result = 1
    result *= next((i for i, item in enumerate(packets) if item.body == "[[2]]"), -1) + 1
    result *= next((i for i, item in enumerate(packets) if item.body == "[[6]]"), -1) + 1

    print(result)


def extract_substatement(body, from_index):
    children = []

    nums = [str(num) for num in range(10)]
    number_accumulator = ""
    wait_for_index = -1
    for symbol_index in range(from_index + 1, len(body)):
        if symbol_index <= wait_for_index:
            continue
        symbol = body[symbol_index]
        if symbol == "[":
            if number_accumulator != "":
                children.append(Word(number_accumulator))
                number_accumulator = ""
            result = extract_substatement(body, symbol_index)
            wait_for_index = result[0]
            children.append(result[1])
        elif symbol == "]":
            if number_accumulator != "":
                children.append(Word(number_accumulator))
            child = Statement(body[from_index:symbol_index + 1], children)
            return (symbol_index, child)
        elif symbol in nums:
            number_accumulator += symbol
        else:
            if number_accumulator != "":
                children.append(Word(number_accumulator))
                number_accumulator = ""


def compare(left, right):
    length = right.length()

    if left.length() > right.length():
        length = left.length()

    for element_index in range(length):
        if not left.within_bounds(element_index):
            return 1
        elif not right.within_bounds(element_index):
            return -1

        curr_left = left.children[element_index]
        curr_right = right.children[element_index]

        if isinstance(curr_left, Statement) and isinstance(curr_right, Word):
            temp_statement = Statement("[" + str(curr_right) + "]", [curr_right])
            result = compare(curr_left, temp_statement)
            if result != 0:
                return result
            else:
                continue

        if isinstance(curr_left, Word) and isinstance(curr_right, Statement):
            temp_statement = Statement("[" + str(curr_left) + "]", [curr_left])
            result = compare(temp_statement, curr_right)
            if result != 0:
                return result
            else:
                continue

        if isinstance(curr_left, Statement) and isinstance(curr_right, Statement):
            result = compare(curr_left, curr_right)
            if result != 0:
                return result
            else:
                continue

        if isinstance(curr_left, Word) and isinstance(curr_right, Word):
            if curr_left.value == curr_right.value:
                continue
            elif curr_left.value < curr_right.value:
                return 1
            else:
                return -1
    return 0


class Statement:
    def __init__(self, body, children):
        self.body = body
        self.children = children

    def length(self):
        return len(self.children)

    def within_bounds(self, index):
        return index < self.length()


class Word:
    def __init__(self, value):
        self.value = int(value)


perform_task()
