def perform_task():
    with open("input") as f:
        lines = f.readlines()

    monkeys = parse_lines(lines)
    rounds_to_perform = 10000

    master_mod = 1
    for monkey in monkeys:
        master_mod *= monkey.test_factor

    for cycle in range(rounds_to_perform):
        if cycle % 10 == 0:
            print("Cycle " + str(cycle))
        for monkey in monkeys:
            movements = monkey.process_round(master_mod)
            for movement in movements:
                monkeys[movement[1]].take_item(movement[0])

    monkeys.sort(key=get_activities_count, reverse=True)
    print(monkeys[0].activities_count * monkeys[1].activities_count)


def get_activities_count(monkey):
    return monkey.activities_count


def parse_lines(lines):
    monkeys = []
    for monkey_index in range(0, len(lines), 7):
        id = int(lines[monkey_index][7:-2])
        starting_items = []
        for item in lines[monkey_index + 1][18:].split(", "):
            starting_items.append(int(item))
        operation_symbol = lines[monkey_index + 2][23]
        operation_factor_string = lines[monkey_index + 2][25:].strip()
        if operation_factor_string == "old":
            operation_factor = None
        else:
            operation_factor = int(operation_factor_string)
        test_factor = int(lines[monkey_index + 3][21:])
        target_if_true = int(lines[monkey_index + 4][29:])
        target_if_false = int(lines[monkey_index + 5][30:])
        monkey = Monkey(id, starting_items, operation_symbol, operation_factor, test_factor, target_if_true, target_if_false)
        monkeys.append(monkey)
    return monkeys


class Monkey:
    def __init__(self, id, items, operation_symbol, operation_factor, test_factor, target_if_true, target_if_false):
        self.target_if_false = target_if_false
        self.target_if_true = target_if_true
        self.test_factor = test_factor
        self.operation_factor = operation_factor
        self.operation_symbol = operation_symbol
        self.items = items
        self.id = id
        self.activities_count = 0

    def process_round(self, master_mod):
        movements = []

        for item in self.items:
            self.activities_count += 1

            if self.operation_factor is None:
                operation_value = item
            else:
                operation_value = self.operation_factor

            if self.operation_symbol == "+":
                item = item + operation_value
            else:
                item = item * operation_value

            if item % self.test_factor == 0:
                movements.append((item % master_mod, self.target_if_true))
            else:
                movements.append((item % master_mod, self.target_if_false))

        self.items = []
        return movements

    def take_item(self, item):
        self.items.append(item)


perform_task()
