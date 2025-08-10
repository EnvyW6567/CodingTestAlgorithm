# https://www.acmicpc.net/problem/13458
import math
import sys


def solution(n, rooms, b, c):
    answer = 0

    for room in rooms:
        if room < b:
            answer += 1
            continue

        answer += 1  # 총 감독관은 한 명 씩 있어야 한다
        answer += math.ceil((room - b) / c)  # 부 감독관 수
    return answer


n = int(sys.stdin.readline())

rooms = map(int, sys.stdin.readline().split())
b, c = map(int, sys.stdin.readline().split())

print(solution(n, rooms, b, c))
