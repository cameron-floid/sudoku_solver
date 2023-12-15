from Solver import Board


board = Board()
board.print()

solved = board.solve(board.tiles)

if solved:
    board.print(title="Solved Board")
else:
    board.print(title="Found No Solution")


