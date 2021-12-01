from typing import List, NoReturn, Tuple
from functools import reduce

SLOPES = [
    (1, 1),
    (3, 1),
    (5, 1),
    (7, 1),
    (1, 2),
]


class Trajectory:
    def __init__(self, input_file: str):
        self.map = self.read_input(input_file)
        self.width = len(self.map[0])
        self.height = len(self.map)
        self.pos_x = 0
        self.pos_y = 0
        self.tree_hits = 0
        self.past_tree_hits = []
        self.slopes = []

    def reset(self):
        self.past_tree_hits.append(self.tree_hits)
        self.tree_hits = 0
        self.pos_x = 0
        self.pos_y = 0

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

    def add_slopes(self, slopes: List[Tuple[int, int]]):
        self.slopes = self.slopes + slopes

    def travel_slopes(self) -> NoReturn:
        for slope in self.slopes:
            print(slope)
            right, down = slope
            self.travel(right, down)
            print(self.tree_hits)
            self.reset()

    def get_total_trees_multiplied(self) -> int:
        print(self.past_tree_hits)
        return reduce(lambda x, y: x*y, self.past_tree_hits)


def main():
    trajectory = Trajectory(input_file="day_3/input.txt")
    trajectory.travel(3, 1)
    tree_hits = trajectory.get_tree_hits()
    print("Tree hits on initial route: ", tree_hits)
    trajectory.reset()

    multiple_trajectory = Trajectory(input_file="day_3/input.txt")
    multiple_trajectory.add_slopes(SLOPES)
    multiple_trajectory.travel_slopes()
    total_tree_hits = multiple_trajectory.get_total_trees_multiplied()
    print("Total tree hits on all routes: ", total_tree_hits)


if __name__ == "__main__":
    main()
