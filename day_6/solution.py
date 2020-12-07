from typing import List, Set


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def parse_paragraphs(lines: List[str]) -> List[Set[str]]:
    parsed_paragraphs = []
    current_paragraph = set()
    for line in lines:
        if line:
            current_paragraph = current_paragraph.union(set(line))
        else:
            parsed_paragraphs.append(current_paragraph)
            current_paragraph = set()
    parsed_paragraphs.append(current_paragraph)
    return parsed_paragraphs


def parse_paragraphs_agreed(lines: List[str]) -> List[Set[str]]:
    parsed_paragraphs = []
    current_group = []
    for line in lines:
        if line:
            current_group.append(set(line))
        else:
            parsed_paragraphs.append(current_group[0].intersection(*current_group))
            current_group = []
    parsed_paragraphs.append(current_group[0].intersection(*current_group))
    return parsed_paragraphs


def main():
    lines = read_input("day_6/input.txt")
    group_positives = parse_paragraphs(lines)
    group_positive_counts = [len(positives) for positives in group_positives]
    print("Positive answers in groups: ", sum(group_positive_counts))

    group_agreements = parse_paragraphs_agreed(lines)
    group_agreements_counts = [len(positives) for positives in group_agreements]
    print("Full positives in groups", sum(group_agreements_counts))


if __name__ == "__main__":
    main()
