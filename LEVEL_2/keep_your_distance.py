from collections import deque


def solution(places):
    answer = []

    for place in places:
        is_place_valid = True
        for row, line in enumerate(place):
            if not is_place_valid:
                break
            for column, section in enumerate(line):
                if section == 'P':
                    if not bfs(place, row, column):
                        is_place_valid = False
                        answer.append(0)
                        break
        if is_place_valid:
            answer.append(1)
    print(answer)
    return answer


def bfs(place, row, column):
    visited = {}
    q = deque()
    q.append((row, column, 0))
    while len(q) > 0:
        row, column, depth = q.popleft()
        if place[row][column] == 'P' and depth > 0:
            return False
        visited[(row, column)] = True
        if depth < 2:
            if (next_section := go_up(row, column, place)) is not False:
                if next_section not in visited:
                    q.append(next_section + (depth + 1,))
                    visited[next_section] = True
            if (next_section := go_down(row, column, place)) is not False:
                if next_section not in visited:
                    q.append(next_section + (depth + 1,))
                    visited[next_section] = True
            if (next_section := go_left(row, column, place)) is not False:
                if next_section not in visited:
                    q.append(next_section + (depth + 1,))
                    visited[next_section] = True
            if (next_section := go_right(row, column, place)) is not False:
                if next_section not in visited:
                    q.append(next_section + (depth + 1,))
                    visited[next_section] = True
    return True


def go_up(row, column, place):
    if row == 0:
        return False
    return check_valid_section(row - 1, column, place)


def go_down(row, column, place):
    if row == 4:
        return False
    return check_valid_section(row + 1, column, place)


def go_left(row, column, place):
    if column == 0:
        return False
    return check_valid_section(row, column - 1, place)


def go_right(row, column, place):
    if column == 4:
        return False
    return check_valid_section(row, column + 1, place)


def check_valid_section(row, column, place):
    if place[row][column] == 'X':
        return False
    return (row, column)


solution([["OPOPO", "OOOOO", "OOOOO", "OOOOO", "OOOOO"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
          ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
          ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]])
