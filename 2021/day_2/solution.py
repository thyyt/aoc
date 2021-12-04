import pandas as pd
from typing import List, Tuple


def sum_direction_type(directions: List[str], direction: str) -> int:
    return sum(
        [
            int(i.split(" ")[1])
            for i in filter(lambda x: str(x).startswith(direction), directions)
        ]
    )


def find_endpoint(directions: List[str]) -> Tuple[int, int]:
    horizontal = sum_direction_type(directions, "forward")
    depth = sum_direction_type(directions, "down") - sum_direction_type(
        directions, "up"
    )
    return horizontal, depth


def calculate_aims(directions: List[str]) -> List[int]:
    aims = []
    aim = 0
    for direction in directions:
        kind = direction.split(" ")[0]
        value = int(direction.split(" ")[1])
        if kind == "up":
            aim -= value
        elif kind == "down":
            aim += value
        aims.append(aim)
    return aims


def part_1(directions: List[str]) -> None:
    depth, horizontal = find_endpoint(directions)
    print(f"{depth} * {horizontal} = {depth *horizontal}")


def filter_and_clean_forwards(directions: List[str]) -> List[int]:
    return [int(x.split(" ")[1]) if x.startswith("forward") else 0 for x in directions]


def find_aimed_depths(directions: List[str]) -> List[int]:
    aims = calculate_aims(directions)
    forwards = filter_and_clean_forwards(directions)
    depth = 0
    for aim, fwd in zip(aims, forwards):
        depth += aim * fwd
    return depth


def part_2(directions: List[str]) -> None:
    horizontal = sum_direction_type(directions, "forward")
    depth = find_aimed_depths(directions)
    print(f"{depth} * {horizontal} = {depth *horizontal}")


def main():
    input_df = pd.read_csv("input", header=None)
    part_1(input_df.iloc[:, 0].to_list())
    part_2(input_df.iloc[:, 0].to_list())


if __name__ == "__main__":
    main()
