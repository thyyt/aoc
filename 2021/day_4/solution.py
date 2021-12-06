from typing import List


class BingoBoard:
    """Bingo Board"""

    def __init__(self, grid_lines: List[str]):
        self.has_bingo = False
        self.width = 5
        self.height = 5
        self.numbers_grid = [
            [int(number) for number in line.split()] for line in grid_lines
        ]
        self.hits = [[False for _ in range(self.width)] for _ in range(self.height)]

    def check_if_has_bingo(self) -> bool:
        horizontal_bingo = max([sum(row) for row in self.hits]) == self.width
        vertical_bingo = (
            max(
                [
                    sum(
                        [
                            self.hits[row_index][col_index]
                            for row_index in range(self.height)
                        ]
                    )
                    for col_index in range(self.width)
                ]
            )
            == self.width
        )
        self.has_bingo = self.has_bingo or (horizontal_bingo or vertical_bingo)
        return self.has_bingo

    def draw_number(self, drawn: int) -> int:
        for row_index in range(self.height):
            for col_index in range(self.width):
                if self.numbers_grid[row_index][col_index] == drawn:
                    self.hits[row_index][col_index] = True
                    if self.check_if_has_bingo():
                        return self.calculate_score(drawn)
        return 0

    def calculate_score(self, last_drawn: int) -> int:
        sum_of_unmarked = 0
        for row_index in range(self.height):
            for col_index in range(self.width):
                sum_of_unmarked += self.numbers_grid[row_index][col_index] * (
                    1 - int(self.hits[row_index][col_index])
                )
        for row in self.numbers_grid:
            print(row)
        for row in self.hits:
            print(row)
        print(sum_of_unmarked, last_drawn)
        return sum_of_unmarked * last_drawn


class BingoSubsystem:
    """Run the whole bingo"""

    def __init__(self, lines: List[str]):
        self.width = 5
        self.height = 5
        self.first_bingo = False
        self.numbers_to_draw = [int(number) for number in lines[0].split(",")]
        self.boards = self.build_boards(lines[2:])

    def build_boards(self, lines: List[str]) -> List[BingoBoard]:
        return [
            BingoBoard(lines[i : i + self.height])
            for i in range(0, len(lines), self.height + 1)
        ]

    def run(self):
        boards_to_remove = []
        for drawn in self.numbers_to_draw:
            for board in boards_to_remove:
                self.boards.remove(board)
            boards_to_remove = []
            for board in self.boards:
                score = board.draw_number(drawn)
                if score > 0 and not self.first_bingo:
                    self.first_bingo = True
                    print(f"BINGO! The score for the first board is: {score}")
                    boards_to_remove.append(board)
                elif score > 0 and len(self.boards) > 1:
                    print("meaningless bingo!")
                    boards_to_remove.append(board)
                elif score > 0 and len(self.boards) == 1:
                    print(f"BINGO! The score for the final board is: {score}")
                    return
        return


def main():
    with open("input") as f:
        lines = f.readlines()
    system = BingoSubsystem(lines)
    system.run()


if __name__ == "__main__":
    main()
