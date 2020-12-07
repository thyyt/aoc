from typing import List, Tuple

PARTITION_MAP = {"F": 0, "B": 1, "R": 1, "L": 0}


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def parse_seat_codes(lines: List[str]) -> List[Tuple[str, str]]:
    seat_codes = []
    for line in lines:
        seat_codes.append((line[:-3], line[-3:]))
    return seat_codes


def decode_binary_space_partition(partitioning: str) -> int:
    seat = 0
    shifts = len(partitioning) - 1
    for letter in partitioning:
        seat += PARTITION_MAP[letter] * (2 ** shifts)
        shifts -= 1
    return seat


def get_seat_id(row: int, column: int) -> int:
    return row * 8 + column


def seat_numbers_from_codes(seat_codes: List[Tuple[str, str]]) -> List[Tuple[int, int]]:
    seat_numbers = []
    for seat_code in seat_codes:
        row = decode_binary_space_partition(seat_code[0])
        column = decode_binary_space_partition(seat_code[1])
        seat_numbers.append((row, column))
    return seat_numbers


def main():
    lines = read_input("day_5/input.txt")
    seat_codes = parse_seat_codes(lines)
    seat_numbers = seat_numbers_from_codes(seat_codes)
    seat_ids = [
        get_seat_id(seat_number[0], seat_number[1]) for seat_number in seat_numbers
    ]

    min_seat_id = min(seat_ids)
    max_seat_id = max(seat_ids)
    print("Largest seat id is: ", max_seat_id)

    all_ids = set([id for id in range(min_seat_id, max_seat_id)])
    missing_seat = all_ids - set(seat_ids)
    print("My seat id is: ", missing_seat)


if __name__ == "__main__":
    main()
