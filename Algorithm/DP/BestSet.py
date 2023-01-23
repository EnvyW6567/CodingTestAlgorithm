def distribute(n, remain, sum):

    if n > remain:
        return remain, sum

    sum += int(remain / n)
    remain = remain % n
    return distribute(n, remain, sum)


def solution(n, s):  # n 원소의 갯수 , s 원소들의 합

    if n > s:
        return [-1]
    remain, sum = distribute(n, s, 0)
    answer = [sum for _ in range(n)]
    for i in range(n-1, n-remain-1, -1):
        answer[i] += 1
    return answer


n = 2
s = 9
print(solution(n, s))
