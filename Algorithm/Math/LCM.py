import math
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print(A * B // math.gcd(A, B))
