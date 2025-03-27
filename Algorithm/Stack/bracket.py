import sys


def solution(brackets):
    stack = []

    for bracket in brackets:
        if bracket == '(':
            stack.append(1)
        elif bracket == ')':
            if len(stack) == 0:
                return "NO"
            stack.pop()

    if len(stack) > 0:
        return "NO"
    return "YES"


N = int(sys.stdin.readline())

for _ in range(N):
    brackets = sys.stdin.readline()
    print(solution(brackets))
