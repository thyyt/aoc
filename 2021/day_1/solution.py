import itertools
import pandas as pd
from typing import List


def pairwise(iterable):
    b = iterable[1:]
    return zip(iterable, b)


def count_number_of_increases(depths: List[int]) -> int:
    count = 0
    for a, b in pairwise(depths):
        if a < b:
            count += 1
    return count


def sum_triplets(depths: List[int]) -> List[int]:
    sums = []
    for i in range(2, len(depths)):
        sums.append(sum(depths[i - 3 : i]))
    return sums


def count_number_of_triplet_increases(depths: List[int]) -> int:
    triplet_sums = sum_triplets(depths)
    increases = count_number_of_increases(triplet_sums)
    print(depths[-10:])
    print(triplet_sums[-10:])
    print(len(triplet_sums))
    return increases


def main():
    input_df = pd.read_csv("input.txt", header=None)
    increases = count_number_of_increases(input_df.iloc[:, 0].to_list())
    print(f"increases: {increases}")

    triplet_increases = count_number_of_triplet_increases(input_df.iloc[:, 0].to_list())
    print(f"triplet increases: {triplet_increases}")


if __name__ == "__main__":
    main()
