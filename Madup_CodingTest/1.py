import math

def solution(n):
    answer = 1
    if 
    if n <= 2:
        return answer
    
    while n > 4:
        answer *= 3
        n -= 3
    answer *= n
    return answer

solution