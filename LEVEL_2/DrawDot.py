# https://school.programmers.co.kr/learn/courses/30/lessons/140107
import math

def solution(k, d):
    answer = 0
    for i in range(0, d + 1, k):
        answer += math.floor(math.floor(math.sqrt(d*d - i*i)) / k) + 1
    return answer

k, d = 1, 5
solution(k, d)