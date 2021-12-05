from sys import stdin

data = [x.strip() for x in stdin.readlines()]

numbers = [int(x) for x in data[0].split(",")]

# gross
b = data[2:]
boards = []
while len(b) > 4:
    boards.append(b[:5])
    b = b[6:]

cleaned = []

for i in range(len(boards)):
    board = []
    for line in boards[i]:
        board.append([int(x.strip()) for x in line.split(" ") if x])
    cleaned.append(board)


def bingo(check, c):
    for line in check:
        if set(line).issubset(c):
            return True

    for i in range(5):
        line = [x[i] for x in check]
        if set(line).issubset(c):
            return True

    return False


called = []
won = []

for number in numbers:

    if len(boards) == 0:
        break

    called.append(number)

    for board in cleaned:
        if bingo(board, set(called)):
            unpack = [*board[0], *board[1], *board[2], *board[3], *board[4]]
            missing = [x for x in unpack if not x in called]
            won.append(sum(missing) * number)
            cleaned.remove(board)

print(won[0])
print(won[-1])
