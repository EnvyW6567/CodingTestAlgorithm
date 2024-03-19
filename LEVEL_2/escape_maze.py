from collections import deque


def solution(maps):
    answer = 0
    for row, map_row in enumerate(maps):
        for column, spot in enumerate(map_row):
            if spot == "S":
                lever = bfs(maps, (row, column, 0), "L")
                if not lever:
                    return -1
                end = bfs(maps, lever, "E")
                if not end:
                    return -1
                _, _, answer = end
                return answer
    return -1


def bfs(maps, start_node, destination):
    visited = {}
    queue = deque([start_node])
    while len(queue) > 0:
        row, column, distance = queue.popleft()
        if maps[row][column] == destination:
            return row, column, distance
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            next_row, next_column = row + dx, column + dy
            if (0 <= next_row < len(maps) and 0 <= next_column < len(maps[0]) and maps[next_row][next_column] != "X"
                    and (next_row, next_column) not in visited):
                queue.append((next_row, next_column, distance + 1))
                visited[(next_row, next_column)] = True

    return False


solution(["SOOOL", "XXXXO", "OOOOO", "OXXXX", "OOOOE"])
