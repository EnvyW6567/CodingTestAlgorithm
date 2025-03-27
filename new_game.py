import sys


def solution(K):
    turn = 1
    order = 0
    while turn <= 1000:
        if order >= K:
            order = 0
            turn += 1
            continue

        if str(order) not in locations:
            order += 1
            continue

        row, col = locations[str(order)]
        piece = board[row][col]

        next_row, next_col = next_location(piece)
        if is_out(next_row, next_col):
            directions[piece[0]] = reverse[directions[piece[0]]]
            next_row, next_col = next_location(piece)
            if is_out(next_row, next_col):
                order += 1
                continue

        board[row][col] = -1
        del locations[piece[0]]

        if world[next_row][next_col] == 1:
            piece = piece[::-1]

        if board[next_row][next_col] != -1:
            piece = board[next_row][next_col] + piece

        board[next_row][next_col] = piece
        locations[piece[0]] = (next_row, next_col)

        if len(piece) > 3:
            return turn

        order += 1
    return -1


def next_location(piece):
    row, col = locations[piece[0]]
    direction = directions[piece[0]]

    match direction:
        case 1:
            return row, col + 1
        case 2:
            return row, col - 1
        case 3:
            return row - 1, col
        case 4:
            return row + 1, col


def action(piece, row, col):
    if board[row][col] != -1:
        board[row][col] += piece
        return
    board[row][col] = piece


def is_out(row, col):
    if row < 0 or row >= len(board) or col < 0 or col >= len(board[0]) or world[row][col] == 2:
        return True
    return False


reverse = {
    1: 2,
    2: 1,
    3: 4,
    4: 3
}

N, K = map(int, sys.stdin.readline().split())

world = []
board = [[-1 for _ in range(N)] for _ in range(N)]
locations = {}
directions = {}

for _ in range(N):
    world.append(list(map(int, sys.stdin.readline().split())))

for i in range(K):
    row, col, direction = map(int, sys.stdin.readline().split())
    piece = str(i)

    board[row - 1][col - 1] = piece
    locations[piece] = (row - 1, col - 1)
    directions[piece] = direction

print(solution(K))
