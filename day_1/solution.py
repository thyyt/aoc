import pandas as pd
from typing import Tuple


def find_target_value_pairs(df: pd.DataFrame, target: int) -> Tuple[int, int]:
    for i in range(df.shape[0]):
        for j in range(df.shape[0] - i - 1):
            if (df.loc[i, 0] + df.loc[j, 0]) == target:
                return (df.loc[i, 0], df.loc[j, 0])


def find_target_value_triplets(df: pd.DataFrame, target: int) -> Tuple[int, int]:
    for i in range(df.shape[0]):
        for j in range(df.shape[0] - i - 1):
            for k in range(df.shape[0] - j - 1):
                if (df.loc[i, 0] + df.loc[j, 0] + df.loc[k, 0]) == target:
                    return (df.loc[i, 0], df.loc[j, 0], df.loc[k, 0])


def main():
    input_df = pd.read_csv("day_1/inputs.txt", header=None)
    x, y = find_target_value_pairs(input_df, 2020)
    a, b, c = find_target_value_triplets(input_df, 2020)

    print(x * y)
    print(a * b * c)


if __name__ == "__main__":
    main()
