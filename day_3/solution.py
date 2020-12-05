from typing import List, NoReturn


class Trajectory:
    def __init__(self, input_file: str):
        self.map = self.read_input(input_file)
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.pos_x = 0
        self.pos_y = 0
        self.tree_hits = 0

    def take_step(self, right_step: int, down_step: int) -> NoReturn:
        self.pos_x = (self.pos_x + right_step) % self.width
        self.pos_y = self.pos_y + down_step
        self.update_trees()

    def update_trees(self) -> NoReturn:
        self.tree_hits += self.location_has_tree(self.pos_x, self.pos_y)

    def location_has_tree(self, x_pos: int, y_pos: int) -> bool:
        if x_pos >= self.width:
            print("Width out of map")
            return False
        if y_pos >= self.height:
            print("Height out of map")
            return False
        return self.map[y_pos][x_pos] == "#"

    def read_input(self, input_file) -> List[str]:
        pw_file = open(input_file, "rb+")
        pw_lines = pw_file.readlines()
        return [pw_line.decode("utf-8").strip() for pw_line in pw_lines]

    def get_tree_hits(self) -> int:
        return self.tree_hits

    def travel(self, right: int, down: int) -> NoReturn:
        while self.pos_y < self.height:
            self.take_step(right, down)


def main():
    trajectory = Trajectory(input_file="day_3/input.txt")
    trajectory.travel(3, 1)
    tree_hits = trajectory.get_tree_hits()
    print("Tree hits: ", tree_hits)


if __name__ == "__main__":
    main()
