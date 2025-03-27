import math
import sys

A, B = map(int, sys.stdin.readline().split())

print(math.gcd(A, B))
print(A * B // math.gcd(A, B))
