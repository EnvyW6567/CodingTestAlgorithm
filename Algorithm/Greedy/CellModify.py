from collections import defaultdict


def solution(n, k, cmd):

    dic = defaultdict(list)
    for i in range(n):
        dic[i].append(i-1)
        dic[i].append(i+1)
    iter = k
    stack = []
    for i in cmd:
        command = list(map(str, i.split()))
        if command[0] == 'U':
            for _ in range(int(command[1])):
                iter = dic[iter][0]
        if command[0] == 'D':
            for _ in range(int(command[1])):
                iter = dic[iter][1]
        if command[0] == 'C':
            stack.append(iter)
            # iter 가 마지막 번호 일 때
            if iter == n-1:
                dic[dic[iter][0]][1] = dic[iter][1]
                iter = dic[iter][0]
            # iter 가 첫 번호 일 때
            elif iter == 0:
                dic[dic[iter][1]][0] = dic[iter][0]
                iter = dic[iter][1]
            else:
                dic[dic[iter][0]][1] = dic[iter][1]
                dic[dic[iter][1]][0] = dic[iter][0]
                iter = dic[iter][1]

        if command[0] == 'Z':
            undo = stack.pop()
            if undo == 0:
                dic[dic[undo][1]][0] = undo
            elif undo == n-1:
                dic[dic[undo][0]][1] = undo
            else:
                dic[dic[undo][0]][1] = undo
                dic[dic[undo][1]][0] = undo
    answer = ''
    for i in range(n):
        if i in stack:
            answer = answer + 'X'
        else:
            answer = answer + 'O'
    return answer


n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]
solution(n, k, cmd)
# 양방향 링크드 리스트 느낌으로 구현을 해볼까 한다.

# 해당 딕셔너리에
