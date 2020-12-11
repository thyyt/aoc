from typing import List, NoReturn, Tuple, Set
from itertools import product
import numpy as np


class Seating:
    def __init__(self, lines: List[str]):
        self.original_seating = self.parse_seating_map(lines)
        self.seating_map = self.original_seating.copy()
        self.iterations = 0
        self.width = len(lines[0])
        self.height = len(lines)
        self.floor = np.nonzero(self.seating_map == ".")
        for i in self.floor:
            if i[0] >= self.width or i[1] >= self.height:
        pair_list = []
        for y, x in zip(*self.floor):
            pair_list.append((x, y))
        self.floor_pairs = set(pair_list)
        self.potentially_changing = set()
        self.update_potentials(
            set(
                (x, y)
                for y, x in product(
                    [i for i in range(self.height)], [i for i in range(self.width)]
                )
            )
        )
        self.full_potentials = self.potentially_changing.copy()

    def update_potentials(self, potetntials: Set[Tuple[int, int]]) -> NoReturn:
        self.potentially_changing = potetntials - self.floor_pairs

    def parse_seating_map(self, lines: List[str]) -> np.ndarray:
        seat_map = []
        for line in lines:
            seat_map.append(list(line))
        return np.array(seat_map)

    def iterate_seating_visible(self) -> Tuple[bool, Set[Tuple[int, int]]]:
        changing_map = []
        new_seating = self.seating_map.copy()
        for x, y in self.potentially_changing:
            occupied_neighbours = self.count_visible_occupied_seats(x, y)
            new_state = self.get_new_state_visible(new_seating[y, x], occupied_neighbours)
            if new_state != self.seating_map[y, x]:
                new_seating[y, x] = new_state
                changing_map.append((x, y))
                changing_map = changing_map + self.get_visible_seats(x, y)
        has_changes = self.equal_seating_maps(new_seating, self.seating_map)
        self.seating_map = new_seating
        self.update_potentials(set(changing_map))
        return has_changes

    def iterate_seating(self) -> Tuple[bool, Set[Tuple[int, int]]]:
        changing_map = []
        new_seating = self.seating_map.copy()
        for x, y in self.potentially_changing:
            occupied_neighbours = self.count_neighboring_occupied_seats(x, y)
            new_state = self.get_new_state(new_seating[y, x], occupied_neighbours)
            if new_state != self.seating_map[y, x]:
                new_seating[y, x] = new_state
                changing_map.append((x, y))
                changing_map = changing_map + self.get_visible_seats(x, y)
        has_changes = self.equal_seating_maps(new_seating, self.seating_map)
        self.seating_map = new_seating
        self.update_potentials(set(changing_map))
        return has_changes

    def iterate_until_convergence_visible(self) -> NoReturn:
        self.seating_map = self.original_seating
        self.update_potentials(self.full_potentials)
        seating_changed = True
        while seating_changed:
            seating_changed = self.iterate_seating_visible()
            self.iterations += 1

    def iterate_until_convergence(self) -> NoReturn:
        seating_changed = True
        while seating_changed:
            seating_changed = self.iterate_seating()
            self.iterations += 1

    def get_visible_seats(self, x: int, y: int) -> List[Tuple[int, int]]:
        visible = []
        for x_diff, y_diff in product([-1, 0, 1], repeat=2):
            if x_diff != 0 or y_diff != 0:
                visible.append(self.find_visible_seat(x, y, x_diff, y_diff))
        return list(filter(lambda x: self.coordinate_is_on_map(x[0], x[1]), visible))

    def find_visible_seat(
        self, x: int, y: int, x_diff: int, y_diff: int
    ) -> Tuple[int, int]:
        x += x_diff
        y += y_diff
        while self.coordinate_is_on_map(x, y):
            if self.seating_map[y, x] != ".":
                return (x, y)
            x += x_diff
            y += y_diff
        return (x, y)

    def get_neighboring_indices(self, x: int, y: int) -> List[Tuple[int, int]]:
        neighbours = []
        for x_diff, y_diff in product([-1, 0, 1], repeat=2):
            if x_diff != 0 or y_diff != 0:
                neighbours.append((x + x_diff, y + y_diff))
        return list(filter(lambda x: self.coordinate_is_on_map(x[0], x[1]), neighbours))

    def count_visible_occupied_seats(self, x: int, y: int) -> int:
        neighbor_indices = self.get_visible_seats(x, y)
        return sum(
            [
                self.seating_map[indices[1], indices[0]] == "#"
                for indices in neighbor_indices
            ]
        )

    def count_neighboring_occupied_seats(self, x: int, y: int) -> int:
        neighbor_indices = self.get_neighboring_indices(x, y)
        return sum(
            [
                self.seating_map[indices[1], indices[0]] == "#"
                for indices in neighbor_indices
            ]
        )

    def equal_seating_maps(self, left: np.ndarray, right: np.ndarray) -> bool:
        return (left != right).any()

    def coordinate_is_on_map(self, x_idx: int, y_idx: int) -> bool:
        return x_idx >= 0 and x_idx < self.width and y_idx >= 0 and y_idx < self.height

    def get_new_state_visible(self, seat_type: str, occupied_neighbours: int) -> str:
        if occupied_neighbours == 0 and seat_type == "L":
            return "#"
        if occupied_neighbours >= 5 and seat_type == "#":
            return "L"
        return seat_type

    def get_new_state(self, seat_type: str, occupied_neighbours: int) -> str:
        if occupied_neighbours == 0 and seat_type == "L":
            return "#"
        if occupied_neighbours >= 4 and seat_type == "#":
            return "L"
        return seat_type

    def get_iteration_count(self) -> int:
        return self.iterations

    def count_occupied(self) -> int:
        return (self.seating_map == "#").sum()


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def main():
    lines = read_input("day_11/input.txt")
    seating = Seating(lines)
    seating.iterate_until_convergence()
    occupied = seating.count_occupied()
    print("Occupied seats:", occupied)

    seating.iterate_until_convergence_visible()
    occupied = seating.count_occupied()
    print("Occupied seats, visible :", occupied)


if __name__ == "__main__":
    main()
