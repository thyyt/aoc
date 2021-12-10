import sys
from typing import List, Dict


class DynamicFuelCounter:
    def __init__(self):
        self.fuel_consumption_by_distance: Dict[int, int] = {}
        self.fuel_consumption_by_distance[0] = 0
        self.fuel_consumption_by_distance[1] = 1

    def get_consumption(self, distance: int) -> int:
        print(f"Calling with: {distance}")
        if isinstance(self.fuel_consumption_by_distance.get(distance), int):
            return self.fuel_consumption_by_distance[distance]
        self.fuel_consumption_by_distance[distance] = distance + self.get_consumption(
            distance - 1
        )
        return self.fuel_consumption_by_distance[distance]


def part_1(lines: List[str]) -> None:
    positions = [int(position) for position in lines[0].split(",")]
    print(max(positions))
    distance_differences = {}
    for position in set(positions):
        distance_differences[position] = sum([abs(i - position) for i in positions])
    print(distance_differences)
    print(min(distance_differences.values()))

    consumptions_by_position = {}
    fuel_counter = DynamicFuelCounter()
    for position in range(max(positions) + 1):
        consumptions_by_position[position] = sum(
            [fuel_counter.get_consumption(abs(i - position)) for i in positions]
        )
    print(consumptions_by_position)
    print(min(consumptions_by_position.values()))


def main():
    with open("input") as f:
        # with open("example") as f:
        lines = f.readlines()
    part_1(lines)


if __name__ == "__main__":
    sys.setrecursionlimit(1500)
    main()
