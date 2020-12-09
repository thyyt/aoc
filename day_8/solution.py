from typing import List, Tuple, NoReturn


class Console:
    def __init__(self, instructions: List[str]):
        self.accumulator = 0
        self.instruction_idx = 0
        self.followed_instructions = set()
        self.original_instructions, self.arguments = self.parse_instructions(
            instructions
        )
        self.instructions = self.original_instructions.copy()
        self.instruction_map = {
            "nop": self.follow_nop,
            "jmp": self.follow_jmp,
            "acc": self.follow_acc,
        }
        self.next_fix_to_attempt = 0
        self.instruction_reverse_map = {"nop": "jmp", "jmp": "nop"}

    def parse_instructions(self, lines: List[str]) -> Tuple[List[str], List[int]]:
        instructions = []
        arguments = []
        for line in lines:
            instructions.append(line.split(" ")[0])
            arguments.append(int(line.split(" ")[1]))
        return instructions, arguments

    def follow_nop(self, argument: int) -> NoReturn:
        self.instruction_idx += 1

    def follow_acc(self, argument: int) -> NoReturn:
        self.accumulator += argument
        self.instruction_idx += 1

    def follow_jmp(self, argument: int) -> NoReturn:
        self.instruction_idx += argument

    def follow_instruction(self, instruction_idx: int) -> NoReturn:
        instruction = self.instructions[instruction_idx]
        argument = self.arguments[instruction_idx]
        self.instruction_map[instruction](argument)

    def next_instruction(
        self,
    ) -> NoReturn:
        pass

    def execute_until_repeat(self) -> int:
        while (
            self.instruction_idx not in self.followed_instructions
            and self.instruction_idx < len(self.instructions)
        ):
            self.followed_instructions.add(self.instruction_idx)
            self.follow_instruction(self.instruction_idx)
        return self.accumulator, self.instruction_idx

    def attempt_next_fix(self) -> bool:
        if self.instructions[self.next_fix_to_attempt] == "acc":
            self.next_fix_to_attempt += 1
            return False
        self.instructions[self.next_fix_to_attempt] = self.instruction_reverse_map[
            self.instructions[self.next_fix_to_attempt]
        ]
        self.execute_until_repeat()
        return self.instruction_idx == len(self.instructions)

    def reset(self) -> NoReturn:
        self.instructions = self.original_instructions.copy()
        self.accumulator = 0
        self.instruction_idx = 0
        self.followed_instructions = set()

    def fix(self) -> int:
        fix_worked = False
        while not fix_worked:
            self.reset()
            fix_worked = self.attempt_next_fix()
            self.next_fix_to_attempt += 1
        return self.accumulator


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def main():
    lines = read_input("day_8/input.txt")
    console = Console(lines)
    accumulator, _ = console.execute_until_repeat()
    print("Accumulator before first repeat: ", accumulator)

    fixed_accumulator = console.fix()
    print("Accumulator after fix: ", fixed_accumulator)


if __name__ == "__main__":
    main()
