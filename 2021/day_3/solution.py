from typing import List


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


def main():
    with open("input") as f:
        lines = f.readlines()
    part_1(lines)


if __name__ == "__main__":
    main()
