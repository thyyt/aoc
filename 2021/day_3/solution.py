from typing import List, Callable


def find_epsilon_bits(lines: List[str]) -> List[int]:
    ones = []
    for i in range(len(lines[0]) - 1):
        one = 0
        for j in range(len(lines)):
            one += int(lines[j][i])
        ones.append(one)
    print(ones)
    print(len(lines))
    bits = [int(round(one / len(lines))) for one in ones]
    return bits


def inverse_string_bits(bits: str) -> str:
    return "".join([str(1 - int(i)) for i in bits])


def inverse_bits(bits: List[int]) -> List[int]:
    return [1 - i for i in bits]


def bits_to_int(bits: List[int]) -> int:
    return int("".join([str(bit) for bit in bits]), 2)


def part_1(lines: List[str]) -> None:
    epsilon_bits = find_epsilon_bits(lines)
    print(epsilon_bits)
    gamma_bits = inverse_bits(epsilon_bits)
    gamma = bits_to_int(gamma_bits)
    epsilon = bits_to_int(epsilon_bits)
    print(gamma, epsilon)
    print(gamma * epsilon)


def find_least_common_bit(bits: List[int]) -> int:
    return int(bool(sum(bits) < len(bits) / 2))


def find_most_common_bit(bits: List[int]) -> int:
    return int(bool(sum(bits) >= len(bits) / 2))


def find_rate_by_elimintion(
    lines: List[str], bit_finder: Callable[[List[int]], int]
) -> str:
    i = 0
    while len(lines) > 1:
        most_common_bit = bit_finder([int(line[i]) for line in lines])
        lines = [line for line in lines if int(line[i]) == most_common_bit]
        i += 1
    print(lines)
    return lines[0]


def part_2(lines: List[str]) -> None:
    lines = [line.strip() for line in lines]
    oxygen_rating = int(find_rate_by_elimintion(lines, find_most_common_bit), 2)
    co2_scrubber_rating = int(
        find_rate_by_elimintion(lines, find_least_common_bit),
        2,
    )
    print(oxygen_rating, co2_scrubber_rating)
    print(oxygen_rating * co2_scrubber_rating)


def main():
    with open("input") as f:
        lines = f.readlines()
    part_1(lines)
    part_2(lines)


if __name__ == "__main__":
    main()
