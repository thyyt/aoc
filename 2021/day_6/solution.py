from typing import List


def parse_input_to_timer(lines: List[str]) -> List[int]:
    numbers = [int(number) for number in lines[0].split(",")]
    timers = []
    for i in range(max(numbers) + 1):
        timers.append(numbers.count(i))
    return timers


def grow_fishes(lines: List[str], days: int) -> None:
    timers = parse_input_to_timer(lines)
    print(timers)
    for _ in range(days):
        print(timers)
        new_timers = [0] * 9
        for i, timer in enumerate(timers):
            if i == 0:
                new_timers[6] = timer
                new_timers[8] += timer
            else:
                new_timers[i - 1] += timer
        timers = new_timers
    print(sum(timers))


def main():
    with open("input") as f:
        # with open("example") as f:
        lines = f.readlines()
    grow_fishes(lines, 80)
    grow_fishes(lines, 256)


if __name__ == "__main__":
    main()
