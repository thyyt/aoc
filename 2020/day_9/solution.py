from typing import List, NoReturn


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


class XMASData:
    def __init__(self, lines: List[str]) -> NoReturn:
        self.numbers = [int(line) for line in lines]
        self.N = 25
        self.rolling_numbers = self.numbers[: self.N]
        self.next_idx = self.N
        self.invalid_number = None

    def process_next(self) -> bool:
        next_number = self.numbers[self.next_idx]
        diffs = [next_number - i for i in self.rolling_numbers if i * 2 != next_number]
        possible_values = set(diffs).intersection(set(self.rolling_numbers))
        return bool(possible_values)

    def update_numbers(self) -> NoReturn:
        self.rolling_numbers = self.rolling_numbers[1:] + [self.numbers[self.next_idx]]
        self.next_idx += 1

    def find_first_bad_number(self) -> int:
        while self.process_next():
            self.update_numbers()
        self.invalid_number = self.numbers[self.next_idx]
        return self.invalid_number

    def is_starting_index(self, start_idx: int) -> int:
        sum_so_far = self.numbers[start_idx]
        idx = start_idx
        while sum_so_far < self.invalid_number:
            idx += 1
            sum_so_far += self.numbers[idx]
        if sum_so_far == self.invalid_number:
            return idx
        return 0

    def find_contiguous_summands(self) -> List[int]:
        starting_idx = self.N - 1
        end_idx = 0
        while not end_idx:
            starting_idx += 1
            end_idx = self.is_starting_index(starting_idx)
        return self.numbers[starting_idx:end_idx]

    def sum_smallest_and_largest(self, numbers: List[int]) -> int:
        return max(numbers) + min(numbers)

    def find_encryption_weakness(self) -> int:
        numbers = self.find_contiguous_summands()
        return self.sum_smallest_and_largest(numbers)


def main():
    lines = read_input("day_9/input.txt")
    xmas_data = XMASData(lines)

    first_bad_number = xmas_data.find_first_bad_number()
    print("First number not satisfying the conditions: ", first_bad_number)

    encryption_weakness = xmas_data.find_encryption_weakness()
    print("Encryption weakness", encryption_weakness)


if __name__ == "__main__":
    main()
