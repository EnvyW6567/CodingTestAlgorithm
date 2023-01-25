import sys
from collections import defaultdict

def lrud(r, c, N, M, planet):
    node = []
    if r-1 >= 0:
        if planet[r-1][c] != 1:
            node.append([r-1, c])
    else : 
        if planet[N-1][c] != 1:
            node.append([N-1, c])

    if r+1 < N:
        if planet[r+1][c] != 1:
            node.append([r+1, c])
    else : 
        if planet[0][c] != 1:
            node.append([0, c])
            
    if c+1 < M:
        if planet[r][c+1] != 1:
            node.append([r, c+1])
    else : 
        if planet[r][0] != 1:
            node.append([r, 0])

    if c-1 >= 0:
        if planet[r][c-1] != 1:
            node.append([r, c-1])
    else : 
        if planet[r][M-1] != 1:
            node.append([r, M-1])
    return node

def hashPlanet(N, M, planet):
    newPlanet = [[[]for _ in range(M)]for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if planet[r][c] == 0:
                for n in lrud(r, c, N, M, planet):
                    newPlanet[r][c].append(n)
    return newPlanet

def dfs(planet, hPlanet, r, c):
    stack = [[r, c]]
    visited = defaultdict(int)
    while stack:
        node = stack.pop()
        visited[node[0]*1000 + node[1]] = 1
        for n in hPlanet[node[0]][node[1]]:
            if visited[n[0]*1000 + n[1]] == 0:
                stack.append(n)
                planet[n[0]][n[1]] = 1
    return planet

N, M = map(int, sys.stdin.readline().split())

planet = []
for n in range(N):
    planet.append(list(map(int, sys.stdin.readline().split())))
    
hPlanet = hashPlanet(N, M, planet)
answer = 0
for n in range(N):
    for m in range(M):
        if planet[n][m] == 0:
            planet = dfs(planet, hPlanet, n , m)
            answer += 1
print(answer)