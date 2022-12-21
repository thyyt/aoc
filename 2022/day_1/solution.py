from typing import List, NoReturn, Tuple, Set


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def first_part(input: List[str]) -> int:
    current_calories = 0
    max_calories = 0
    for calories in input:
        if calories:
            current_calories += int(calories)
        else:
            max_calories = max(max_calories, current_calories)
            current_calories = 0

    max_calories = max(max_calories, current_calories)
    return max_calories


def second_part(input: List[str]) -> int:

    current_calories = 0
    elf_calories = []
    for calories in input:
        if calories:
            current_calories += int(calories)
        else:
            elf_calories.append(current_calories)
            current_calories = 0

    elf_calories.append(current_calories)

    return sum(sorted(elf_calories)[-3:])


def main():
    input = read_input("input")
    print(first_part(input))
    print(second_part(input))


if __name__ == "__main__":
    main()
