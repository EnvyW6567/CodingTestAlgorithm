import sys
from collections import deque


def solution(H):
    to_right = True
    for height in H:
        row = R - height
        if to_right:
            for col in range(C):
                if cave[row][col] == 1:
                    throw(row, col)
                    break
        else:
            for col in range(C - 1, -1, -1):
                if cave[row][col] == 1:
                    throw(row, col)
                    break

    for c in cave:
        for cc in c:
            print(cc, end='')
        print('')


def throw(row, col):
    cave[row][col] = 0
    if row == R:
        return
    after = search(row - 1, col)

    is_splited = True
    for row, _ in after:
        if row == R - 1:
            is_splited = False
            break

    if is_splited:
        for r, c in after:
            cave[r][c] = 0
        for r, c in after:
            cave[r + 1][c] = 1


def search(row, col):
    queue = deque([(row, col)])
    visited = {}

    while queue:
        row, col = queue.popleft()

        if row + 1 < R and cave[row + 1][col] == 1 and (row + 1, col) not in visited:
            queue.append((row + 1, col))
            visited[(row + 1, col)] = True
        if row - 1 > 0 and cave[row - 1][col] == 1 and (row - 1, col) not in visited:
            queue.append((row - 1, col))
            visited[(row - 1, col)] = True
        if col + 1 < C and cave[row][col + 1] == 1 and (row, col + 1) not in visited:
            queue.append((row, col + 1))
            visited[(row, col + 1)] = True
        if col - 1 > 0 and cave[row][col - 1] == 1 and (row, col - 1) not in visited:
            queue.append((row, col - 1))
            visited[(row, col - 1)] = True

    return visited


R, C = map(int, sys.stdin.readline().split())
cave = [[] for _ in range(R)]
mineral_count = 0

for r in range(R):
    row = sys.stdin.readline()
    for element in row:
        if element == 'x':
            cave[r].append(1)
            mineral_count += 1
        else:
            cave[r].append(0)

N = int(sys.stdin.readline())
H = list(map(int, sys.stdin.readline().split()))

solution(H)
