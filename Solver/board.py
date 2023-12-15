class Board:

    def __init__(self):
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
            print("\nThe Entered Sodoku Board Is Not Valid!\n")
            exit()

    def print(self, title: str = "Board"):

        print(f"\n{title}:\n")

        for i in range(len(self.tiles)):

            if not i % 3 == 0 and i != 0:
                print()

            if i % 3 == 0 and i != 0:
                print("\n- - - - - - - - - - - -")

            for j in range(len(self.tiles[i])):
                if j % 3 == 0 and j != 0:
                    print(" | ", end="")

                print(self.tiles[i][j], end=" ")

        print("\n")

    def next_empty_tile(self):

        """
        Returns the next empty tile in the board
        :return:
        """

        for i in range(len(self.tiles)):
            for j in range(len(self.tiles[i])):
                if self.tiles[i][j] == 0:
                    return i, j

        return None

    def valid_board(self):
        size = len(self.tiles)
        for col in self.tiles:
            if len(col) != size:
                return False

        return True

    def valid(self, board, value: int, position: tuple) -> bool:

        # check row
        for i in range(len(self.tiles[0])):
            if self.tiles[position[0]][i] == value and i != position[1]:
                return False

        # check the col
        for i in range(len(self.tiles[0])):
            if self.tiles[i][position[1]] == value and i != position[0]:
                return False

        # check square
        box_start_row = position[0] // 3 * 3
        box_start_col = position[1] // 3 * 3

        i = box_start_row
        j = box_start_col

        while i < box_start_row + 3:
            while j < box_start_col + 3:
                if self.tiles[i][j] == value and (i, j) != position:
                    return False
                j += 1
            i += 1

        return True

    def solve(self, board):

        next_tile = self.next_empty_tile()

        if not next_tile:
            return True

        else:

            row, col = next_tile

            for i in range(1, 10):
                if self.valid(self.tiles, i, next_tile):
                    self.tiles[row][col] = i

                    if self.solve(self.tiles):
                        return True

                    self.tiles[row][col] = 0

        return False
