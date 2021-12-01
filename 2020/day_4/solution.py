from typing import List, Dict
import re

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
ALLOWED_HAIR_COLORS = [
    "amb",
    "blu",
    "brn",
    "gry",
    "grn",
    "hzl",
    "oth",
]


def country_id_validator(value: str) -> bool:
    return True


def birth_year_validator(value: str) -> bool:
    return int(value) >= 1920 and int(value) <= 2002


def issue_year_validator(value: str) -> bool:
    return int(value) >= 2010 and int(value) <= 2020


def expiration_year_validator(value: str) -> bool:
    return int(value) >= 2020 and int(value) <= 2030


def height_validator(value: str) -> bool:
    height_value = value[:-2]
    if value[-2:] == "in":
        return int(height_value) >= 59 and int(height_value) <= 76
    if value[-2:] == "cm":
        return int(height_value) >= 150 and int(height_value) <= 193
    return False


def hair_color_validator(value: str) -> bool:
    return bool(re.match("^#[a-z0-9]{6}$", value))


def eye_color_validator(value: str) -> bool:
    return value in ALLOWED_HAIR_COLORS


def passport_id_validator(value: str) -> bool:
    return bool(re.match("^[a-z0-9]{9}$", value))


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
    parsed_passports.append(current_passport)
    return parsed_passports


FIELD_VALIDATOR_MAP = {
    "byr": birth_year_validator,
    "iyr": issue_year_validator,
    "eyr": expiration_year_validator,
    "hgt": height_validator,
    "hcl": hair_color_validator,
    "ecl": eye_color_validator,
    "pid": passport_id_validator,
    "cid": country_id_validator,
}


def fields_are_valid(pw_fields: Dict[str, str]) -> bool:
    for key, value in pw_fields.items():
        if not FIELD_VALIDATOR_MAP[key](value):
            return False
    return True


def has_required_fields(pw_fields: Dict[str, str]) -> bool:
    for field in REQUIRED_FIELDS:
        if not (field in pw_fields.keys()):
            return False
    return True


def read_input(input_file) -> List[str]:
    pw_file = open(input_file, "rb+")
    pw_lines = pw_file.readlines()
    return [pw_line.decode("utf-8").strip() for pw_line in pw_lines]


def main():
    lines = read_input("day_4/input.txt")
    passport_data = parse_passports(lines)
    has_fields_counter = 0
    valid_passports = 0
    invalid_passports = []
    for passport in passport_data:
        has_fields = has_required_fields(passport)
        valid = fields_are_valid(passport)
        has_fields_counter += has_fields
        valid_passports += valid and has_fields

        if not valid:
            invalid_passports.append(passport)

    print("Required fields in passports: ", has_fields_counter)
    print("Valid passports: ", valid_passports)


if __name__ == "__main__":
    main()
