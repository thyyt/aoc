from typing import List, Tuple


def get_letter_counts(pw: str, letter: str) -> int:
    return pw.count(letter)


def get_letter_indices(limit_str: str) -> Tuple[int, int]:
    splitted_rule = limit_str.split("-")
    return int(splitted_rule[0]) - 1, int(splitted_rule[1]) - 1


def get_rule_limits(limit_str: str) -> Tuple[int, int]:
    splitted_rule = limit_str.split("-")
    return int(splitted_rule[0]), int(splitted_rule[1])


def get_target_letter(letter_str: str) -> str:
    return letter_str[0]


def read_passwords(target_file: str) -> List[str]:
    pw_file = open(target_file, "rb+")
    pw_lines = pw_file.readlines()
    return [pw_line.decode("utf-8").strip() for pw_line in pw_lines]


def sled_validate_passwords(pw_rules: List[str]) -> List[bool]:
    validities = []
    for pw_rule in pw_rules:
        validities.append(check_password(pw_rule))
    return validities


def check_password(pw_rule: str):
    rule_list = pw_rule.split(" ")

    min_count, max_count = get_rule_limits(rule_list[0])
    letter = get_target_letter(rule_list[1])
    letter_counts = get_letter_counts(rule_list[2], letter)
    if min_count <= letter_counts and letter_counts <= max_count:
        return True
    return False


def toboggan_validate_passwords(pw_rules: List[str]) -> List[bool]:
    validities = []
    for pw_rule in pw_rules:
        validities.append(toboggan_check_password(pw_rule))
    return validities


def letter_at_index(pw: str, letter: str, idx: int):
    if (len(pw) > idx) and (pw[idx] == letter):
        return True
    return False


def toboggan_check_password(pw_rule: str):
    rule_list = pw_rule.split(" ")
    min_idx, max_idx = get_letter_indices(rule_list[0])
    letter = get_target_letter(rule_list[1])
    min_letter_match = letter_at_index(rule_list[2], letter, min_idx)
    max_letter_match = letter_at_index(rule_list[2], letter, max_idx)
    if min_letter_match + max_letter_match == 1:
        return True
    return False


def main():
    password_rules = read_passwords("day_2/input.txt")
    sled_validity_flags = sled_validate_passwords(password_rules)
    sled_valid_count = sum(sled_validity_flags)

    toboggan_validity_flags = toboggan_validate_passwords(password_rules)
    toboggan_valid_count = sum(toboggan_validity_flags)

    print("Valid sled rental passwords: ", sled_valid_count)
    print("Valid toboggan passwords: ", toboggan_valid_count)


if __name__ == "__main__":
    main()
