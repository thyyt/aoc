from typing import List, NoReturn, Dict


class JoltageExplorer:
    def __init__(self, lines: List[str]) -> NoReturn:
        self.jolts = sorted([int(line) for line in lines])
        self.extended_jolts = self.jolts + [max(self.jolts) + 3]
        self.joltage = 0
        self.jolt_differences = {1: 0, 2: 0, 3: 0}
        self.adapter_combinations = {max(self.jolts): 1}

    def try_all_adapters(self) -> NoReturn:
        for adapter in self.extended_jolts:
            diff = adapter - self.joltage
            self.jolt_differences[diff] += 1
            self.joltage = adapter

    def get_jolt_differences(self) -> Dict[int, int]:
        return self.jolt_differences

    def set_adapter_combinations_for_jolt(
        self, jolt: int, combinations: int
    ) -> NoReturn:
        self.adapter_combinations[jolt] = combinations

    def get_adapter_combinations_for_jolt(self, jolt: int) -> int:
        return self.adapter_combinations.get(jolt)

    def get_previous_adapters(self, jolt: int) -> int:
        return list(filter(lambda x: x > jolt and x <= jolt + 3, self.jolts))

    def update_adapter_combinations(self, jolt: int) -> NoReturn:
        previous = self.get_previous_adapters(jolt)
        self.set_adapter_combinations_for_jolt(
            jolt, sum([self.get_adapter_combinations_for_jolt(i) for i in previous])
        )

    def count_all_combinations_dynamic(self):
        jolts_and_ground = [0] + self.jolts
        for jolt in jolts_and_ground[::-1][1:]:
            self.update_adapter_combinations(jolt)
        return self.get_adapter_combinations_for_jolt(0)


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def main():
    lines = read_input("day_10/input.txt")
    joltage_explorer = JoltageExplorer(lines)
    joltage_explorer.try_all_adapters()
    jolt_differences = joltage_explorer.get_jolt_differences()
    print(
        "1-jolt differences * 3-jolt differences: ",
        jolt_differences[1] * jolt_differences[3],
    )

    combinations = joltage_explorer.count_all_combinations_dynamic()
    print("Total adapter combinations:", combinations)


if __name__ == "__main__":
    main()
