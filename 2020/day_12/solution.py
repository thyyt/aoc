from typing import List, NoReturn, Tuple, Set


RIGHT_TURNS = {"E": "S", "N": "E", "S": "W", "W": "N"}
LEFT_TURNS = {v: k for k, v in RIGHT_TURNS.items()}


class Ship:
    def __init__(self, lines: List[str]) -> NoReturn:
        self.facing = "E"
        self.east = 0
        self.north = 0
        self.instructions = self.parse_instructions(lines)
        self.waypoint_east = 10
        self.waypoint_north = 1

    def parse_instructions(self, lines: List[str]) -> List[Tuple[str, int]]:
        instructions = []
        for line in lines:
            instructions.append((line[0], int(line[1:])))
        return instructions

    def move_to_waypoint(self, value: int) -> NoReturn:
        self.north += value * self.waypoint_north
        self.east += value * self.waypoint_east

    def move_waypoint(self, direction: str, value: int) -> NoReturn:
        if direction in ["S", "W"]:
            value = -value
        if direction in ["S", "N"]:
            self.waypoint_north += value
        else:
            self.waypoint_east += value

    def go_to_direction(self, direction: str, value: int) -> NoReturn:
        if direction == "F":
            direction = self.facing
        if direction in ["S", "W"]:
            value = -value
        if direction in ["S", "N"]:
            self.north += value
        else:
            self.east += value

    def turn_waypoint(self, direction: str, value: int) -> NoReturn:
        print(self.waypoint_north, self.waypoint_east, direction, value)
        if direction == "R":
            next_north = (-1) * self.waypoint_east
            self.waypoint_east = self.waypoint_north
            self.waypoint_north = next_north
            # next_east = (-1) * self.waypoint_north
            # self.waypoint_north = self.waypoint_east
            # self.waypoint_east = next_east
            value -= 90
            if value > 0:
                self.turn_waypoint(direction, value)
        # no need to think the operation to other direction :)
        if direction == "L":
            self.turn_waypoint("R", 3 * value)

    def turn_ship(self, direction: str, value: int) -> NoReturn:
        if direction == "R":
            self.facing = RIGHT_TURNS[self.facing]
        if direction == "L":
            self.facing = LEFT_TURNS[self.facing]
        value -= 90
        if value > 0:
            self.turn_ship(direction, value)

    def follow_instructions_part_1(self) -> NoReturn:
        for action, value in self.instructions:
            self.take_action(action, value)

    def follow_instructions_part_2(self) -> NoReturn:
        for action, value in self.instructions:
            self.take_waypoint_action(action, value)

    def take_waypoint_action(self, action: str, value: int) -> NoReturn:
        if action in ["R", "L"]:
            self.turn_waypoint(action, value)
        elif action == "F":
            self.move_to_waypoint(value)
        else:
            self.move_waypoint(action, value)

    def take_action(self, action: str, value: int) -> NoReturn:
        if action in ["R", "L"]:
            self.turn_ship(action, value)
        else:
            self.go_to_direction(action, value)

    def get_manhattan_distance(self) -> int:
        return abs(self.east) + abs(self.north)

    def reset(self) -> NoReturn:
        self.east = 0
        self.north = 0


def read_input(input_file) -> List[str]:
    open_file = open(input_file, "rb+")
    lines = open_file.readlines()
    return [line.decode("utf-8").strip() for line in lines]


def main():
    lines = read_input("day_12/input.txt")

    ship = Ship(lines)
    ship.follow_instructions_part_1()
    distance = ship.get_manhattan_distance()
    print("Part 1 Manhattan distance from starting point:", distance)

    ship.reset()
    ship.follow_instructions_part_2()
    distance = ship.get_manhattan_distance()
    print("Part 2 Manhattan distance from starting point:", distance)


if __name__ == "__main__":
    main()
