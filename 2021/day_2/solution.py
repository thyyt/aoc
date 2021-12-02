import pandas as pd
from typing import List, Tuple


def sum_direction_type(directions: List[int], direction: str) -> int:
    return sum(
        [
            int(i.split(" ")[1])
            for i in filter(lambda x: str(x).startswith(direction), directions)
        ]
    )


def find_endpoint(directions: List[int]) -> Tuple[int, int]:
    horizontal = sum_direction_type(directions, "forward")
    depth = sum_direction_type(directions, "down") - sum_direction_type(
        directions, "up"
    )
    return horizontal, depth


def main():
    input_df = pd.read_csv("input", header=None)
    depth, horizontal = find_endpoint(input_df.iloc[:, 0].to_list())
    print(f"{depth} * {horizontal} = {depth *horizontal}")


if __name__ == "__main__":
    main()
