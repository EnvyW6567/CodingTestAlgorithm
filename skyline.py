# https://www.acmicpc.net/problem/1027
# 고층 빌딩
def sorted_swap(x, y):
    if x > y:
        return y, x
    return x, y


n = int(input())
heights = list(map(int, input().split()))
answer = 0

for i, height in enumerate(heights):
    can_see = 0
    for j, c_height in enumerate(heights):
        if i == j:
            continue

        s, e = sorted_swap(i, j)
        gap = (heights[e] - heights[s]) / (e - s)
        d, flag = 1, True
        for b in range(s + 1, e):
            if heights[b] >= heights[s] + gap * d:
                flag = False
                break
            d += 1

        if flag:
            can_see += 1
    answer = max(answer, can_see)

print(answer)
