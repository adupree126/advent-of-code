from functools import reduce


class board:
    def __init__(self):
        self.squares = []
        self.checked = [[False for i in range(5)] for j in range(5)]

    def addRow(self, newRow):
        squares = [newRow[i:i+2] for i in range(0, len(newRow), 3)]
        squares = [int(square) for square in squares]
        self.squares.append(squares)

    def getBoard(self) -> str:
        out_str = "board:\n"
        for i in range(5):
            for j in range(5):
                out_str += str(self.squares[i][j])
                if self.checked[i][j]:
                    out_str += "!"
                out_str += ", "
            out_str += "\n"
        return out_str

    def mark(self, called):
        for i in range(5):
            for j in range(5):
                if self.squares[i][j] == called:
                    self.checked[i][j] = True
                    break

    def isDone(self):
        rowStats = [reduce(lambda a, b: (a and b), row)
                    for row in self.checked]
        cols = [[self.checked[i][j] for i in range(5)] for j in range(5)]
        colStats = [reduce(lambda a, b: (a and b), col) for col in cols]
        # diags = [[self.checked[i][i]
        #          for i in range(5)], [self.checked[4 - i][i] for i in range(5)]]
        # diagStats = [reduce(lambda a, b: (a and b), diag) for diag in diags]
        return reduce(lambda a, b: a or b, rowStats + colStats)

    def uncheckedSum(self):
        total = 0
        for i in range(5):
            for j in range(5):
                if not self.checked[i][j]:
                    total += self.squares[i][j]
        return total


file = open('input')
moves = [int(move) for move in file.readline().split(',')]
boards = []
while file.readline() == '\n':  # flush the empty line
    newBoard = board()
    for i in range(5):
        newBoard.addRow(file.readline())
    boards.append(newBoard)
    print(newBoard.getBoard())
file.close()

finished = False
for move in moves:

    print("___PLAY: {}____".format(move))
    nextBoards = boards.copy()
    for board in boards:
        board.mark(move)
        finished = len(boards) == 1 and board.isDone()
        if board.isDone() and len(boards) > 1:
            nextBoards.remove(board)
            print('winning board removed! {} boards left'.format(len(boards)))
    boards = nextBoards
    if finished:
        print("finished last board left on move {}:".format(move))
        print(boards[0].getBoard())
        print("value: {}".format(boards[0].uncheckedSum() * move))
        break
