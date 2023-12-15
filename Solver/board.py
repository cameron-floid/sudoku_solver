class Board:

    def __init__(self):
        """
        Constructor for the Board class.

        Raises:
            ValueError: If the entered Sudoku board is not valid.
        """

        self.tiles = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]

        if not self.valid_board():
            raise ValueError("The entered Sudoku board is not valid!")

    def display(self, title: str = "Board"):
        """
        Display the Sudoku board.

        Args:
            title (str): Title for the board display.
        """
        print(f"\n{title}:\n")

        for i, row in enumerate(self.tiles):
            if not i % 3 == 0 and i != 0:
                print()

            if i % 3 == 0 and i != 0:
                print("\n- - - - - - - - - - - -")

            for j, value in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")
                print(value, end=" ")

        print("\n")

    def next_empty_tile(self):
        """
        Find the next empty tile in the Sudoku board.

        Returns:
            tuple: Coordinates (row, column) of the next empty tile, or None if the board is full.
        """
        return next(((i, j) for i, row in enumerate(self.tiles) for j, value in enumerate(row) if value == 0),
                    None)

    def valid_board(self):
        """
        Check if the Sudoku board is valid.

        Returns:
            bool: True if the board is valid, False otherwise.
        """
        size = len(self.tiles)
        return all(len(col) == size for col in self.tiles)

    def valid(self, value: int, position: tuple) -> bool:
        """
        Check if placing a value at a specific position is valid.

        Args:
            value (int): The value to be placed.
            position (tuple): Coordinates (row, column) of the position.

        Returns:
            bool: True if the placement is valid, False otherwise.
        """
        row, col = position

        # check row
        if any(self.tiles[row][i] == value and i != col for i in range(len(self.tiles[0]))):
            return False

        # check the col
        if any(self.tiles[i][col] == value and i != row for i in range(len(self.tiles[0]))):
            return False

        # check square
        box_start_row, box_start_col = row // 3 * 3, col // 3 * 3

        return not any(
            self.tiles[i][j] == value and (i, j) != position for i in range(box_start_row, box_start_row + 3)
            for j in range(box_start_col, box_start_col + 3))

    def solve(self):
        """
        Solve the Sudoku board using backtracking.

        Returns:
            bool: True if a solution is found, False otherwise.
        """
        next_tile = self.next_empty_tile()

        if not next_tile:
            return True

        else:
            row, col = next_tile

            for i in range(1, 10):
                if self.valid(i, next_tile):
                    self.tiles[row][col] = i

                    if self.solve():
                        return True

                    self.tiles[row][col] = 0

        return False
