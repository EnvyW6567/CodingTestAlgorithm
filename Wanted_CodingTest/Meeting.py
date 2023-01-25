import sys

N, M, C = map(int, sys.stdin.readline().split())
W = []
for _ in range(C):
    W.append(list(map(int, sys.stdin.readline().split())))

nTend = list(map(int, sys.stdin.readline().split()))
mTend = list(map(int, sys.stdin.readline().split()))

satis = [[0 for _ in range(M)]for _ in range(N)]
for n in range(N):
    for m in range(M):
        satis[n][m] = W[nTend[n]-1][mTend[m]-1]

max = 0
idx = 0 # 현재 위치 m값
for n in range(N):
    cur_max = 0
    for m in range(M):
        cur = satis[n][m]
        if cur_max < cur:
            cur_max = cur

            
'''
현재 m보다 작은데
현재까지의 max값 보다 지금의 선택값이 더 클 경우 max = cur
현재 값보다 
'''