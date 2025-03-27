import sys

N = int(sys.stdin.readline())

for _ in range(N):
    words = sys.stdin.readline().split()

    for word in words:
        print(word[::-1], end=" ")
    print("")
