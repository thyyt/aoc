from typing import List, NoReturn, Tuple, Set


def solve_part_1(lines: List[str]) -> int:
    pass


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def main():
    lines = read_input("day_11/input.txt")
    part_1 = solve_part_1(lines)
    print("Part 1 solution", part_1)


if __name__ == "__main__":
    main()
