import string
from typing import List, Dict

SHAPE_VALUES: Dict[str, int] = {'Y':  2, 'X': 1, 'Z': 3}
OUTCOME_MAP: Dict[str, int] = {'Y':  3, 'X': 0, 'Z': 6}


ALPHABET = list(string.ascii_uppercase)
ELF_RPS = ALPHABET[:3]
RPS_INDICES: Dict[str, int] = {ELF_RPS[i]: i for i in range(len(ELF_RPS))}
RPS_MAP: Dict[str, str] = {elf: human for elf,
                           human in zip(ALPHABET[:3], ALPHABET[-3:])}

BEATS = {'X': 'Z', 'Y': 'X', 'Z': 'Y'}
INVERSE_BEATS = {lose: beat for beat, lose in BEATS.items()}


print(SHAPE_VALUES)
print(OUTCOME_MAP)
print(ALPHABET)
print(ELF_RPS)
print(RPS_INDICES)
print(RPS_MAP)
print(BEATS)


def run_rock_paper_scissors(elf: str, me: str) -> int:
    if elf == me:
        return 3
    if BEATS[elf] == me:
        return 0
    return 6


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def first_part(input: List[str]) -> int:
    score = 0
    for rps in input:
        score += run_rock_paper_scissors(RPS_MAP[rps[0]],
                                         rps[-1]) + SHAPE_VALUES[rps[-1]]

    return score


def inverse_rps(elf: str, outcome: int) -> str:
    direction = int(outcome/3) - 1
    print(RPS_INDICES[elf] + direction)
    print(elf, outcome)
    return RPS_MAP[ELF_RPS[RPS_INDICES[elf] + direction]]


def second_part(input: List[str]) -> int:
    score = 0
    for rps in input:
        outcome = OUTCOME_MAP[rps[-1]]
        score += outcome
        elf_to_human = RPS_MAP[rps[0]]
        if outcome == 6:
            score += SHAPE_VALUES[INVERSE_BEATS[elf_to_human]]
        elif outcome == 0:
            score += SHAPE_VALUES[BEATS[elf_to_human]]
        else:
            score += SHAPE_VALUES[elf_to_human]
    return score


def main():
    input = read_input("input")
    print(first_part(input))
    print(second_part(input))


if __name__ == "__main__":
    main()
