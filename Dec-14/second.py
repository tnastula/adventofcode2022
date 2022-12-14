def perform_task():
    spawn_point = (500, 0)
    map = Map([spawn_point])

    with open("input") as f:
        lines = f.readlines()

    for line in lines:
        line = line.strip()
        map.add_rocks(line)

    floor_y = map.max_rock_y + 2
    map.add_rocks("0," + str(floor_y) + " -> 999," + str(floor_y))

    while map.execute_step():
        pass

    print(map.rested)


class Map:
    def __init__(self, spawn_points):
        self.map = [["." for _ in range(1000)] for _ in range(1000)]
        self.spawn_points = spawn_points
        self.max_rock_y = None
        self.sand_pos = None
        self.rested = 0

    def add_rocks(self, input_line):
        coords = []
        line_parts = input_line.split(" ")
        for coord_index in range(0, len(line_parts), 2):
            coords_raw = line_parts[coord_index].split(",")
            coords.append((int(coords_raw[0]), int(coords_raw[1])))
        for coord_index in range(1, len(coords)):
            prev_coord = coords[coord_index - 1]
            coord = coords[coord_index]
            delta_x = coord[0] - prev_coord[0]
            if delta_x > 0:
                delta_x = 1
            elif delta_x < 0:
                delta_x = -1
            delta_y = coord[1] - prev_coord[1]
            if delta_y > 0:
                delta_y = 1
            elif delta_y < 0:
                delta_y = -1

            current = prev_coord
            self.map[current[1]][current[0]] = "#"
            self.register_min_rock_y(current[1])
            while current[0] != coord[0] or current[1] != coord[1]:
                current = (current[0] + delta_x, current[1] + delta_y)
                self.map[current[1]][current[0]] = "#"
                self.register_min_rock_y(current[1])
            self.map[current[1]][current[0]] = "#"
            self.register_min_rock_y(current[1])

    def execute_step(self):
        if self.sand_pos is None:
            self.sand_pos = (self.spawn_points[0][0], self.spawn_points[0][1])
            return True
        elif self.map[self.sand_pos[1] + 1][self.sand_pos[0]] == ".":
            self.sand_pos = (self.sand_pos[0], self.sand_pos[1] + 1)
            return True
        elif self.map[self.sand_pos[1] + 1][self.sand_pos[0] - 1] == ".":
            self.sand_pos = (self.sand_pos[0] - 1, self.sand_pos[1] + 1)
            return True
        elif self.map[self.sand_pos[1] + 1][self.sand_pos[0] + 1] == ".":
            self.sand_pos = (self.sand_pos[0] + 1, self.sand_pos[1] + 1)
            return True
        elif self.sand_pos != self.spawn_points[0]:
            self.map[self.sand_pos[1]][self.sand_pos[0]] = "o"
            self.sand_pos = None
            self.rested += 1
            return True

        self.rested += 1
        return False

    def register_min_rock_y(self, y):
        if self.max_rock_y is None:
            self.max_rock_y = y
        elif y > self.max_rock_y:
            self.max_rock_y = y

    def print(self):
        for row in self.map:
            row_text = ""
            for cell in row:
                row_text += cell
            print(row_text)


perform_task()
