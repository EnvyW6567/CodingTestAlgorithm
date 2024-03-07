# https://school.programmers.co.kr/learn/courses/30/lessons/172927
import math

def solution(picks, minerals):
    efficiency = {
        "diamond" : 25,
        "iron" : 5,
        "stone" : 1
    }
    pickEff = {
        0: 25,
        1: 5,
        2: 1
    }
    chunks = []
    chunk = []
    picksSum = 0
    for pick in picks : 
        picksSum += pick
    if (picksSum*5 < len(minerals)):
        minerals = minerals[:picksSum*5]
    
    for index, mineral in enumerate(minerals):
        if index != 0 and index % 5 == 0:
            chunks.append(chunk)
            chunk = []
        chunk.append(efficiency[mineral])
        
        if index == len(minerals) - 1: 
            chunks.append(chunk)
            
    effSum = [(sum(chunkP), chunkP) for chunkP in chunks]
    sortedChunks = sorted(effSum, reverse = True)
    
    answer = 0
    chunkNum = 0
    for pickType, pick in enumerate(picks):
        while(pick != 0 and chunkNum < len(sortedChunks)):
            pick -= 1
            for mineral in sortedChunks[chunkNum][1]:
                answer += math.ceil(mineral / pickEff[pickType])
            chunkNum += 1
    print(answer)
    return answer

minerals =  ["stone", "stone", "stone", "stone", "stone", "diamond"]
picks = [0, 0, 1]
solution(picks, minerals)