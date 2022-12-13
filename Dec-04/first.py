def perform_task():
    with open("input") as f:
        lines = f.readlines()

    fully_containing_the_other = 0
    for index in range(len(lines)):
        line = lines[index].strip()
        range_sections = line.split(",")
        ranges = [ElfRange(range_sections[0]), ElfRange(range_sections[1])]
        if ranges[0].contained_in(ranges[1]) or ranges[1].contained_in(ranges[0]):
            fully_containing_the_other += 1

    print(fully_containing_the_other)


class ElfRange:
    def __init__(self, range_description):
        range_nums = range_description.split("-")
        self.lower = int(range_nums[0])
        self.upper = int(range_nums[1])

    def contained_in(self, other_range):
        if other_range.lower <= self.lower <= other_range.upper \
           and other_range.upper >= self.upper >= other_range.lower:
            return True
        else:
            return False


perform_task()
