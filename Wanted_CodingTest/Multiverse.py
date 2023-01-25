from collections import defaultdict
import sys
from itertools import combinations

M, N = map(int, sys.stdin.readline().split())

planet = []
multiverse = defaultdict(int)

for m in range(M):
    planet = list(map(int, sys.stdin.readline().split()))
    before = 0
    univ = ""
    for i in range(N-1):
        for j in range(i+1, N):
            if planet[j] > planet[i]:
                univ += "2"
            elif planet[j] < planet[i]:
                univ += "0"
            else:
                univ += "1"

    multiverse[univ] += 1
answer = 0
for m in multiverse:
    if multiverse[m] > 1 : 
        answer += len(list(combinations(range(multiverse[m]),2)))
print(answer)