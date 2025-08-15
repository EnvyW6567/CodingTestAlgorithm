# https://www.acmicpc.net/problem/14761
# FizzBuzz

x, y, n = map(int, input().split())

for i in range(1, n + 1):
    flag = 0
    if i % x == 0:
        flag += 1
    if i % y == 0:
        flag += 2

    if flag == 1:
        print("Fizz")
    elif flag == 2:
        print("Buzz")
    elif flag == 3:
        print("FizzBuzz")
    else:
        print(i)
