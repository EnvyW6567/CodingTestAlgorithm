def solution(board):
    answer = 0
    row_max, column_max = len(board), len(board[0])
    if row_max < 2 or column_max < 2:
        for row in board:
            for square in row:
                if square == 1:
                    return 1

    for row in range(1, row_max):
        for column in range(1, column_max):
            up = board[row - 1][column]
            left = board[row][column - 1]
            left_up = board[row - 1][column - 1]
            if board[row][column] > 0:
                board[row][column] = min(up, left, left_up) + board[row][column]
                if board[row][column] > answer:
                    answer = board[row][column]
    return answer ** 2


solution([[0, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [0, 1, 1, 1, 1], [1, 1, 1, 1, 1]])
# solution([[0, 0, 0], [0, 0, 0], [0, 0, 1]])
