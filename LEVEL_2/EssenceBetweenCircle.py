# https://school.programmers.co.kr/learn/courses/30/lessons/181187
import math

def solution(r1, r2):
    answer = 0
    
    for x in range(1, r2 + 1):
        outer = math.floor(math.sqrt(r2*r2 - x*x))
        if (r1 > x):
            inner = math.floor(math.sqrt(r1*r1 - x*x))
            if inner == math.sqrt(r1*r1 - x*x):
                answer += 1
        else:
            inner = 0
            answer += 1
        answer += outer - inner
    
    return answer * 4

r1 = 2
r2 = 3
solution(r1, r2)