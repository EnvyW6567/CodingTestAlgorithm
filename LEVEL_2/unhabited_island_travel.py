# https://school.programmers.co.kr/learn/courses/30/lessons/154540
def solution(maps):
    answer = []
    for idx, m in enumerate(maps):
        maps[idx] = list(m)
    for row in range(len(maps)):
        for col in range(len(maps[0])):
            if maps[row][col] != 'X':
                maps, food_sum = search(maps, (row, col))
                answer.append(food_sum)
    if len(answer) == 0:
        answer.append(-1)
    answer = sorted(answer)
    return answer


def search(maps, start_node):
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    stack = [start_node]
    visited = {start_node: maps[start_node[0]][start_node[1]]}
    while len(stack) > 0:
        cur_node = stack.pop()
        for move in moves:
            next_node = (cur_node[0] + move[0], cur_node[1] + move[1])
            if (0 <= next_node[0] < len(maps) and 0 <= next_node[1] < len(maps[0]) and
                    maps[next_node[0]][next_node[1]] != 'X'):
                stack.append(next_node)
                visited[next_node] = maps[next_node[0]][next_node[1]]
                maps[next_node[0]][next_node[1]] = 'X'
    food_sum = 0
    for food in visited:
        food_sum += int(visited[food])
    return maps, food_sum


solution(["X591X", "X1X5X", "X231X", "1XXX1"])
