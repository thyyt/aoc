from typing import List, Dict

REQUIRED_FIELDS = [
    "byr",
    "iyr",
    "eyr",
    "hgt",
    "hcl",
    "ecl",
    "pid",
]
OPTIONAL_FIELD = "cid"


def parse_passports(lines: List[str]) -> List[Dict[str, str]]:
    parsed_passports = []
    current_passport = {}
    for line in lines:
        if line:
            fields = line.split(" ")
            for field in fields:
                field_parts = field.split(":")
                current_passport[field_parts[0]] = field_parts[1]
        else:
            parsed_passports.append(current_passport)
            current_passport = {}
    return parsed_passports


def is_valid_passport(pw_fields: Dict[str, str]) -> bool:
    for field in REQUIRED_FIELDS:
        if not (field in pw_fields.keys()):
            print(field, len(pw_fields), pw_fields)
            return False
    return True


def read_input(input_file) -> List[str]:
    pw_file = open(input_file, "rb+")
    pw_lines = pw_file.readlines()
    return [pw_line.decode("utf-8").strip() for pw_line in pw_lines]


def main():
    lines = read_input("day_4/input.txt")
    passport_data = parse_passports(lines)
    valid_passports = 0
    total_passports = 0
    for passport in passport_data:
        valid = is_valid_passport(passport)
        valid_passports += valid
        total_passports += 1

    print("Valid passports: ", valid_passports)
    print("Total passports: ", total_passports)


if __name__ == "__main__":
    main()
