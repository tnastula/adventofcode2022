def perform_task():
    with open("input") as f:
        lines = f.readlines()

    root = Node("/", None, 0, True)
    working_dir = None

    for line in lines:
        line = line.strip()
        parts = line.split(" ")
        if parts[0] == "$":
            if parts[1] == "cd":
                if parts[2] == "/":
                    working_dir = root
                elif parts[2] == "..":
                    working_dir = working_dir.parent
                else:
                    working_dir = working_dir.get_child(parts[2])
                    if working_dir is None:
                        print("Error: child not found")
        elif parts[0] == "dir":
            working_dir.add_child(Node(parts[1], working_dir, 0, True))
        else:
            working_dir.add_child(Node(parts[1], working_dir, int(parts[0]), False))

    total_space = 70000000
    required_space = 30000000
    used_space = root.size()
    available_space = total_space - used_space
    space_to_free = required_space - available_space
    best_so_far = used_space

    for size in root.dir_stats():
        if space_to_free <= size < best_so_far:
            best_so_far = size

    print(best_so_far)


class Node:
    def __init__(self, name, parent, own_size, is_directory):
        self.name = name
        self.parent = parent
        self.own_size = own_size
        self.is_directory = is_directory
        self.children = []

    def get_child(self, name):
        for child in self.children:
            if child.name == name:
                return child
        return None

    def add_child(self, child):
        self.children.append(child)

    def size(self):
        accumulator = self.own_size
        for child in self.children:
            accumulator += child.size()
        return accumulator

    def dir_stats(self, stats=[]):
        stats.append(self.size())
        for child in self.children:
            if child.is_directory:
                stats = child.dir_stats(stats)
        return stats


perform_task()
