import sys

N, M = map(int, sys.stdin.readline().split())
n = 1
five_count = 0
two_count = 0

while N // pow(5, n) > 0 or N // pow(2, n):
    if N // pow(5, n) > 0:
        five_count += N // pow(5, n)
    if N // pow(2, n) > 0:
        two_count += N // pow(2, n)
    n += 1

n = 1
while M // pow(5, n) > 0 or M // pow(2, n) > 0:
    if N // pow(5, n) > 0:
        five_count -= M // pow(5, n)
    if N // pow(2, n) > 0:
        two_count -= M // pow(2, n)
    n += 1

n = 1
while (N - M) // pow(5, n) > 0 or (N - M) // pow(2, n) > 0:
    if N // pow(5, n) > 0:
        five_count -= (N - M) // pow(5, n)
    if N // pow(2, n) > 0:
        two_count -= (N - M) // pow(2, n)
    n += 1

print(min(five_count, two_count))
