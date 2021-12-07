from typing import List, Tuple
from collections import namedtuple
import numpy as np

Point = namedtuple("Point", "x y")
Line = namedtuple("Line", "start end")


class HydroVents:
    def __init__(self, lines: List[str]):
        self.line_ends = self.parse_input(lines)
        self.height, self.width = self.find_dimensions()
        self.grid = np.zeros((self.height, self.width))

    def parse_input(self, lines) -> List[Line]:
        vent_lines = []
        for line in lines:
            start = Point(
                int(line.split(",")[0]), int(line.split(",")[1].split(" ")[0])
            )
            end = Point(
                int(line.split(" -> ")[1].split(",")[0]),
                int(line.split(",")[2]),
            )
            vent_lines.append(Line(start, end))
        return vent_lines

    def find_dimensions(self) -> Tuple[int, int]:
        width = 0
        height = 0
        for ends in self.line_ends:
            height = max(height, ends.start.y, ends.end.y)
            width = max(width, ends.start.x, ends.end.x)
        return 1 + height, 1 + width

    def draw_horizontal_lines(self) -> None:
        for ends in self.line_ends:
            if ends.start.x == ends.end.x:
                low_y = min(ends.start.y, ends.end.y)
                high_y = max(ends.start.y, ends.end.y)
                self.grid[ends.end.x, low_y : high_y + 1] += 1

    def draw_vertical_lines(self) -> None:
        pass
        for ends in self.line_ends:
            if ends.start.y == ends.end.y:
                low_x = min(ends.start.x, ends.end.x)
                high_x = max(ends.start.x, ends.end.x)
                self.grid[low_x : high_x + 1, ends.start.y] += 1

    def count_ovelaps(self) -> int:
        return (self.grid > 1).sum()

    def draw_diagonal_lines(self) -> None:
        for ends in self.line_ends:
            if ends.start.x != ends.end.x and ends.start.y != ends.end.y:
                for y, x in zip(
                    self.get_diagonal_range(ends.start.y, ends.end.y),
                    self.get_diagonal_range(ends.start.x, ends.end.x),
                ):
                    self.grid[x, y] += 1

    def get_diagonal_range(self, start: int, end: int) -> np.ndarray:
        if start < end:
            return np.arange(start, end + 1, 1)
        return np.arange(start, end - 1, -1)


def main():
    with open("input") as f:
        # with open("example") as f:
        lines = f.readlines()
    hydro_vents = HydroVents(lines)
    hydro_vents.draw_vertical_lines()
    hydro_vents.draw_horizontal_lines()
    print(hydro_vents.grid.T)
    print(f"horizontal and vertical line overlaps: {hydro_vents.count_ovelaps()}")
    hydro_vents.draw_diagonal_lines()
    print(hydro_vents.grid.T)
    print(f"Total line overlaps: {hydro_vents.count_ovelaps()}")


if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
