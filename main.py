from Solver import Board


board = Board()
board.display()

solved = board.solve()

if solved:
    board.display(title="Solved Board")
else:
    board.display(title="Found No Solution")


