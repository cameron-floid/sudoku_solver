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
