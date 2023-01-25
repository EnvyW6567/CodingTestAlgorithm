import sys
import math

input = int(sys.stdin.readline())

div = []

answer = 0
end = int(math.sqrt(input))

for i in range(1, input+1):
    count = int(input / i)
    answer += count * i


print(answer)