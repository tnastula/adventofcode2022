from queue import PriorityQueue

def perform_task():
    with open("input") as f:
        lines = f.readlines()

    node_map = NodeMap(lines)
    print(node_map.get_distance())


class NodeMap:
    def __init__(self, lines):
        self.end_node = None
        self.start_nodes = []
        self.nodes = []
        self.build(lines)

    def build(self, lines):
        self.nodes = []
        for line_index in range(len(lines)):
            row = []
            line = lines[line_index].strip()
            for symbol_index in range(len(line)):
                symbol = line[symbol_index]
                node = Node((symbol_index, line_index), symbol)
                if symbol == "S" or symbol == "a":
                    node.symbol = "a"
                    self.start_nodes.append(node)
                elif symbol == "E":
                    node.symbol = "z"
                    self.end_node = node
                if symbol_index > 0:
                    node.build_edge(row[symbol_index - 1], True)
                if line_index > 0:
                    node.build_edge(self.nodes[line_index - 1][symbol_index], True)
                row.append(node)
            self.nodes.append(row)

    def get_distance(self):
        min_distance = None

        for start_node in self.start_nodes:
            for row in self.nodes:
                for node in row:
                    node.cost_from_start = None
                    node.prev_node = None
            start_node.cost_from_start = 0

            queue = PriorityQueue()
            queue.put((start_node.cost_from_start, start_node.address, start_node))
            while not queue.empty():
                current_node = queue.get()[2]
                for edge in current_node.edges:
                    cost_to_reach = current_node.cost_from_start + edge.cost
                    if edge.destination.cost_from_start is None or edge.destination.cost_from_start > cost_to_reach:
                        edge.destination.cost_from_start = cost_to_reach
                        edge.destination.prev_node = current_node
                        queue.put((edge.destination.cost_from_start, edge.destination.address, edge.destination))

            current = self.end_node
            distance = 0
            while current is not None:
                current = current.prev_node
                distance += 1
            distance -= 1

            if (min_distance is None or min_distance > distance) and distance > 0:
                min_distance = distance

        return min_distance


class Node:
    def __init__(self, address, symbol):
        self.address = address
        self.symbol = symbol
        self.cost_from_start = None
        self.prev_node = None
        self.edges = []

    def height(self):
        return ord(self.symbol) - 97

    def update_route(self, prev_node, cost_from_start):
        self.prev_node = prev_node
        self.cost_from_start = cost_from_start

    def is_edge_possible(self, other_node):
        if other_node.height() - self.height() <= 1:
            return True
        else:
            return False

    def build_edge(self, other_node, reverse):
        if not self.is_edge_possible(other_node):
            return

        edge = next(
            (obj for obj in self.edges if obj.destination == other_node),
            None
        )

        if edge is None:
            edge = Edge(self, other_node)
            self.edges.append(edge)

        if reverse:
            other_node.build_edge(self, False)


class Edge:
    def __init__(self, origin, destination):
        self.cost = 1
        self.origin = origin
        self.destination = destination


perform_task()
