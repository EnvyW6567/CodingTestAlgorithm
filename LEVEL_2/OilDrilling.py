# https://school.programmers.co.kr/learn/courses/30/lessons/250136
from collections import defaultdict

def solution(land):
    rowSize = len(land)
    columnSize = len(land[0])
    oilNum = 0

    for row in range(rowSize):
        for column in range(columnSize):
            if land[row][column] == 1:
                count, visited = dfs(land, (row, column))
                oilNum += 1
                for v in visited.keys():
                    visitedRow, visitedColumn = v
                    land[visitedRow][visitedColumn] = [oilNum, count]
    answer = 0
    for column in range(columnSize):
        oil = 0
        visitedOilSpot = []
        for row in range(rowSize):
            if land[row][column] != 0: 
                oilNum, sizeOfOil = land[row][column]
                if oilNum not in visitedOilSpot:
                    visitedOilSpot.append(oilNum)
                    oil += sizeOfOil
        if oil > answer:
            answer = oil
    print(answer)
    return answer

def dfs(land, startNode):
    visited = defaultdict(lambda : False)
    visited[startNode] = True # Initialize visited dict
    nodeStack = [startNode]
    count = 1
    while(len(nodeStack) != 0):
        node = nodeStack.pop()
        neighbour = checkNeighbor(land, node)
        for n in neighbour:
            if not visited[n]:
                count += 1
                visited[n] = True
                nodeStack.append(n)
    return count, visited

def checkNeighbor(land, node):
    neighbor = []
    row, column = node
    if row - 1 >= 0 and land[row - 1][column] == 1:
        neighbor.append((row - 1, column))
    if row + 1 < len(land) and land[row + 1][column] == 1:
        neighbor.append((row + 1, column))
    if column - 1 >= 0 and land[row][column - 1] == 1:
        neighbor.append((row, column - 1))
    if column + 1 < len(land[row]) and land[row][column + 1] == 1:
        neighbor.append((row, column + 1))

    return neighbor


land = [[1,1,1,1,1], [1,0,1,1,1], [1,0,0,0,0], [1,1,1,1,1]]
solution(land)