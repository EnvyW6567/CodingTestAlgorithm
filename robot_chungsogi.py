# https://www.acmicpc.net/problem/14503
# 로봇 청소기

def rotate(direction):
    direction -= 1

    if direction < 0:
        return 3
    elif direction > 3:
        return 0
    return direction


def check_floor():
    global directions
    global room
    dirties_arr = []

    for x, y in directions:
        new_r, new_c = r + x, c + y
        if room[new_r][new_c] == 0:
            dirties_arr.append((new_r, new_c))

    return dirties_arr


N, M = map(int, input().split())
r, c, d = map(int, input().split())
room = []
answer = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
reversed_directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for _ in range(N):
    row = list(map(int, input().split()))
    room.append(row)

while True:
    if room[r][c] == 0:
        answer += 1
        room[r][c] = 2

    dirties = check_floor()

    if not dirties:
        # 후진
        r, c = map(sum, zip(reversed_directions[d], (r, c)))
        if room[r][c] == 1:
            break
        continue

    while True:
        # 반시계 90도 회전
        d = rotate(d)
        nr, nc = map(sum, zip(directions[d], (r, c)))
        if (nr, nc) in dirties:
            r, c = nr, nc
            break

print(answer)
