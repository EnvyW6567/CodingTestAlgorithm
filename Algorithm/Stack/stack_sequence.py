import sys


def solution(N):
    stack = []
    answer = []
    num = 1

    for _ in range(N):
        dest = int(sys.stdin.readline())
        while True:
            if len(stack) > 0 and stack[len(stack) - 1] == dest:
                stack.pop()
                answer.append("-")
                break
            else:
                stack.append(num)
                num += 1
                answer.append("+")
            if num > N + 1:
                return "NO"
    return answer


N = int(sys.stdin.readline())

answer = solution(N)

if answer != "NO":
    for a in answer:
        print(a)
else:
    print("NO")
