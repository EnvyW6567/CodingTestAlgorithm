# https://school.programmers.co.kr/learn/courses/30/lessons/42860
import math

def solution(name):
    alpOps = {}
    length = len(name)
    for index, alphabet in enumerate(name):
        alpOps[index] = charChangeCount(alphabet)
    print(alpOps)
    start, answer, nearest = 0, 0, 0
    while(len(alpOps.keys()) > 0):
        minDistance = length
        if start in alpOps:
            answer += alpOps[start]
            del alpOps[start]
        for end in alpOps.keys():
            distance = getDistance(start, end, length)
            print(start, end, distance, minDistance)
            if start != end and minDistance > distance:
                nearest = end
                minDistance = distance
                print(distance, start, end)
                
        answer += minDistance
        start = nearest
    print(answer)

def charChangeCount(alphabet):
    alpNum = ord(alphabet) - 65
    if alpNum > 13:
        return 26 - alpNum
    return alpNum

def getDistance(start, end, length):
    if abs(end - start) > math.floor(length / 2):
        return length - abs(end - start)
    return abs(end - start)

name = "JEROEN"
print(name)
solution(name)