from typing import List


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def first_part(input: List[str]) -> int:
    pass


def second_part(input: List[str]) -> int:
    pass


def main():
    input = read_input("input")
    print(first_part(input))
    print(second_part(input))


if __name__ == "__main__":
    main()
