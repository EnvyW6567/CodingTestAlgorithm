# https://school.programmers.co.kr/learn/courses/30/lessons/68645
def solution(n):
    answer = []
    triangle = [[0 for _ in range(n)] for _ in range(n)]
    triangle[0][0] = 1
    snail(triangle, "down", (0, 0), 1, n)
    for row in triangle:
        for col in row:
            if col != 0:
                answer.append(col)

    return answer


def snail(triangle, direction, start, count, n):
    while count < (n**2 + n) / 2:
        if direction == "down":
            while start[0] + 1 < n and triangle[start[0] + 1][start[1]] == 0:
                count += 1
                triangle[start[0] + 1][start[1]] = count
                start = (start[0] + 1, start[1])
            direction = "right"
        elif direction == "right":
            while start[1] + 1 < n and triangle[start[0]][start[1] + 1] == 0:
                count += 1
                triangle[start[0]][start[1] + 1] = count
                start = (start[0], start[1] + 1)
            direction = "left_up"
        elif direction == "left_up":
            while triangle[start[0] - 1][start[1] - 1] == 0:
                count += 1
                triangle[start[0] - 1][start[1] - 1] = count
                start = (start[0] - 1, start[1] - 1)
            direction = "down"


print(solution(6))
