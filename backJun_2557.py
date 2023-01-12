import sys

# 마네킹이 있을경우 지나갈 수 없는 곳을 벽으로 바꿔줌


def mannequin(x, y):
    for i in range(-k, k+1, 1):
        xx = x+i
        if xx < 0 or xx >= n:
            continue
        count = k - abs(i)
        for j in range(count*2+1):
            yy = y-count+j
            if yy < 0 or yy >= n:
                continue
            if dept[xx][yy] == 0:
                dept[xx][yy] = 1


def route(x, y):
    for _ in range(len(chair)):


n, m, k = map(int, sys.stdin.readline().split())
chair = []

dept = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if dept[i][j] == 3:
            mannequin(i, j)
        elif dept[i][j] == 4:
            siru_x = i
            siru_y = j
        elif dept[i][j] == 2:
            chair.append([i, j])
print(chair)
