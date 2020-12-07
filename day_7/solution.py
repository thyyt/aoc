from typing import List, Dict, Tuple


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def clean_lines(lines: List[str]) -> List[str]:
    cleaned = []
    for line in lines:
        line = line.replace(" bags", "")
        line = line.replace(" bag", "")
        line = line.replace(".", "")
        cleaned.append(line)
    return cleaned


def get_containments(containment_str: str) -> Tuple[List[str], List[int]]:
    if containment_str == "no other":
        return ([], [])
    count_list = []
    bag_list = []
    bags = containment_str.split(",")
    for bag in bags:
        bag = bag.strip()
        bag_parts = bag.split(" ")
        count_list.append(int(bag_parts[0]))
        bag_list.append(bag_parts[1] + " " + bag_parts[2])
    return (bag_list, count_list)


def get_contain_lists(
    cleaned_lines: List[str],
) -> Dict[str, Tuple[List[str], List[int]]]:
    containment_map = {}
    for line in cleaned_lines:
        parts = line.split(" contain ")
        target_bag = parts[0]
        bag_list, bag_counts = get_containments(parts[1])
        containment_map[target_bag] = (bag_list, bag_counts)

    return containment_map


def count_bags_inside(
    bag: str,
    bag_map: Dict[str, Tuple[List[str], List[int]]],
) -> int:
    bags_inside = 0
    containments, counts = bag_map[bag]
    for bag, count in zip(containments, counts):
        bags_inside += (count * (1 + count_bags_inside(bag, bag_map)))
    return bags_inside


def can_contain_bag(
    bag: str,
    bag_map: Dict[str, Tuple[List[str], List[int]]],
    target_bag: str = "shiny gold",
) -> str:
    containments, _ = bag_map[bag]
    if not containments:
        return False
    if target_bag in containments:
        return True
    return bool(
        max(
            [
                can_contain_bag(inner_bag, bag_map, target_bag)
                for inner_bag in containments
            ]
        )
    )


def iterate_over_bags(bag_map: Dict[str, Tuple[List[str], List[int]]]) -> List[str]:
    good_bags = []
    for bag, _ in bag_map.items():
        if can_contain_bag(
            bag,
            bag_map,
        ):
            good_bags.append(bag)
    return good_bags


def main():
    lines = read_input("day_7/input.txt")
    cleaned_lines = clean_lines(lines)

    contain_maps = get_contain_lists(cleaned_lines)
    good_bags = iterate_over_bags(contain_maps)
    print(good_bags)
    print("Number of bags that fit 'shiny gold':", len(good_bags))

    inside_shiny = count_bags_inside("shiny gold", contain_maps)
    print("Number of bags inside 'shiny gold':", inside_shiny)


if __name__ == "__main__":
    main()
