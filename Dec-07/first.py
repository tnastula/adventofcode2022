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

    print(root.find())


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

    def find(self):
        max_size = 100000
        accumulator = 0

        size_of_me = self.size()
        if size_of_me <= max_size:
            accumulator += size_of_me

        for child in self.children:
            if child.is_directory:
                accumulator += child.find()

        return accumulator


perform_task()
