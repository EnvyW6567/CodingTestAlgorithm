from math import sqrt
from collections import deque


def lrud(r, c, N, board):
    node = []
    if r-1 >= 0:
        if board[r-1][c] != 1:
            node.append([r-1, c])
    if r+1 < N:
        if board[r+1][c] != 1:
            node.append([r+1, c])
    if c+1 < N:
        if board[r][c+1] != 1:
            node.append([r, c+1])
    if c-1 >= 0:
        if board[r][c-1] != 1:
            node.append([r, c-1])
    return node


# def bfs(board):
#     queue = deque([[0, 0]])  # 시작위치 0,0 설정
#     visited = []
#     while queue:
#         node = queue.popleft()
#         visited.append(node)
#         for n in board[node[0]][node[1]]:
#             if n not in visited and n not in queue:
#                 queue.append(n)
#                 # print(f'visited : {visited}, node : {n}, queue : {queue}')
#     print(visited)


def dfs(board):
    stack = [[0, 0]]
    visited = []
    while stack:
        node = stack.pop()
        visited.append(node)
        for n in board[node[0]][node[1]]:
            if n not in visited and n not in stack:
                stack.append(n)
    return visited


def show(visited, N):
    show = [[0 for _ in range(N)] for _ in range(N)]
    i = 1
    visited = deque(visited)
    while visited:
        idx = visited.popleft()
        show[idx[0]][idx[1]] = i
        i += 1
    for i in range(N):
        print("\n")
        for j in range(N):
            print(f'{show[i][j]}', end=" ")


def solution(board):

    answer = 0
    N = len(board)
    cost = [[0 for _ in range(N)]for _ in range(N)]
    newBoard = [[[]for _ in range(N)]for _ in range(N)]
    for r in range(N):
        for c in range(N):
            for n in lrud(r, c, N, board):
                newBoard[r][c].append(n)
    q = deque([[0, 0], [1, 1]])
    visited = dfs(newBoard)
    show(visited, N)

    return answer


board = [[0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 1, 0], [0, 0, 1, 0, 0, 0],
         [1, 0, 0, 1, 0, 1], [0, 1, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0]]
print(solution(board))
