from collections import deque


def move_robot(start, board):
    sr, sc = start
    directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
    visited = {(sr, sc)}
    queue = deque([(sr, sc, 0)])

    while queue:
        dest = []
        start = queue.popleft()

        # D 혹은 벽까지 탐색
        for direction in directions:
            nr, nc, depth = start

            while True:
                r, c = [x + y for x, y in zip([nr, nc], direction)]

                # 벽인지 확인
                if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or board[r][c] == 'D':
                    dest.append((nr, nc, depth))
                    break

                nr, nc = r, c

        for dr, dc, depth in dest:
            if (dr, dc) not in visited:
                if board[dr][dc] == 'G':
                    return depth + 1

                visited.add((dr, dc))
                queue.append([dr, dc, depth + 1])
    return -1


def solution(board):
    board = [list(b) for b in board]
    start = []

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == 'R':
                start = [r, c]
                break

    return move_robot(start, board)


print(solution(["...D..R", ".D.G...", "....D.D", "D....D.", "..D...."]))
