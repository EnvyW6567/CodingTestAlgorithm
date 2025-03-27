import sys

N = int(sys.stdin.readline())

count = 0
two_count = 0
five_count = 0

for i in range(1, N + 1):
    n = i
    while n % 2 == 0 or n % 5 == 0:
        if n % 2 == 0:
            n /= 2
            two_count += 1
        if n % 5 == 0:
            n /= 5
            five_count += 1

print(min(two_count, five_count))
